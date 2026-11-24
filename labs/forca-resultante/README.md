# Força resultante e movimento

Rascunho original, 21/10/2026, para revisão de Jhuann. Estudo de ensino médio; Python é opcional. A página permite estudar equações e resolver exercícios sem programar.

## Modelo

Partícula sobre apoio horizontal ideal, sem atrito ou arrasto. Duas forças prescritas constantes, para direita/esquerda; massa positiva constante; referencial inercial, x(0)=0, SI e g=10 m/s². Vertical em equilíbrio: N=mg. A resultante horizontal não depende da velocidade. Portanto continua atuando na inversão: não é um modelo de atrito ou freio que desliga.

Caso principal: m=3 kg, Fdireita=12 N, Fesquerda=6 N, v0=−2 m/s. Resultante 6 N, a=2 m/s². Em 1 s, v=0, x=−1 m; em 2 s, v=2 m/s e x=0. Deslocamento zero não significa distância zero: a distância no intervalo é 2 m. O painel exibe deslocamento com sinal, sem rotulá-lo como distância.

Diagrama: setas horizontais em 6 px/N; verticais em 1,7 px/N. Escalas diferentes explicitadas; não comparar comprimentos entre esses grupos. N/P equilibram a vertical, mas são forças recebidas pelo mesmo corpo, não parceiros da terceira lei. Gráfico separado de velocidade versus tempo, escala vertical adaptativa; não representa posição ou força.

## Verificação reproduzível

Na raiz do protótipo:

```sh
python3 labs/forca-resultante/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Quatro testes: 243 combinações contra fórmulas com frações exatas; impulso e variação do momento, trabalho e variação de energia cinética nos mesmos casos; inversão, resultante zero e sinais; domínio inválido. Oitenta e uma configurações adicionais cruzadas Python/JavaScript. O trabalho se refere às duas forças constantes: W=Fresultante Δx. Os balanços são verificações algébricas do modelo, não dados experimentais.

## Fontes públicas consultadas parcialmente em 21/10/2026

- [OpenStax Physics §4.2](https://openstax.org/books/physics/pages/4-2-newtons-first-law-of-motion-inertia): primeira lei e distinção entre manter velocidade e alterar movimento.
- [OpenStax Physics §4.3](https://openstax.org/books/physics/pages/4-3-newtons-second-law-of-motion): resultante, aceleração, massa e unidades.
- [OpenStax Physics §4.4](https://openstax.org/books/physics/pages/4-4-newtons-third-law-of-motion): agentes, sistemas e forças de interação em corpos diferentes.

Consulta das explicações pertinentes, sem reproduzir figuras, exercícios ou exemplos. Diagrama, condições iniciais, sequência e verificações são próprios. Não houve nova leitura de um livro privado neste bloco. Referência pública não implica cobertura curricular ou de vestibular completa.

Ainda faltam atrito estático/cinético, planos inclinados, sistemas de corpos, forças variáveis, referenciais acelerados e comparação com medidas reais. A primeira lei não é deduzida de m a como definição de referencial; a aula declara o referencial inercial como hipótese operacional. Nenhum experimento foi executado, e o rascunho não certifica domínio pessoal.
