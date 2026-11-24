# Euler simplético:estrutura,energia e fase

Extensão original assistida por IA,28/10/2026,revisão pessoal pendente.Não demonstra competência pessoal ou simulação de uma pesquisa.

## Fonte e limites de leitura

[Maria Cameron,AMSC660,SymplecticMethods](https://math.umd.edu/~cameron/SymplecticMethods.pdf),consulta textual parcial28/10/2026,§3.1 p.7/PDF7(oscilador e comparação de Euler) e§3.3 p.14/PDF14(composição drift∘kick).Data editorial não confirmada,sem leitura integral ou cópia de programa/figuras.As contas do invariante,cotas,ciclo e fase são deduções das notas,não transcrição da fonte.Burden10 mantém papel temático anterior,sem seção simplética afirmada.Hairer/Pisa retornou acesso negado,não usado como texto lido.Programa não reaberto neste bloco,versão da turma ainda não comprovada.

## Derivação

Massa normalizada:q′=p,p′=−ω²q;p é velocidade/momento por massa. Escolha L>0 e defina τ=ωt,Q=q/L,P=p/(ωL),η=hω. Energia por massa e=(p²+ω²q²)/2; E=e/(ω²L²).
P⁺=P−ηQ;Q⁺=Q+ηP⁺.M=[[1−η²,η],[−η,1]],det1.Em2D,MᵀJM=(detM)J;emdimensão maior,det1 não basta para simpleticidade.
I=(Q²+P²−ηQP)/2.SubstituaP=P⁺+ηQ no estado antigo eQ⁺=Q+ηP⁺ no novo:ambos dão[Q²+(P⁺)²+ηQP⁺]/2.Exatamente conservado em aritmética exata,sem afirmar que I é o Hamiltoniano exato gerador do mapa.
I=[(P−ηQ/2)²+(1−η²/4)Q²]/2.Para0<η<2 é positivo e(1−η/2)E≤I≤(1+η/2)E,deonde as cotas das notas paraE_n/E₀,E₀>0.
η1:(1,0),(0,−1),(−1,−1),(−1,0),(0,1),(1,1),(1,0).I1/2;Eoscila1/2–1.
η2:(Q_n,P_n)=(−1)ⁿ(1+2n,2n).I1/2 masE cresce quadraticamente.A forma é semidefinida;det1 eautovalores−1 não bastam.Não confundir módulo unitário com potências limitadas se há bloco deJordan.
η>2:forma indefinida,raiz real de módulo>1;há direção instável,sem afirmar que todo estado cresce.
Fase espectralθ=2arcsen(η/2),diferente do ângulo polar usual no plano não circular.Paraη1,n6,diferença2π−6.No tempo fixo,nηconstante,expansãoθ−η=η³/24+O(η⁵) implica erro espectralO(η²).O estado do método continua de primeira ordem em geral.

## Executar

```sh
python3 labs/euler-simpletico/invariant.py
python3 -m unittest discover -s labs/euler-simpletico -t .
```

Inteiros/Fraction somente;0<η≤3 e0–200passos,limites operacionais didáticos.Testa identidade/cotas com20pares de parâmetros/estados por40passos;ciclo/fronteira;determinante/fase/caso instável;contratos.Não testa toda função Hamiltoniana ou controla denominadores arbitrários de entradasFraction.Não é solver de produção.O código/painel anteriores foram preservados;eles mostram energia física,não este invariante.

## Revisão pessoal20min

Reproduzir a prova,explicar E1≠E0 no exemplo antigo comη0,1 econstância deI,derivar o crescimentoη2 ecomparar período6 com2π.Sem passos adaptativos certificados,sistemas dissipativos ou prova geral de estabilidade.Não conclui o tópico inteiro.
