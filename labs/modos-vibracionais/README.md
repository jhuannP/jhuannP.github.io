# Modos longitudinais: cadeia livre 1-M-1

Rascunho original, 16/10/2026. Execute experiment.py em Python 3.
Na raiz: python3 -m unittest labs.modos-vibracionais.test_experiment.

Duas molas iguais k, três massas 1,M,1, nenhuma parede ou campo externo.
Somente três deslocamentos longitudinais: uma translação e dois estiramentos.
V=k[(q2-q1)²+(q3-q2)²]/2. Matriz de massa diag(1,M,1).
Autovalores generalizados: 0,k,k(1+2/M); vetores (1,1,1),(-1,0,1),(1,-2/M,1).
O sinal de um vetor não altera o modo. O código oferece normalização por massa;
o desenho normaliza a maior componente para módulo 1 e usa A=0,15.

Unidades: m0, k0, l0, tempo sqrt(m0/k0). Ω físico exige fator sqrt(k0/m0).
O painel não mostra Hz ou cm-1. Fase seleciona uma configuração, sem comparar
um mesmo instante entre sistemas diferentes. A translação zero é estática,
q=0,15(1,1,1), v=0, e ignora fase; a família geral do modo zero inclui deriva.

Uma triatômica linear tem quatro modos vibracionais na descrição 3D usual;
o painel contém só dois estiramentos. Sem flexões, resposta eletrônica,
atividade/intensidade IV/Raman, anharmonicidade ou molécula real identificada.

Quatro testes: identidades Fraction no problema generalizado, ortogonalidade
com massas, energia/centro de massa, integração independente velocity Verlet
para superposição e refinamento, escalas e domínio. 36 referências Python em
reference.json são conferidas pelo JavaScript, com forças e energia adicionais.
O laboratório é somente biblioteca padrão, sem pacote científico obrigatório.

Fontes parciais, consulta em 16/10/2026:
- Miessler/Fischer/Tarr, Química Inorgânica, quinta edição brasileira,
  Pearson 2014, acervo privado, seção 4.4. Trechos pp. 103/107
  (PDF 118/122); página 107 inspecionada visualmente para critério IV.
  Trecho Raman da p. 110 extraído, mas não usado para implementar regras
  nem confundir polarização e polarizabilidade. Não se atribui o modelo
  de três massas ao livro e não se reproduzem figuras/exercícios.
- [Feynman I, 49–4/49–5](https://www.feynmanlectures.caltech.edu/I_49.html):
  modos de sistemas lineares e superposição. Exemplo de cadeia próprio.

Pendente: simetria de todos os modos moleculares 3D, flexões, regras IV/Raman,
constantes experimentais, unidades espectroscópicas, revisão e prática pessoal.
