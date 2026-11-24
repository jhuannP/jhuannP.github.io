# Informação em faixas e previsão condicional

27/10/2026. Notas originais com apoio de IA; revisão pessoal de Jhuann pendente. Extensão do exemplo triangular, percurso complementar, sem equivalência a disciplina formal.

## Modelo e resultados

f(x,y)=3x em 0≤y≤x≤1; zero fora. Variáveis adimensionais. Perda quadrática, distribuição conhecida; nenhum dado medido ou ajuste. Y|X=x é uniforme em [0,x] para x>0. m(x)=x/2, E[Y²|X=x]=x²/3, v(x)=x²/12. Pode-se escolher m(0)=v(0)=0 no ponto marginal nulo; não é divisão de eventos 0/0.

Expandir (Y−g(X))² em torno de m(X), com termo cruzado de média condicional zero, dá E[(Y−g(X))²]=E[v(X)]+E[(m(X)−g(X))²] para previsores de segundo momento finito. m é ótimo para essa perda; não para qualquer perda.

E[Y]=3/8, E[Y²]=1/5, Var(Y)=19/320. E[v(X)]=1/20, Var(m(X))=3/320; soma 19/320. Esses são riscos populacionais de previsores ideais, não métricas de um modelo treinado.

Z indica X≤1/2 ou X>1/2. Massas 1/8,7/8; momentos restritos de primeira ordem 3/128,45/128 e de segunda ordem 1/160,31/160. Previsões 3/16,45/112; variâncias 19/1280,3763/62720. A mistura dos erros dá 487/8960, entre 1/20 e 19/320. Perder o X exato custa 39/8960; observar as faixas reduz 9/1792 frente à constante.

Média simples das previsões =33/112, incorreta para recuperar E[Y]. A mistura ponderada dá 3/8. A variância do grupo alto supera a marginal em 39/62720: informação melhora o melhor risco médio, sem garantir melhora em toda faixa/realização. Refinar uma partição não aumenta o risco ótimo porque preserva os previsores antigos como candidatos.

## Fontes e limites

Magalhães e Lima, *Noções de Probabilidade e Estatística*, 7ª ed., §2.2 pp.54–55/PDF69–70: retomada da razão de eventos, trecho já conferido. Magalhães, *Probabilidade e Variáveis Aleatórias*, 2ª ed., §5.3 pp.260–265/PDF135–137 (páginas duplas): definição 5.7, Teorema 5.9, definição 5.8, consulta textual parcial em 27/10. Mapeamento da página impresso/PDF conferido na extração paginada, com colunas intercaladas; sem nova inspeção visual ou leitura integral. A decomposição de variância é proposta na seção; a dedução e a aplicação aqui são próprias. Nenhum enunciado/exercício do livro foi reproduzido; PDFs privados não distribuídos.

Figura original `informacao.svg`: barras de origem zero e escala comum para os três riscos; rótulos com frações/decimais e descrição textual. Sem afirmação causal ou profissional sobre a formação pessoal.

## Código e revisão

`prediction.py`: somente int/Fraction, sem bool/float. Integra momentos restritos E[Y^k 1{a<X≤b}]=3(b^(k+3)−a^(k+3))/((k+1)(k+3)), k inteiro de 0 a 20. Exige faixas de largura positiva e partições ordenadas completas. Retorna massas, médias, variâncias e riscos exatos deste modelo fixo; não estima densidades nem incorpora ruído. `affine_risk` avalia previsores a+bX, não aprende coeficientes.

Execute da raiz: `python3 -m unittest discover -s labs/previsao-condicional -t .`. Verificação executada e aprovada: momentos e decomposição; 81 previsores afins confrontados com quadratura de Gauss independente em y=xu; duas faixas e contraexemplo de variância local; refinamentos e esperança iterada; contratos. A quadratura é exata para os polinômios envolvidos, salvo arredondamento da implementação em float, sem garantia para integrandos gerais.

Respostas dos exercícios: 1/4;1/48;1/5;19/320;1/20;1/8;3/16;45/112;487/8960; pesos 1/8 e 7/8; não há melhora de toda variância local; modelo sintético conhecido. Resoluções completas na aula.

Revisão proposta em duas sessões de 20 minutos: derivar a média/variância; depois reconstruir as faixas e comparar os riscos. Dúvidas pessoais permanecem em branco. Pendentes: estimação com dados, perdas diferentes, sensores com ruído e revisão conceitual pessoal.

Conferência da entrega: cinco testes locais e 14 do catálogo aprovados; 739 fórmulas MathML conferidas. Navegador a 390 px: resposta incorreta/correta do exercício 9 verificadas pelo Enter, interpretação do exercício 11 aceita, figura legível e sem transbordamento horizontal; console sem erros. Revisão pessoal, leitor de tela e Windows real pendentes.
