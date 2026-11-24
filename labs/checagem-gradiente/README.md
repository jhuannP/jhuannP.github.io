# Checagem de gradientes — passo, função e diagnóstico

27/10/2026. Ampliação da aula existente `dl-checagem-gradiente`, com14seções e12exercícios. Mantidos exemplo, Python anterior, desafio e IDs cg1/cg2. Notas, figura e código originais com apoio de IA, em rascunho para revisão pessoal. Trilha complementar, sem domínio certificado ou curso concluído.

## Função fixa e derivada pretendida

Para função escalar real J(θ), compare o vetor analítico com diferenças centrais por coordenada:

Dᵢ(h)=[J(θ+h eᵢ)−J(θ−h eᵢ)]/(2h).

Fixe dados, rótulos, parâmetros restantes, regularização, redução e estado. As duas avaliações não incluem atualização de pesos. Cada componente requer duas avaliações; para p parâmetros são2p avaliações na rotina básica. Não é um método de treinamento.

Taylor em uma coordenada, sob suavidade suficiente, cancela termos pares. Com quinta derivada limitada na vizinhança, Dᵢ(h)=∂ᵢJ+h²∂ᵢ³J/6+O(h⁴). Com terceira derivada limitada, temos o erro O(h²). Essa análise é de truncamento, não de arredondamento. Passos pequenos podem amplificar erro da subtração; não há melhor h universal.

## Exemplo com referência algébrica independente

J(a,b)=a⁴/4+ab+b²/2; ∇J=(a³+b,a+b). Em(1,2), J=17/4 e ∇J=(3,3).

Por expansão direta, Dₐ(h)=a³+b+a h² e Dᵦ(h)=a+b em aritmética exata. Em(1,2), h=0,1;0,01;0,001 dão Dₐ=3,01;3,0001;3,000001, com erros0,01;0,0001;0,000001. É um oráculo algébrico para a estimativa numérica, não uma rede neural.

Em float, 1e20+J pode perder a diferença entre avaliações apesar de a derivada matemática permanecer igual. Se θᵢ±h arredondar para θᵢ, o laboratório gera erro. Ele não detecta automaticamente todo cancelamento na perda: esse problema precisa ser investigado pela escala e pelos resultados.

## Critério declarado e falsos acordos

Por componente, usar |analítico−numérico|≤atol+rtol×max(|analítico|,|numérico|). O termo absoluto evita divisão por uma derivada zero; o relativo acompanha a escala. Afrouxar tolerâncias até passar não é validação.

Direção u=(1,1): tanto(3,3) quanto o gradiente incorreto(4,2) têm produto escalar6. O erro(1,−1) é ortogonal a u. Checagem por coordenadas ou outra direção pode revelá-lo. A direção não é normalizada neste exemplo; o denominador é2h para a perturbação hu declarada. Uma direção fixa não determina todo o vetor.

ReLU em zero: diferença central1/2, mas derivada clássica inexistente porque as laterais são0 e1. Divergir da convenção0 de uma implementação não prova um bug nesse ponto. Também testar pontos diferentes: o gradiente sempre zero passa em(0,0) do polinômio e falha em(1,2).

## Ligação à rede manual existente

O novo teste importa `dense_net.py` da raiz; não duplica ou modifica o modelo. Rede2→H→1, tanh/BCE, média por N; penalidade λ/2 sobre W/v, sem biases. Contagem: W2H+bH+vH+c1=4H+1 parâmetros.

Casos H=2/semente42 e H=4/semente43; dados fixos[[0.2,-0.7],[0.9,0.3],[-0.4,0.8]], y=[0,1,1]; λ=0 e0,07, passos1e-4,1e-5,1e-6. Os26parâmetros entre as duas redes são comparados nos seis pares λ/passo:156comparações escalares. Tolerâncias nesse teste:atol1e-7,rtol1e-4. São critérios locais, não uma recomendação universal.

Falhas introduzidas de propósito: trocar a média pelo gradiente de soma do termo de dados; retirar a penalidade do gradiente comparando com a perda regularizada. O teste exige detectar discrepâncias. Os exemplos anteriores da página continuam checando apenas c e um peso com penalidade; o novo laboratório amplia os grupos verificados.

## Código e execução

`check.py`: Python padrão, vetores reais não vazios e finitos; passo absoluto positivo, tolerâncias não negativas. `central` percorre coordenadas; `directional` aceita vetor não nulo da mesma dimensão; `compare` devolve entradas analítica/numérica, erro, limite e aprovação por componente. Usa tuplas novas e não altera a lista de parâmetros original. Não controla a aleatoriedade ou estado interno de uma função fornecida pelo usuário: determinismo é pré-condição, não garantia da API.

Rodar da raiz do protótipo, para também encontrar `dense_net.py`:

```sh
python3 -m unittest discover -s labs/checagem-gradiente -t .
```

Cinco testes: padrão algébrico de erro do polinômio; todos os parâmetros das redes e falhas controladas; falso acordo direcional; ReLU e perda arredondada; contratos/estado. Quadraturas, frameworks, GPU e treino não são executados por esse laboratório. Os testes não substituem demonstração, avaliação externa ou revisão pessoal.

## Fontes consultadas parcialmente

- [Dive into Deep Learning1.0.3, §5.3](https://d2l.ai/chapter_multilayer-perceptrons/backprop.html), em27/10/2026: função objetivo, grafo e penalidade. A forma e o exemplo deste laboratório são próprios; sem leitura integral do livro.
- [PyTorch2.14, Gradcheck mechanics, real-to-real functions](https://docs.pytorch.org/docs/2.14/notes/gradcheck.html), em27/10: diferenças centrais por coordenadas e comparação com derivadas. A página stable redirecionou para2.14. Não implementa ou executa a API, números complexos ou checagem de segunda derivada.

Exercícios, números, derivação específica, diagrama e código são originais. Fonte é referência de princípios, não evidência de integração com PyTorch.

## Resoluções e revisão

1. Exemplo anterior:4e-6/(2e-6)=2.
2. Reduzir h sem limite não garante precisão.
3. ∂J/∂a=1³+2=3.
4. Dₐ(0,1)=3,01 em aritmética exata.
5. Erro0,01.
6. Rede com H=2 tem9parâmetros.
7. (4,2)·(1,1)=6, falso acordo possível.
8. Diferença central de ReLU em zero=1/2.
9. Usar a mesma média e penalidade nas duas rotas.
10. Uma direção pode ocultar componentes de erro ortogonais.
11. Acordo em(0,0) não demonstra correção global.
12. Máscaras diferentes não representam em geral a mesma função de diagnóstico.

Próxima revisão pessoal20min: derivar o polinômio, prever o erro de cada passo e explicar a direção que esconde discrepância. Depois conferir média e penalidade da rede. Registro pessoal permanece em branco. Dropout, normalização com estado, redes grandes, derivadas superiores e robustez de diagnóstico geral continuam pendentes.
