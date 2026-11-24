# Eletrólise: carga, estequiometria e inventário

Laboratório original sem dependências. `python3 labs/eletrolise-carga/faraday.py` e `python3 -m unittest discover -s labs/eletrolise-carga -t .` a partir da raiz do protótipo.

Q=∑IΔt, n(e)=Q/F, n(produto)=ηQ/(zF), m=MηQ/(zF). Exemplo sintético: I=1A,1930s,z=2,M63,5g/mol,F96500C/mol de elétrons (valor didático arredondado),η0,80; produto0,008mol e0,508g. Todo cálculo racional é exato para esses dados, não para valores físicos sem incerteza. z é número de elétrons por unidade do produto conforme meia-reação. `required_charge` inverte a fórmula com η>0; não prevê tempo sem corrente assumida.

Correntes não negativas, sem inversão ou remoção de depósitos, até100 trechos,I≤1000A,Δt≤86400s,Q≤10^9C. Int/Fraction; z1..8,M0,1..1000g/mol,F1000..10^6C/mol,η0..1. available é inventário inicial em mol do íon para uma estequiometria1:1 no produto; excedê-lo causa rejeição, sem saturar e fingir η constante. Sem migração,difusão,cinética,condutividade,controle,tensão mínima ou previsão de produtos. Carga atribuída a outros processos não permite descobrir a reação lateral. SVG próprio com barra proporcional80/20; não é dado medido.

Fonte: OpenStax,Chemistry2e,§17.7,https://openstax.org/books/chemistry-2e/pages/17-7-electrolysis,consulta parcial29/10/2026: distinção galvânica/eletrolítica e trecho Quantitative Aspects of Electrolysis. F da fonte≈96485C/mol; foi explicitamente adotado96500 para contas didáticas. Não se copiaram os exemplos,exercícios ou figuras. Eficiência prescrita, inventário e cenários numéricos são extensões próprias de contabilidade, sem validação experimental. Levine6ª2009 permanece referência curricular/acervo anterior,sem nova leitura neste bloco.

Quatro testes: fixture/inventário,120 partições temporais/escalas,72 combinações de carga,z,η,M para balanço e inversão,contratos. Não certificam uma célula experimental nem domínio pessoal; rascunho para revisão.
