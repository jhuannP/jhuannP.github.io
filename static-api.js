/* Versão estática da API de server.py, para hospedagem sem servidor (GitHub Pages).
   Intercepta fetch('/api/...') e responde com JSON pré-gerado em /api-static/.
   A correção replica check_answer() de server.py; nesta versão as respostas ficam nos arquivos públicos. */
(function () {
  const BASE = '/api-static/';
  const realFetch = window.fetch.bind(window);
  const cache = new Map();
  const load = path => {
    if (!cache.has(path)) cache.set(path, realFetch(BASE + path).then(r => { if (!r.ok) { cache.delete(path); throw new Error('404'); } return r.json(); }));
    return cache.get(path);
  };
  const json = (value, status = 200) => new Response(JSON.stringify(value), { status, headers: { 'Content-Type': 'application/json; charset=utf-8' } });
  const notFound = () => json({ error: 'Conteúdo não encontrado.' }, 404);
  const fold = t => String(t).normalize('NFKD').toLowerCase().replace(/[̀-ͯ]/g, '');

  function number(value) {
    if (typeof value === 'boolean' || !['number', 'string'].includes(typeof value)) throw new Error('Use um número, por exemplo 0,5 ou 1/2.');
    const text = String(value).trim().replace(/,/g, '.');
    if (text.length > 80) throw new Error('A resposta numérica é muito longa.');
    const parts = text.split('/');
    const num = s => { const t = s.trim(); if (!/^[+-]?(\d+\.?\d*|\.\d+)(e[+-]?\d+)?$/i.test(t) && !/^[+-]?(inf|infinity|nan)$/i.test(t)) throw 0; return Number(t.replace(/^([+-]?)inf(inity)?$/i, '$1Infinity')); };
    let result;
    try {
      if (parts.length === 1) result = num(parts[0]);
      else if (parts.length === 2) { const d = num(parts[1]); if (d === 0) throw 0; result = num(parts[0]) / d; }
      else throw 0;
    } catch (_) { throw new Error('Use um número ou uma fração simples, por exemplo 0,5 ou 1/2, com denominador diferente de zero.'); }
    if (!Number.isFinite(result)) throw new Error('Use um número finito.');
    return result;
  }
  function check(ex, answer) {
    let correct;
    if (ex.type === 'numeric') {
      const received = number(answer), expected = ex.answer;
      correct = Math.abs(received - expected) <= (ex.tolerance ?? 1e-6) * Math.max(1, Math.abs(expected));
    } else {
      if (typeof answer === 'boolean') throw new Error('Selecione uma alternativa.');
      const s = String(answer).trim();
      if (!/^[+-]?\d+$/.test(s)) throw new Error('Selecione uma alternativa.');
      const received = parseInt(s, 10);
      if (!(received >= 0 && received < ex.options.length)) throw new Error('Selecione uma alternativa válida.');
      correct = received === ex.answer;
    }
    return { correct, feedback: correct ? ex.solution : ex.hint };
  }

  async function handle(url, init) {
    const seg = url.pathname.replace(/^\/|\/$/g, '').split('/').map(decodeURIComponent);
    const method = (init && init.method || 'GET').toUpperCase();
    try {
      if (method === 'POST') {
        if (url.pathname !== '/api/check') return json({ error: 'Endpoint não encontrado.' }, 404);
        let payload;
        try { payload = JSON.parse(init.body); } catch (_) { return json({ error: 'Use uma resposta válida, por exemplo 0,5 ou 1/2.' }, 400); }
        const answers = await load(`answers/${encodeURIComponent(payload.lessonId)}.json`).catch(() => null);
        const ex = answers && answers[payload.exerciseId];
        if (!ex) return json({ error: 'Exercício não encontrado.' }, 404);
        try { return json(check(ex, payload.answer)); } catch (e) { return json({ error: e.message }, 400); }
      }
      if (url.pathname === '/api/health') { const c = await load('catalog.json'); return json({ status: 'ok', courses: c.totalCourses, lessons: c.totalLessons, schemaVersion: 1 }); }
      if (url.pathname === '/api/catalog') {
        const c = await load('catalog.json'), q = fold(url.searchParams.get('q') || '').slice(0, 150), area = url.searchParams.get('area') || '';
        const courses = c.courses.filter(x => (!area || x.area === area) && (!q || x._search.includes(q))).map(({ _search, ...rest }) => rest);
        return json({ courses, totalCourses: c.totalCourses, totalLessons: c.totalLessons });
      }
      if (seg.length === 3 && seg[1] === 'courses') return json(await load(`courses/${encodeURIComponent(seg[2])}.json`));
      if (seg.length === 3 && seg[1] === 'lessons') return json(await load(`lessons/${encodeURIComponent(seg[2])}.json`));
      if (seg.length === 5 && seg[1] === 'lessons' && seg[3] === 'solutions') {
        const ex = (await load(`answers/${encodeURIComponent(seg[2])}.json`))[seg[4]];
        return ex ? json({ solution: ex.solution }) : notFound();
      }
    } catch (_) { return notFound(); }
    return notFound();
  }

  window.fetch = function (input, init) {
    const url = new URL(typeof input === 'string' ? input : input.url, location.href);
    if (url.origin === location.origin && url.pathname.startsWith('/api/')) return handle(url, init);
    return realFetch(input, init);
  };

  /* O download do exemplo em Python usa um arquivo estático; dá a ele o nome <aula>.py. */
  document.addEventListener('click', e => {
    const a = e.target.closest && e.target.closest('a[href^="/api/lessons/"][href$="/python"]');
    if (a) a.setAttribute('download', decodeURIComponent(a.getAttribute('href').split('/')[3]) + '.py');
  }, true);
})();
