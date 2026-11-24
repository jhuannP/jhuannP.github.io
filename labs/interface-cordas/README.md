# Interface entre cordas: deslocamento e energia

22/10/2026. Rascunho didático original para revisão de Jhuann. Não é medição ou experimento pessoal.

## Referências e recorte

- Nussenzveig, *Curso de Física Básica2*, quinta edição revista/ampliada, Blucher2014, exemplar privado identificado. Consulta parcial do corpo §5.6, pp.143–144/PDF144–145: extremidade livre e junção de cordas sob tensão comum, continuidade de deslocamento/força. Página144/PDF145 inspecionada visualmente. Extração incluiu141–142 e início de5.7; não se afirma leitura integral ou cobertura dos modos normais. Sem distribuição do PDF ou reprodução de figuras/exercícios.
- Richard Fitzpatrick/University of Texas, [Normal Reflection and Transmission at Interfaces](https://farside.ph.utexas.edu/teaching/315/Waves/node45.html), consulta direta parcial22/10/2026: deslocamentos, impedâncias, coeficientes e conservação. O recorte desta aula usa coeficientes de deslocamento com sinal, sem exigir amplitudes positivas com fases iguais. A condição de força é derivada diretamente, não inferida apenas da conservação quadrática.
- Michael Fowler/University of Virginia, [Impedance101](https://galileoandeinstein.phys.virginia.edu/Elec_Mag/2022_Lectures/EM_45_Impedance.html), blocos de cordas, impedância e condições na junção consultados diretamente e parcialmente. Não se usou a discussão eletromagnética posterior como modelo de corda.

Derivação aplicada, pulso, energias instantâneas, figuras e exercícios próprios. A unidade se liga a `f2-onda`, preservada: extremidades fixa/livre não são interfaces com transmissão. Vínculo ao grupo de ondas/interferência do mapa oficial de FísicaII; tópico permanece parcial.

## Hipóteses e unidades

Junção emx0, sem massa/perdas/força transversal externa; cordas semi-infinitas, flexíveis e lineares, tensão comum1N. μ₁1kg/m, c₁1m/s, Z₁1kg/s. q=Z₂/Z₁ positivo, controles0,5..2 em quartos; μ₂=q²kg/m, c₂=1/q m/s, Z₂=q kg/s. Não há onda incidente do lado direito.

F(s)=A(1−(s/w)²)³ em|s|<w, zero fora; A0,02m, w0,5s, t₀2s. F,F′,F″ contínuas. À esquerda: F(t−x/c₁−t₀)+rF(t+x/c₁−t₀); à direita: τF(t−x/c₂−t₀). Pulso temporal escolhido, não dados.

Continuidade:1+r=τ. Equilíbrio transversal:T yₓ esquerdo=T yₓ direito, portanto Z₁(1−r)=Z₂τ. Resultam r=(1−q)/(1+q), τ=2/(1+q). Mesma tensão é necessária para a igualdade de inclinações usada aqui; sem ela, compare forças, não apenas inclinações. Pequenas inclinações e ausência de massa são hipóteses, não consequências das figuras.

## Balanço e solução

u=μyₜ²/2+T yₓ²/2 e P=−T yₓyₜ. R=r² e T_E=qτ²; R+T_E=1. Para q0,5, τ4/3 mas T_E8/9: não usar τ² como fração de energia.

I=∫F′²ds=1024A²/(385w). E₀=Z₁I. A integral parcial normalizada C(t) usa z=(t−t₀)/w e H(z)=z³/3−4z⁵/5+6z⁷/7−4z⁹/9+z¹¹/11, H(1)=128/3465. No suporte C=[H(z)+128/3465]/[256/3465], com extremos0/1. Termos cruzados cinético/elástico cancelam à esquerda. E_esq/E₀=1−C+RC; E_dir/E₀=T_E C. Em t2s, C1/2 e potência instantânea zero, sem energia transferida nula. R/T_E são frações finais quando a separação acabou; tabela não confunde energia esquerda atual com reflexão final.

Domínio de figura x∈[−4,7]m contém todo suporte para controles t0..5s e q0,5..2. Gráfico y/A; tabela usa frações e relatório SI. Controle temporal escolhe uma fotografia analítica. O campo transmitido muda largura espacial com c₂; a duração temporal não muda. Não há integração temporal usada para desenhar.

## Verificações

```sh
python3 labs/interface-cordas/experiment.py
python3 -m unittest discover -s labs/interface-cordas -t .
```

Quatro testes: coeficientes racionais e casamento das condições em147tempos/cenários; energias nos dois semieixos por Simpson2048 em56cenários contra primitiva independente; equação de onda por diferenças finitas em28pontos/cenários; limites, contornos e contratos. A integral total do polinômio também conferida com Fraction.42referências cruzam JavaScript/Python para coeficientes, energia e valores dos dois lados da junção. Não se declarou verificação por integrador de diferenças finitas evoluindo o campo, nem validação experimental.

## Limites e continuidade

Sem absorção, dispersão, rigidez flexional, não linearidade ou massa na junção. Limites q→0⁺/∞ são comparações matemáticas com extremidades livre/fixa, fora dos controles; não se simulam cordas de densidade zero/infinita. Solução geral de dados iniciais, interfaces com massa e modos gerais continuam pendentes. Revisão pessoal e notas da turma não realizadas.
