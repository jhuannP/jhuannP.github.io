# Wronskiano, dados iniciais e espaço de soluções

29/10/2026. Material original para revisão de Jhuann. Exemplo padrão de raiz dupla com parâmetros e dados locais; sem solver geral ou alegação de novidade matemática.

## Hipóteses

Em intervalo abertoJ, equação normalizada y''+p(t)y'+q(t)y=0, com p/q contínuas. O teorema de existência e unicidade torna a aplicação y→(y(t0),y'(t0)) um isomorfismo entre o espaço de soluções eR². Para duas soluções da mesma EDO, matrizPhi com linhas de funções e derivadas tem W=detPhi. W não nulo em um ponto equivale a base fundamental;W'=−pW e a fórmula de Abel impedem zeros isolados no intervalo regular. Fora dessas hipóteses, não usar esse teste como regra geral de funções.

Exemplo y''+4y'+4y=0: substituição y=e^(−2t)p reduz a p''=0. Base e^(−2t),t e^(−2t);Phi=e^(−2t)B, B=[[1,t],[-2,1−2t]],detB=1 eW=e^(−4t). Para y0=3,v0=−4,coeficientes(3,2) e y=e^(−2t)(3+2t). Em t1,y=5e⁻² e y'=−8e⁻².

**O código devolve B e o estado multiplicado por e^(2t), não Phi nem y real.** O fator exponencial é separado simbolicamente para preservar contas racionais. Não calcula exponenciais nem estabilidade de uma implementação em float. Derivadas de polinômios usam até oito coeficientes em ordem crescente,int/Fraction estritos. t adimensional neste modelo;uma aplicação física precisa de constantes com unidades apropriadas.

## Limite do teste em um ponto

f=t²,g=t³ são independentes como funções emR, masW=t⁴ se anula em0. Ambas satisfazem t²y''−4ty'+6y=0, cuja normalização falha em0. Em intervalos sem0,p=−4/t e q=6/t² são contínuas eW é não nulo. Em0,o par tem dados iniciais zero apesar de funções não nulas;não contradiz o teorema regular. Não foi alegado queW identicamente nulo implique dependência para funções arbitrárias.

Com forçante4,a particular y=1 dá conjunto1+kerL,afim:duas soluções da mesma forçante somam uma solução com forçante8, não4. Não é espaço vetorial quando forçante é não nula.

## Execução

`python3 -m labs.wronskiano-inicial.fundamental`

`python3 -B -m unittest discover -s labs/wronskiano-inicial -t .`

Cinco testes:49 pares de dados/quatro tempos;25 matrizes e identidade diferencial independente;25 pontos do par polinomial/EDO singular;operador para49 polinômios lineares e distinção afim;contratos. Provas acima não são substituídas pela grade finita.

## Referências consultadas

Apostol,CálculoII,traduçãoReverté1996/reimpressão2004 da2ªedição,§§6.4–6.5 pp165–167/PDF182–184,trechos textuais sobre operador,regularidade,existência/unicidade;§6.12 pp182–184/PDF199–201,trechos sobre matrizWronskiana eAbel,consulta parcial29/10/2026. p183/PDF200 inspecionada visualmente,confirmando sinal e limites do integral omitidos parcialmente noOCR. Deslocamento17 páginas neste recorte,não transferido ao livro todo. Não leitura integral. Uma busca mostrou exercício com outra equação; não adotado como atividade. Exemplo e dados desta aula próprios,sem cópia de figuras/exercícios ou distribuição privada.

JúpiterCCM0213 reaberto29/10/2026: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0213 . Ativação15/07/2024,itens6/7,compatível com2024/2 sem provar versão ministrada. Apostol é referência complementar do acervo,não um dos cinco títulos oficiais desse programa. Não confundir CCM0213/MatemáticaIII com CCM0223/MatemáticaIV ou nome didáticoCálculo3.

Próxima revisão20min:provar o isomorfismo pelos dados iniciais,calcularW e explicar a singularidade em0. Casos de ordem geral,condições de fronteira,coeficientes não contínuos e revisão pessoal pendentes.
