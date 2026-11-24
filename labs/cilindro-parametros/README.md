# A mesma lateral, parâmetros diferentes

Extensão original de28/10/2026,assistida por IA,para revisão de Jhuann. Não comprova domínio pessoal ou experimento.

## Fontes e escopo

[USP CCM0223 — Matemática IV](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0223),reaberto28/10/2026,ativação01/01/2025,captura da última semana:integrais de superfície no item3;versão ministrada não comprovada. No site o percurso tem nome didático Cálculo3.
Apostol,CálculoII,tradução portuguesa1996/reimpressão2004,§12.1 pp.467–470/PDF480–483,§12.2 p.471/PDF484 e§12.8 pp.484–486/PDF497–499:consulta textual parcial28/10,sem nova inspeção visual/leitura integral.Paginação não transplantada da edição inglesa.PDF privado não servido.
[OpenStax CalculusVolume3 §6.6](https://openstax.org/books/calculus-volume-3/pages/6-6-surface-integrals):consulta parcial às partes de parametrização e orientação.Exemplos,código,figura e contas são próprios.

## Derivar antes de executar

q=s∘ψ; ψ(u,v)=(θ(u,v),z(u,v)). Pela cadeia,q_u=s_θθ_u+s_z z_u e q_v=s_θθ_v+s_z z_v.Expandindo o produto e usando a antissimetria,sobra(det Dψ)(s_θ×s_z).Para integral escalar,o módulo do determinante é absorvido pela mudança de variáveis.Para fluxo,o sinal define se a orientação induzida coincide com a normal geométrica pretendida.Hipóteses:C¹,bijeção regular entre domínios apropriados,determinante não nulo,integrandos integráveis.Esta discussão não substitui a teoria global de atlas.

Na lateral s(θ,z)=(Rcosθ,Rsenθ,z),o produto é(Rcosθ,Rsenθ,0),normaR;R,H em metros.Área2πRH.CampoF=κ(x,y,0),κ em s⁻¹:fluxo externo2πκR²H.
No quadrado:θ=sign·2πk u+βv,z=Hv.O produto tem módulo2πkRH e sinal radial sign;β apenas inclina linhas de parâmetros.Uma volta cobre uma vez salvo a costura,mais voltas contam multiplicidade.

R2m,H3m,κ1s⁻¹:

|Representação|Integral de área no domínio|Fluxo induzido|
|---|---:|---:|
|k1,sign+1|12πm²|24πm³/s|
|k1,sign−1|12πm²|−24πm³/s|
|k2,sign+1|24πm²|48πm³/s|

A área geométrica continua12πm²,não muda por dupla cobertura.A lateral não inclui tampas;Gauss requer fechamento.No campo escolhido,fluxo das tampas é zero pois F_z=0.

## Laboratório

```sh
python3 labs/cilindro-parametros/charts.py
python3 -m unittest discover -s labs/cilindro-parametros -t .
```

Derivadas analíticas,produto vetorial e quadratura de ponto médio em malha do quadrado.O integrando de área/fluxo deste exemplo é constante;quadratura não testa convergência de uma função geral.Limites operacionais:R,H de10⁻⁶ a10⁴;|β|≤100;1–8voltas;|κ|≤10⁴;malha1–128.São limites didáticos de cálculo,sem validação física.O produto vetorial é verificado também por diferenças finitas nos testes;isso é evidência numérica,sem substituir a prova.

## Revisão pessoal20min

Reproduzir a expansão do produto,o determinante comβ5,eos valores12π/24π/48π.Declarar a normal em cada caso.Explicar por que uma cobertura dupla não é uma reparametrização bijetiva.

Pendentes:atlas,não orientabilidade,campos/densidades gerais,estimativas de quadratura e revisão pessoal.Não marca o tópico inteiro como completo.

Para β≠0,o domínio (θ,z) é um paralelogramo, não o retângulo fixo original. A comparação usa cálculo direto e periodicidade; não afirma que ψ é bijetiva sobre aquele retângulo.
