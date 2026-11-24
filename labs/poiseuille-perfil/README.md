# Poiseuille: perfil e integral por anéis

Notas originais em rascunho;revisão pessoal pendente. Modelo de FísicaII,não experimento,CFD geral ou circulação biológica.

Nussenzveig,Curso de Física Básica2,5ªed.,Blucher2014,§2.7(a–b) pp.48–51/PDF49–52,consulta textual parcial29/10/2026; cabeçalhos finais conferidos. Sem nova inspeção visual,leitura integral ou distribuição do PDF privado. [OpenStax UP1§14.7](https://openstax.org/books/university-physics-volume-1/pages/14-7-viscosity-and-turbulence),consulta parcial a fundamentos,Poiseuille e Reynolds,sem reprodução de figuras,exercícios,tabela ou dados. Lei conhecida;derivação redigida,dados e código próprios.

## Hipóteses e conta

Tubo reto circular horizontal e rígido;fluido newtoniano incompressível,η constante,regime estacionário laminar totalmente desenvolvido e sem deslizamento. Δp=pentrada−psaída orienta Q. τ=Δp r/(2L) para queda positiva;integrar lei viscosa dá v=Δp(a²−r²)/(4ηL). Q=∫v2πrdr=πΔpa⁴/(8ηL),v_média=v_máx/2. Média radial sem anel seria2v_máx/3 e não calcula Q.

Dados próprios a1mm,L1m,η0,1Pa·s,Δp1000Pa,ρ1000kg/m³: máximo2,5mm/s,média1,25mm/s,Q1,25πμL/s,Re0,025,tensão na parede0,5Pa. Potência ΔpQ não negativa;Bernoulli sem perdas não fornece essa dissipação. Dobrar raio com pressão fixa dá Q×16,v_média×4,Re×8. Para Q fixo,Δp/16. Sem afirmar que o regime persiste para toda mudança de parâmetro.

## Executar

Na raiz:`python3 labs/poiseuille-perfil/pipe.py`;testes:`python3 -m unittest discover -s labs/poiseuille-perfil -t .`.

Inteiros/Fraction em SI;Q/π eP/π mantidos racionais,π só na apresentação. Validação da integral por Simpson é exata porque o integrando2rv é cúbico;isso não é validação experimental. Sinal invertido deΔp inverte v,Q e conserva potência positiva. Sem entrada,turbulência ou resolução de estabilidade.

Próxima revisão20min:derivar forças e integral;conferir unidades e condição imposta. Experimento,fluidos reais,regimes gerais e revisão pessoal pendentes.

O campo `peak` do código guarda a velocidade central orientada. Se Δp<0,ele é negativo; sua magnitude corresponde à rapidez máxima,sem confundir com o maior valor algébrico de v.
