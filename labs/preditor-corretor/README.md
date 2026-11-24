# AB2 + uma correção trapezoidal (PECE)

Rascunho original assistido por IA, aguardando revisão de Jhuann. Sem resultado científico ou competência pessoal atribuídos.

## Fonte e convenção

Fonte temática primária consultada em 16/10/2026: [NTNU, notas 6.4–6.5](https://www.math.ntnu.no/emner/TMA4215/2016h/notater/AdamsPredCorr.pdf), PDF de quatro páginas. Sustenta a construção do par e a distinção entre correções finitas e método implícito. Dedução do intervalo real, exemplos, implementação e testes desta aula são próprios; não reproduzem a tabela da fonte.

## Contrato

EDO escalar real, t=0 até T>0, passo fixo, 2 a 4096 passos. Inicialização por Heun, preditor AB2, uma correção com a fórmula do trapézio, avaliação da derivada corrigida. O início difere do RK4 usado na aula anterior de AB2. Custo desta implementação: 2n+1 avaliações, incluindo a última. Estados não finitos são rejeitados.

Para y′=λy, z=hλ: a=1+z+3z²/4, b=z²/4, y_next=a*y−b*y_prev. Polinômio r²−ar+b. Decaimento estrito no eixo real negativo: −2<z<0; em −2 há raiz dupla 1. A solução constante produzida pelo início específico nessa fronteira não certifica estabilidade robusta. Trapézio realmente resolvido usa (1+z/2)/(1−z/2); não confundir com uma correção explícita.

Defeito local sem divisão por h é O(h³) sob suavidade/Lipschitz; a ordem global 2 é verificada no problema de refinamento, sem prova geral do algoritmo composto. O limite f=0 tem raízes 1 e 0; isso não substitui teoria geral de zero-estabilidade/convergência.

## Executar

```sh
python3 labs/preditor-corretor/experiment.py
python3 -m unittest discover -s labs/preditor-corretor -t . -p 'test_*.py'
```

Quatro testes: recorrência independente em frações, reprodução de polinômios e custo, refinamento/defeito/raízes e contratos. `reference.json` cruza 24 configurações Python/JavaScript, incluindo fronteira e crescimento instável. A comparação usa erro absoluto, não apenas curvas semelhantes.

## Roteiro e respostas

No site, comece κ=2,n=16,T=4. Reduza n=4 (fronteira z=−2), depois κ=4 (z=−4). Troque para trapézio resolvido e veja alternância de sinal. O eixo vertical se adapta; segmentos numéricos não são a solução contínua.

Respostas dos dez exercícios: 1) h=1/2; 2) y₁=5/8; 3) P₂=13/32; 4) y₂=47/128; 5) 41 avaliações; 6) derivada corrigida; 7) −2<z<0; 8) raiz dupla 1; 9) R=−1/3; 10) refinamento não prova convergência geral.

Para aprofundar: prova de propagação sob hipóteses gerais, região complexa, outros pares, solvers implícitos e história em malha variável. Diferença previsão/correção não é certificado de erro ou adaptação implementada. Sem dados físicos reais.
