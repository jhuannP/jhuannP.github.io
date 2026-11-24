# Ridge em uma reta — objetivo, escala e avaliação

27/10/2026. Notas de aula originais com apoio de IA, em rascunho; revisão pessoal de Jhuann pendente. Aprofundamento de `ml-ridge`, percurso complementar de machine learning. Não representa disciplina concluída, produção ou resultado de cliente/pesquisa.

## Fontes e escopo

Bishop, *Pattern Recognition and Machine Learning*,2006, §3.1.4 pp.144–146/PDF163–165, consulta parcial em27/10/2026; p.145/PDF164 renderizada e conferida visualmente. Fonte escreve erros e penalidade com fatores1/2; multiplicar o objetivo inteiro por2 não altera o mínimo. Nossa restrição a uma reta com intercepto não penalizado é declarada e deduzida, sem tratar automaticamente toda parametrização da fonte como idêntica. Livro privado autorizado não distribuído, sem copiar figuras ou exercícios nem alegar leitura integral.

[Scikit-learn, §1.1.2.1 Ridge](https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression-and-classification), consulta parcial27/10/2026: página estável exibiu versão1.9.1 e objetivo de soma penalizada. Pacote não instalado ou executado; não se apresenta o laboratório como reimplementação de todos os solvers do pacote. API e solver não foram inferidos a partir de versões anteriores.

Pré-requisito: aula de regressão afim e noções de derivadas, média e SSE. Exemplo original, Python float/desafio e painel `ridgeShrinkage` foram preservados. Novo laboratório usa racionais e tem contratos próprios explícitos.

## Derivação e mínimo global

Dados não vazios(xᵢ,yᵢ), n≥1. Previsão ŷᵢ=w xᵢ+b. Objetivo J=SSE+λw², λ≥0; b livre, sem penalidade. Unidade de J é a de y², quando os dados têm unidades físicas.

∂J/∂b=2∑(w xᵢ+b−yᵢ)=0 dá b=ȳ−w x̄. Defina Sxx=∑(xᵢ−x̄)², Sxy=∑(xᵢ−x̄)(yᵢ−ȳ), Syy=∑(yᵢ−ȳ)². O objetivo reduzido é Syy−2wSxy+(Sxx+λ)w². Se Sxx+λ>0, seu mínimo tem wλ=Sxy/(Sxx+λ), bλ=ȳ−wλx̄.

Para perturbações u,v:

J(wλ+u,bλ+v)−J(wλ,bλ)=(Sxx+λ)u²+n(v+x̄u)².

Se Sxx+λ>0, só u=v=0 zera essa soma: mínimo global único. Se x é constante eλ=0, Sxx=0 eSxy=0; qualquer w com b=ȳ−wx̄ minimiza o objetivo, cujo SSE éSyy. A exceção da rotina significa não escolher um mínimo da família, não ausência de solução. Seλ>0, w=0,b=ȳ é único.

Com e=ŷ−y, as condições são∑e=0 e∑x e=−λw. A ortogonalidade com x deOLS não continua automaticamente válida quando há penalidade.

## Exemplo original e três convenções

x=[−1,0,1], y=[−2,0,2], médias zero, Sxx=2,Sxy=4.

| λ | w | b | SSE | Penalidade λw² | J da própria linha |
|---:|---:|---:|---:|---:|---:|
|0|2|0|0|0|0|
|2|1|0|2|2|4|
|6|1/2|0|9/2|3/2|6|

Os objetivos em linhas comλ diferentes não são a mesma função. Para comparar minimização, fixeλ: comλ=2, a reta w=1 temJ=4 e a retaOLS w=2 temJ=8. Ridge escolhe o menor objetivo penalizado, embora aumente o erro de treino.

1. **SSE versus MSE:** SSE+λw² eMSE+μw² têm o mesmo mínimo quandoλ=nμ. No exemplo, μ=2/3. Multiplicar ambos os termos pelo mesmo fator é diferente de mudar apenas um.
2. **Duplicar todas as linhas:** comλ=2 fixo, Sxy8/Sxx4 dáw=4/3. Comλ=4, volta aw=1. Na convenção de média, a duplicação inteira preserva a MSE. Duplicar observações não as torna medições independentes.
3. **Unidades:** x′=c x pede w′=w/c,b′=b eλ′=c²λ para mesmas previsões e penalidade. Comc=100, λ=2 vira20000 e w=1 vira0,01. Manterλ=2 nessa escala daria w′=200/10001, produzindo previsões diferentes. Se y tem unidadeUy e x temUx, λ tem unidadeUx² nesta convenção.

Somar uma constanted ax mantém a inclinação e exige b′=b−wd; somar d ay mantém a inclinação e aumenta b emd. Centralização e mudança de escala não são a mesma transformação. Estatísticas aprendidas de dados pertencem ao treino de cada divisão, sem vazamento.

## Sensibilidade não é garantia fora do treino

Perturbe só o último alvo do exemplo para2+δ. Sxy aumentaδ eȳ aumentaδ/3. A inclinaçãoOLS mudaδ/2; comλ=2 mudaδ/4. O intercepto mudaδ/3 nos dois casos. Menor resposta da inclinação a essa perturbação não prova menor variância geral ou menor erro de previsão.

No ponto novo sintético x=2,y=4 da regra y=2x, OLS prevê4 e tem erro quadrado0; Ridge deλ=2 prevê2 e tem erro quadrado4. É contraexemplo de promessa universal, não estimativa de risco populacional. λ deve ser escolhido com validação apropriada, sem usar o teste final; transformações precisam ser reajustadas no treino. A escolha efetiva não é automatizada neste laboratório.

## Laboratório e verificação

`ridge.py` usa apenas Python padrão eFraction. Dados em listas/tuplas não vazias do mesmo tamanho; valoresint/Fraction, semfloat/bool. λ não negativo. `Fit` é imutável, com coeficientes racionais validados; `predict`, `sse` e `objective` mantêm a convenção. Não muda dados e não opera como Ridge multivariado. O código float original permanece distinto; teste racional não prova sua estabilidade para toda entrada.

```sh
python3 -m labs.ridge-reta.ridge
python3 -m unittest discover -s labs/ridge-reta -t .
```

Cinco testes selecionados: solução centrada contra equações normais brutas por Cramer; decomposição global em216ajustes e25perturbações por ajuste; unidades/translações/duplicação; exemplos e sensibilidade; x constante, não unicidade, contratos e preservação de dados. Referências são cálculos algébricos exatos, sem importar scikit-learn. Não são benchmark, comprovação de generalização ou análise de condicionamento de problemas gerais.

## Resoluções dos12 exercícios

1. Inclinação do exemplo:1.
2. Mesmaλ não preserva efeito após toda mudança de unidade de x.
3. SSE regularizada:2.
4. Objetivo regularizado:4.
5. Penalidade equivalente na MSE:2/3.
6. Duplicação comλ=2 fixo: w=4/3.
7. x′=100x pedeλ′=20000.
8. ∑x e=−2 no exemplo regularizado.
9. x constante eλ=0 tem família de mínimos, não inexistência.
10. Translação do alvo é absorvida pelo intercepto livre.
11. Erro quadrado4 no ponto novo sintético para w=1,b=0.
12. Menor sensibilidade específica não garante menor erro externo.

Revisão20min: derivar b e w, conferirSSE2/J4, transformar convenções e explicar o contraexemplo externo. Dúvidas e avaliação pessoal em branco. Pendentes regularização multivariada, espectro, incerteza, estabilidade numérica ampla e avaliação com dados reais. A aula e o percurso seguem em elaboração.
