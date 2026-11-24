# Ordens cinéticas e comparação controlada — rascunho

Nova aula `q2-ordens-cineticas`:14seções/12exercícios/4MathML,primeiro recorte de leis de velocidade. Não completa cinética,temperatura,mecanismos ou análise experimental.

## Fontes

Levine,Physical Chemistry6ªed./McGraw-Hill2009,acervo autorizado:consulta textual parcial p.518 sobre mecanismo/estequiometria e §16.3 pp.521–523 sobre integração,convenção k_A e meia-vida(PDF536,539–541). Extração incluiu pp.519–520,sem declarar leitura integral. Fatores estequiométricos explicitados;usa-se aqui v=−d[A]/dt em A→P1:1. [OpenStax Chemistry2e12.4](https://openstax.org/books/chemistry-2e/pages/12-4-integrated-rate-laws) consultado diretamente de forma parcial. Nenhum PDF,figura,dado ou exercício copiado.

Normalização,comparação,extensão por esgotamento,textos,exercícios e painel próprios. Fontes apresentam leis integradas;isso não atribui a elas os dados ou conclusões de um experimento pessoal.

## Modelo e limites

Mistura fechada1:1,A₀>0,P₀=0,volume/temperatura constantes,sem reversão. v=kₙ[A]ⁿ com n0/1/2. A₀ e v₀ comuns;kₙ=v₀/A₀ⁿ. Com a=[A]/A₀,u=v₀t/A₀,da/du=−aⁿ. Soluções:ordem0 atéu1,a=1−u;ordem1,e^(−u);ordem2,1/(1+u). Para ordem0,o painel acrescenta interrupção do consumo apósu1. A=max(1−u,0) é contínua,mas derivada inexistente na junção;taxa é None/null ali,não o valor de um dos lados por convenção escondida.

Meias-vidas emu:.5,ln2,1. A k fixo em cada modelo: A₀/(2k₀),ln2/k₁,1/(k₂A₀). Alterar A₀ a v₀ fixo modifica k₁/k₂;evitar atribuir essa comparação ao mesmo sistema físico com k fixo. Unidades dos k são diferentes.

Painel emu0..3,um controle. Gráfico com nó exato emu1 na curva contínua da ordem0. Tabela de frações de reagente/produto e taxas,sem mistura de unidades. Azul contínuo1,preto tracejado0,azul pontilhado2;texto fornece valores e hipóteses. Não simula mecanismo,ajuste,temperatura ou reação real.

## Verificar

`python3 -m unittest discover -s labs/cinetica-ordens -t .`

Quatro testes:61estados com frações exatas e Decimal70dígitos;tempo obtido independentemente por quadratura Simpson4096 de1/aⁿ;meias-vidas/escala,junção e estoque;contratos.13estados cruzados Python/JS.

Tese visual:uma comparação de concentrações com mesma escala,legenda por padrões e tabela que identifica a junção. Sem animação automática. Próxima revisão:derivar as três curvas e explicar o que está fixo. Próximo aprofundamento local:ajuste de dados sintéticos com incerteza,antes de interpretar ensaio real;alternar áreas antes de iniciar.
