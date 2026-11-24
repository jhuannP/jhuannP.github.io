# Integração por partes

Rascunho original, 22/10/2026, revisão de Jhuann pendente. Aprofunda `c2-partes` de 3/2 para 14 seções/12 exercícios; preserva exemplo, IDs e desafio anteriores. É apoio editorial de integração, não novo item nominal de CCM0123 nem comprovação de domínio.

## Fonte

Apostol, *Calculus Volume I*, 2ª edição, Wiley1967, §5.9 pp.217–218 (PDF237–238): leitura parcial da derivação pela regra do produto, estratégia e forma definida. Extração incluiu página219, não usada como fundamento adicional. Nenhum capítulo completo declarado lido, página ou figura distribuída. Os exemplos de exponencial e logaritmo e exercícios foram desenvolvidos aqui; não são transcrição de problemas da referência.

## Modelo

I(b)=∫₀ᵇ x exp(x)dx=b exp(b)−(exp(b)−1). u=x,dv=exp(x)dx. Para b<0, f<0 no intervalo entre b e 0, mas a orientação 0→b torna I positivo. Para b=0, I=0; b=1 dá1, b=2 dá1+e². O código não é integrador geral nem garante precisão relativa para b arbitrariamente próximo de zero; contrato b em décimos no intervalo[-2,2]. A rotina usa expm1 no termo restante, calcula o resultado pela forma (b−1)exp(b)+1 e trata zero explicitamente; os termos da tabela são aproximações flutuantes da identidade exata.

Tese visual: curva única com região destacada; tabela separa fronteira, integral restante e resultado. Conteúdo: um controle, gráfico, tabela e orientação. Interação: teclado muda b, preenchimento e relatório respondem; limites zero e negativos recebem texto próprio. Escalas adaptadas são declaradas; preenchimento não codifica orientação e não permite comparar integrais por pixels.

## Verificação e lacunas

Quatro testes: série integrada independentemente com Decimal70 em41pontos, Simpson4096 orientado em7pontos, derivada da primitiva/casos exatos e contratos. Arquivo reference.json usa a mesma série integrada de80termos para41estados; cruzado com JavaScript. Apenas biblioteca padrão.

Execute `python3 -m unittest discover -s labs/integracao-partes -t .`, `node test_simulations.cjs` e `node test_math.cjs` na raiz.

Próxima ação pessoal: derivar a identidade e justificar I(−1)>0 sem olhar a solução. Pendentes: escolhas mais difíceis, impróprias e problemas integrados; este recorte não conclui integração ou Cálculo II.

Verificação final: 716 testes Python, JS269demos/807cenários básicos e comparações adicionais,417MathML e12testes de catálogo aprovados. b negativo/zero e exercício0,26424112conferidos no navegador.390px sem overflow e console sem erros observados; prévia `integracao-partes-mobile.jpg` na raiz. Viewport restaurado; revisão pessoal pendente. Saldo77%, parada65%.
