# Relaxação com entrada periódica

Material original preparado com IA para revisão pessoal. y′+ky=Bcos(ωt),y(0)=y0, t≥0, k>0. Se t em segundos e y em U, k em s⁻¹, ω em rad/s, B em U/s. y é sinal assinado; não se presume que uma variável física como concentração aceite valores negativos. Dados prescritos, sem medições.

A particular é a cos(ωt)+b sin(ωt), a=Bk/(k²+ω²),b=Bω/(k²+ω²). Somar (y0−a)e^(−kt) cumpre o PVI. Para B>0, amplitude B/√(k²+ω²) e atraso φ=atan2(ω,k), fase na forma cos(ωt−φ). Para B<0, o sinal adicional é π; phase da API é atraso em relação à entrada com seu próprio sinal. B=0 não tem fase observável, apesar do valor paramétrico retornado. A API não retorna atraso em segundos: φ/ω não se define em ω=0.

Caso original k2,ω3,B13,y0−1: a2,b3,C−3, y(0)=−1, y′(0)=15, amplitude√13. Envelope do transiente3e^(−2t),≤0,03 para t≥ln10. Amplitude periódica não é limite de y(t), que continua oscilando. Em ω=0 retorna o caso constante da aula. Ganho normalizado k/√(k²+ω²) decresce: este modelo estável de primeira ordem não tem pico ressonante em frequência positiva.

A solução é analítica em float. Aceita int/float sem bool/texto e finitos; k1e−3..1000, ω0..1000, |B|/|y0|≤1000 e t0..100. São limites computacionais, não regime universal da física. Não integra coeficientes variáveis ou entradas gerais. Reutiliza simpson de numerics.py e integrate de numerics4.py apenas nos testes, sem alterar motores. Não substitui aulas de convolução, Laplace ou o oscilador de segunda ordem existente.

Fonte primária: [MIT18.03SC, First Order Response to Sinusoidal Input](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/252a538daffe147f050d5e49424f4429_MIT18_03SCF11_s9_2text.pdf),2011, §3 pp2–3/PDF2–3, leitura textual parcial30/10/2026. A extração traz Ae^(2it) numa linha do caso geral; as substituições seguintes explicitam iω e a derivação local fixa e^(iωt). Nenhum exercício, exemplo numérico ou figura reproduzido. Consulta inicial FeynmanI23 tratava segunda ordem e não é fonte do recorte produzido.

Da raiz:

```sh
python3 -B -m unittest discover -s labs/relaxacao-harmonica -t .
python3 -B -m labs.relaxacao-harmonica.response
```

Cinco métodos: referência/preparação;54 PVIs e162 resíduos/derivadas centrais;32 integrais com fator integrante por Simpson;três soluções RK4 e ganho;snippets antigos/contratos. Quadratura e discretização são referências numéricas independentes, com tolerâncias, não prova por amostragem. Revisão pessoal e validação física pendentes.
