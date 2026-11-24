# Superposição linear: fase, nós e batimentos

Rascunho original pendente da revisão de Jhuann. Sem dados experimentais ou resultados pessoais de pesquisa. A proposta de exploração não é registrada como experiência realizada.

## Fontes consultadas em 16/10/2026

- [Feynman Lectures, vol. I, cap. 48](https://www.feynmanlectures.caltech.edu/I_48.html), edição online oficial em inglês: soma de frequências próximas, módulo da modulação e batimentos. O texto foi acessível; mídias não foram reproduzidas. O exemplar privado em português já identificado no acervo não foi usado para atribuir páginas equivalentes.
- [OpenStax University Physics I, 16.6](https://openstax.org/books/university-physics-volume-1/pages/16-6-standing-waves-and-resonance): padrões estacionários e condições de contorno. Não foram copiadas figuras ou exercícios.

As identidades são desenvolvidas com convenções explícitas; exemplos numéricos, exercícios, gráficos e código são próprios. Os livros do acervo continuam privados.

## Modelo, unidades e reprodução

A=0,01 m; frequência base 8 Hz. Nos cortes espaciais, lambda=1 m, k=2pi rad/m e c=8 m/s. `evaluate` retorna as duas componentes, soma e envelope em metros. O gráfico divide deslocamentos por A; a tabela mantém metros. `beat_metrics(0)` retorna período ausente, sem divisão por zero.

- Situação 0: mesma direção e frequência, fase relativa phi. A amplitude total é 2A|cos(phi/2)|.
- Situação 1: direções opostas, sem diferença de frequência; y=2Acos(kx)cos(omega t). A janela [0,1] m tem antinós nas bordas, não duas extremidades fixas. Nós interiores em 0,25 e 0,75 m.
- Situação 2: série temporal num ponto, frequências 8 e 8+df Hz. Envelope 2A|cos(pi df t)|. A janela positiva mostra dois períodos de batimento quando df>0; para df=0 usa 2 s e envelope constante. O cosseno com sinal tem período duplo do módulo; a frequência de batimento é df. Interpretação como envelope lento pede diferença pequena frente à média.

O controle de tempo escolhe um corte nos modos 0/1 e o marcador da série no modo 2. Fase só altera 0; diferença de frequência só altera 2. Não há áudio, aquisição de sinal ou ajuste a medições.

Na raiz: `python3 -m unittest discover -s labs/superposicao-ondas -t .`. Quatro testes verificam identidades, equação de onda por diferenças finitas, nós em múltiplos instantes, contorno senoidal separado, periodicidade dos batimentos, limite de frequências iguais e energia. As 76 configurações em `reference.json` também são cruzadas com JS; a concordância entre linguagens não substitui as referências algébricas.

## Energia e limites

`standing_energy` usa mu>0, tensão mu*c², densidade mu*y_t²/2+T*y_x²/2 e fluxo -T*y_x*y_t. Os testes fazem média em 1024 instantes de um período: fluxo médio zero, mas densidade média mu*A²*omega² positiva. Num nó, velocidade local zero não implica ausência de energia elástica associada à inclinação.

Na situação 0, a razão de potência em relação a uma componente é 4cos²(phi/2), para mesmo meio/frequência. Não aplique essa razão ao fluxo líquido do caso estacionário. As expressões valem no modelo linear ideal, sem dissipação.

## Exploração proposta

1. Preveja a amplitude em phi=0, pi/2 e pi e só depois mova o controle.
2. No caso estacionário, encontre um instante com todos os deslocamentos zero. Explique por que nem todos os pontos são nós.
3. Para 8 e 9 Hz, identifique máximos do envelope em 0,1,2 s e mínimos em 0,5 e 1,5 s. Diferencie mínimos do envelope dos numerosos zeros da portadora.
4. Compare df>0 e df=0. Uma ausência de período finito deve aparecer como estado explícito, não número inválido.

Reflexão fixa/livre, derivação completa da equação de onda, interfaces, pacotes dispersivos e modos gerais permanecem pendentes. A aula e Física II não estão concluídas, e aprovação acadêmica não comprova domínio atual desses assuntos.
