# Faraday e Lenz — notas de aula

Aula existente aprofundada. Exemplo1→7 Wb em3s/fem média−2V, Python, desafio e painel linear preservados. Nova geometria de barra móvel e campo elétrico azimutal sob simetria. Rascunho; revisão pessoal pendente.

Fonte: Feynman, Leighton e Sands, The Feynman Lectures on PhysicsII, edição oficial online, §§17–1/17–2, consulta parcial em27/10/2026. Fundamentos: contribuição elétrica/magnética, contorno fixo, barra e cuidado com circuitos móveis. Não é leitura integral dos capítulos16–17. Números, figura, balanços e exercícios próprios; sem copiar imagens/texto do livro. https://www.feynmanlectures.caltech.edu/II_17.html

Orientação+z e contorno anti-horário. Contorno fixo: fem=−dΦ/dt; geometria axial ideal com raioa tem Eφ=−rḂ/2 dentro e−a²Ḃ/(2r) fora. Barra emB+z, comprimentoℓ, velocidadev em+x: fem=−Bℓv,I=fem/R,Fmag,x=IℓB. Velocidade mantida, resistência positiva, sem autoindutância/radiação. Potência externa=I²R. Circulação/fem emV, E emV/m, força emN; trabalho mecânico vem de quem puxa. Fonte da figura é o desenho original, não figura do Feynman.

Rodar na raiz: `python3 -m unittest discover -s labs/faraday-barra -t .`. Biblioteca padrão, float, números finitos. Não resolve campo completo, franja, autoindutância, contatos gerais ou disco de Faraday. A regra do fluxo não deve ser aplicada a um circuito arbitrário sem identificar geometria/movimento. Nenhum experimento pessoal foi realizado. Painel anterior usa apenas fluxo linear em contorno fixo.

## 27/10/2026 — Faraday, barra móvel e balanço

Aula `f3-faraday` aprofundada de3 para14 seções e2 para12 exercícios. IDs, exemplo1→7Wb/3s, Python, desafio e painel anteriores preservados. Normal/contorno, fem média versus instantânea e Lenz; campo induzido axial dentro/fora de fluxo cilíndrico imposto. Barra móvel com corrente, força de frenagem, fonte mecânica e potênciaJoule0,045W. Condições de circuito resistivo quase estacionário explícitas; sem autoindutância, franja, radiação ou contatos gerais. Não confundir ∮E·dl no contorno fixo com contribuição magnética na barra móvel.

Fonte: Feynman/Leighton/Sands, Lectures on PhysicsII, edição oficial online, §§17–1/17–2 consultados parcialmente em27/10/2026: https://www.feynmanlectures.caltech.edu/II_17.html . Distinção entre campos/circuitos móveis e limites da regra do fluxo; sem leitura integral dos capítulos16–17 ou reprodução de figuras/texto. Campos idealizados, exemplos numéricos, figura e exercícios próprios; nenhum experimento pessoal ou dado de pesquisa/cliente. Júpiter não reaberto nesta sessão.

Verificação:14 testes do catálogo e cinco locais aprovados;788 estruturas MathML conferidas. Testes: exemplo,36 estados de barra/energia/sinais, circulação vetorial por quadratura em15 casos, rotacional radial/continuidade do modelo axial e diferença temporal de fluxo, zero/contratos. Não é verificação de campo completo ou garantia geral de precisão float. No navegador390px, força rejeitou+0,015 e aceitou−0,015N pelo Enter. Painel preservado respondeu Home/End; taxa−3Wb/s por espira/N1 exibiu fem+3V. Figura corrente/força inspecionada em`faraday-barra-mobile.jpg`; documento390px, console sem erros. Leitor de tela, Windows real e revisão pessoal pendentes.

FísicaIII14 aulas/125 exercícios, quatro introduções curtas, sete grupos parciais e duas lacunas. Global51 trilhas,544 aulas/4269 exercícios e202 introduções curtas. Nenhum curso completo ou domínio pessoal certificado. Próxima ação: reconstruir sinais e balanço0,045W em20min. Próximo bloco global: inspecionar introdução de Probabilidade/Processos Estocásticos para aprofundar modelo temporal com referência. Saldo semanal81%; parada operacional65% mantida.
