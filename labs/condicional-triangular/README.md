# Condicionamento com suporte triangular

27/10/2026. Notas de aula originais com apoio de IA, em rascunho. Revisão pessoal de Jhuann pendente. Percurso complementar, sem equivalência a disciplina formal ou prova de domínio.

## Modelo e derivação

Grandezas adimensionais X,Y com conjunta f(x,y)=3x em 0≤y≤x≤1 e zero fora. Normalização: ∫₀¹3x·x dx=1. O triângulo tem área1/2, mas a densidade não é uniforme. Não representa dados observados.

Marginais: fX(x)=3x² no intervalo unitário; fY(y)=(3/2)(1−y²) no intervalo unitário; zero fora. Cortes verticais têm comprimento x e horizontais comprimento 1−y.

Versão fY|X(y|x)=1/x em 0≤y≤x para 0<x≤1; zero fora. Versão fX|Y(x|y)=2x/(1−y²) em y≤x≤1 para 0≤y<1; zero fora. Integrais normalizadoras: x/x=1 e (1−y²)/(1−y²)=1. Usar 1/x no quadrado inteiro erra o suporte. Razões não especificadas pelo código em x=0 ou y=1; versões podem ser modificadas em conjuntos marginais nulos.

Exemplos originais: P(Y>1/4|X=1/2)=1/2; P(Y>3/4|X=1/2)=0; P(X>3/4|Y=1/2)=7/12. A primeira condicional é uniforme, a inversa é crescente. Alturas não são probabilidades.

Probabilidade total: cauda acima de1/2 é zero até x=1/2 e 1−1/(2x) depois. Integrar com peso3x² dá5/16. Integração da marginal de Y confirma. E[Y|X=x]=x/2; misturar com fX dá E[Y]=3/8, igualmente obtida por fY.

Dependência: A={Y>1/2}, B={X≤1/2} têm interseção de massa zero e produto5/128>0. Nenhuma interpretação causal é inferida.

Uma faixa positiva em torno de1/2 não é um ponto. Para 0<h≤1/4, P(Y>1/4 | 1/2−h≤X≤1/2+h)=1−(3/4)/(3/2+2h²), convergindo para1/2. Faixa degenerada não usa essa extensão: retorna None na razão por eventos.

## Referências e autoria

Magalhães e Lima, *Noções de Probabilidade e Estatística*,7ª ed., §2.2 pp.54–55/PDF69–70: fundamentos da razão e produto, localização já conferida. Magalhães, *Probabilidade e Variáveis Aleatórias*,2ª ed., §3.2 pp.128–130/PDF69–70 (páginas duplas): definição3.6, faixas, densidades condicionais e mistura, reconferência textual parcial em27/10/2026. A extração intercala colunas; não houve leitura integral ou nova inspeção visual. Modelo, números, redação, figura, código e questões próprios. Não se reproduzem exemplos ou exercícios das fontes. Livros privados não distribuídos.

## Código e verificação

Da raiz do protótipo: `python3 -m unittest discover -s labs/condicional-triangular -t .`.

`triangle.py` aceita int e Fraction, rejeita bool/float e intervalos fora de[0,1] ou invertidos. `rectangle` integra o suporte por cortes verticais, retornando massa zero para retângulos degenerados; `given_x` e `given_y` integram as versões declaradas; `band_x` usa razão de eventos e retorna None para condição nula. Fora do suporte condicionante, as funções condicionais rejeitam a entrada; marginais retornam zero fora.

Cinco testes:225 retângulos contra CDF deduzida na outra ordem; normalização, suportes e partições condicionais; probabilidade total e médias por Simpson racional exato para polinômios de grau≤3; limites de faixas e contraexemplo de independência; contratos e eventos nulos. Para a CDF, F(t,s)=(3/2)t²u−u³/2, u=min(t,s). A quadratura não é garantia para funções gerais nem verificação de dados reais.

Resoluções dos12 exercícios:3;3/4;9/8;2;1/2;0;7/12;5/16;3/8; falha de fatoração; suporte até x; razão não especificada no ponto nulo. As explicações completas estão na aula.

## Próxima revisão pessoal

Dois blocos de20min: desenhar cortes e normalizar; depois reconstruir as probabilidades e a média por duas rotas. Dúvidas e avaliação pessoal permanecem em branco. Pendente: ruído de observação, suportes mais gerais, modelos mistos/singulares e revisão conceitual por Jhuann. Não é material concluído ou experiência profissional comprovada.

Conferência de entrega: cinco testes locais e14 do catálogo aprovados;713 estruturas MathML verificadas. Em390px, exercício7 rejeitou0,5 e aceitou0,5833333333 pelo Enter; figura legível e documento sem transbordamento horizontal. Revisão pessoal, leitor de tela e Windows real pendentes.
