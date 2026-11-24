# Fonte e carga: modelo equivalente CC

Notas de aula originais em rascunho. Percurso próprio escolar, sem equivalência curricular integral ou uso com aluno comprovados.

## Fontes

Nussenzveig,Curso de Física Básica3,Eletromagnetismo,2ªed.,Blucher2015,§6.8 p.123/PDF124. Consulta textual parcial29/10/2026 ao exemplar privado autorizado; cabeçalho conferido. Edição/ano confirmados na ficha textual. Apoio para fonte equivalente, corrente e tensão terminal; sem nova inspeção visual ou leitura integral, PDF não servido.

[OpenStax CollegePhysics2e§21.2](https://openstax.org/books/college-physics-2e/pages/21-2-electromotive-force-terminal-voltage),consulta pública parcial29/10/2026 aos trechos de fem/resistência interna/tensão terminal. Não foram copiados exemplos, exercícios ou figuras. Contas, derivação algébrica do máximo, diagrama e código próprios.

## Modelo e limites

Fem ε>0 fixa, resistência interna r≥0 e carga R≥0 constantes, r+R>0, regime estacionário, fios ideais. I=ε/(R+r),V=IR=ε−Ir. Fonte ideal entrega εI; carga recebe I²R; dissipação interna I²r. Eficiência elétrica R/(R+r) não é eficiência química total.

Para r>0,Pmáx=ε²/(4r),pois diferença=ε²(R−r)²/[4r(R+r)²]. Máximo em R=r com eficiência50%; cargas maiores podem ter eficiência maior e potência menor. Em circuito aberto I=0,V=ε,potências0 e eficiência indefinida. r=0,R>0 tem eficiência1,sem o mesmo máximo finito. r=R=0 é singular e rejeitado. R=0,r>0 é limite matemático,sem proposta de montagem.

Dados sintéticos ε12V,r2Ω,R6Ω: I1,5A,V9V,Pcarga13,5W,Pinterna4,5W,Pfonte18W,η75%. R2Ω entrega18W,masη50%. Dois pontos artificiais(1A,10V)/(2A,8V) recuperam ε12V,r2Ω sob hipótese de reta. Sem inferência experimental validada.

## Executar e revisar

Na raiz: `python3 labs/fonte-carga/source.py`; testes: `python3 -m unittest discover -s labs/fonte-carga -t .`.

Fraction,inteiros/racionais em SI; carga None é circuito aberto. Testes de balanço,identidade do máximo,escala,fronteiras e contratos não validam bateria real ou regime de descarga. Reproduzir o exemplo e provar a cota em20min. Incerteza,modelos não lineares,transitórios,revisão pessoal e uso com aluno continuam pendentes.
