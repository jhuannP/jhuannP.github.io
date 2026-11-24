'use strict';

const reviewFields = [
  ['universo', '1. Quem ficou no denominador?'],
  ['base', '2. E se a base mudar?'],
  ['registro-sinal', '3. Outra informação ou uma cópia?'],
  ['reflexao', 'Registro pessoal: o que consegui reconstruir?'],
];

document.querySelector('#review-form').addEventListener('submit', event => event.preventDefault());
document.querySelector('#exportar').addEventListener('click', () => {
  const status = document.querySelector('#export-status');
  const answers = reviewFields.map(([id, title]) => ({title, text: document.getElementById(id).value.trim()}));
  if (!answers.some(answer => answer.text)) {
    status.textContent = 'Escreva uma resposta ou reflexão antes de baixar seu registro.';
    document.getElementById('universo').focus();
    return;
  }
  const date = new Intl.DateTimeFormat('pt-BR').format(new Date());
  const markdown = [
    '# Meu registro de revisão — condicionamento e Bayes',
    `Data local da exportação: ${date}`,
    'Este arquivo contém respostas digitadas pelo visitante. Não representa avaliação ou certificação de domínio.',
    ...answers.map(answer => `## ${answer.title}\n\n${answer.text || '(não preenchido)'}`),
    'Referência do roteiro: /labs/condicional/revisao.html. Questões e soluções não incluídas nesta exportação.',
  ].join('\n\n') + '\n';
  const blob = new Blob([markdown], {type: 'text/markdown;charset=utf-8'});
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement('a');
  anchor.href = url;
  anchor.download = 'minha-revisao-condicional.md';
  document.body.append(anchor);
  anchor.click();
  anchor.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
  status.textContent = 'Download solicitado. Confira o arquivo na pasta de downloads antes de fechar esta aba.';
});
