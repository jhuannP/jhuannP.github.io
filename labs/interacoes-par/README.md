# Interações e potencial de par

Material original, rascunho para revisão de Jhuann. Distinguimos interações entre entidades e ligações internas;dispersão também existe em espécies sem dipolo permanente. Recorte qualitativo de polaridade,doadores/aceptores e propriedades não é cálculo completo de ponto de ebulição ou estrutura cristalina.

Fontes primárias: OpenStax Chemistry2e§10.1, consulta textual parcial29/10/2026 de dispersão,polarizabilidade,dipolo e ligação de hidrogênio, https://openstax.org/books/chemistry-2e/pages/10-1-intermolecular-forces . NIST, Lennard-Jones Fluid Reference Calculations:Cuboid Cell,§3A, consulta parcial à definição do potencial tradicional12-6 e contexto de variantes com corte29/10/2026, https://www.nist.gov/mml/csd/chemical-informatics-group/lennard-jones-fluid-reference-calculations-cuboid-cell . Não usamos configurações,tabelas de resultados,figuras ou exercícios dessas fontes;sem downloads dos dados NIST. Provas,código,figura e exercícios próprios.

Modelo isolado U(r)=4ε[(σ/r)^12−(σ/r)^6],ε>0,σ>0,r>0 e U(infinito)=0. ε é energia POR PAR,σ é comprimento;um parâmetro molar não entra como energia de par sem conversão. Não representa dipolos orientados,ligação de hidrogênio,histerese química ou todas as forças reais. Expoente12 é forma de repulsão do modelo,não derivação microscópica universal.

q=(σ/r)^6;U/ε=4(q−1/2)²−1 e rF_r/ε=24q(2q−1),com F_r=−dU/dr positivo no sentido de aumentar separação. q1 dá energia0 mas força repulsiva; q1/2 dá mínimo−ε em r=2^(1/6)σ; q1/4 dá−3ε/4 e rF/ε=−3. U negativa não significa força sempre atrativa. Contribuição atrativa pode coexistir com repulsão maior em distâncias curtas. Não deduzir temperatura de fusão,estrutura sólida ou fase de um poço de dois corpos.

Código padrão,int/Fraction e limites didáticos:1/4096<=q<=64,.5<=x=r/σ<=4. reduced retorna U/ε e rF/ε,at_distance retorna U/ε e Fσ/ε;valores não são forças em newtons sem escalas. Rejeita bool/float;raízes irracionais aparecem só como fórmula analítica/figura aproximada. Não inclui dinâmica,cutoff,condições periódicas,correção de cauda ou MonteCarlo. Não foi validado contra dados NIST ou experimento real.

Execute da raiz: `python3 -m unittest discover -s labs/interacoes-par -t .`; `python3 labs/interacoes-par/pair.py`. Quatro testes:valores analíticos;128 pontos com quadrado completo/sinal de força e expressão independente em distância;derivada central da energia em cinco distâncias com refinamento do passo;contratos. Malha não prova mínimo global;quadrado completo sim. Revisão pessoal pendente.
