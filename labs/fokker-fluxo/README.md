# Fokker–Planck, corrente e um passo periódico

Modelo original de coeficientes constantes e um passo explícito. Não é solver geral de EDP, medição experimental ou validação da IC.

## Equação e fronteiras

Na convenção de Itô, a densidade regular satisfaz ∂tρ=−∂x(bρ)+∂xx(Dρ),D=σ²/2. A corrente é J=bρ−∂x(Dρ). Se D varia no espaço, não retirar D das derivadas. No intervalo[a,b], M′=J(a)−J(b).

Reflexão: corrente normal zero. Absorção: densidade interna nula na fronteira no modelo regular, podendo perder massa interior; acompanhar também os absorvidos. Periodicidade: extremidades identificadas, densidade e corrente compatíveis. Dividir uma subdensidade sobrevivente por sua massa produz lei condicionada, sem recuperar a informação sobre quem saiu.

## Solução analítica separada

Em[0,L) periódico, com c constante,D>0,k=2π/L e |a|≤1:

ρ(x,t)=[1+a exp(−Dk²t)cos(k(x−ct))]/L.

Integra1,é não negativa e satisfaz a equação por diferenciação. O exemplo uniforme1/L é estacionário com corrente c/L,que não precisa ser zero. `periodic_density` avalia a função específica em floats finitos; rejeita domínio inválido e avaliações não representáveis. D=0 é um limite de advecção admitido no código, sem suavização difusiva.

A gaussiana de OU do snippet anterior é outro exemplo, na reta. Início determinístico tem Dirac em t=0;densidade gaussiana regular exigeσ>0,t>0. Não usar sua curva com variância nula.

## Médias celulares e fluxos

O laboratório numérico usa intervalo periódico de comprimento1. São médias de densidade r_i em células com largura Δx=1/N. Probabilidade de célula é Δx r_i, não r_i sozinho.

Fluxo de interface: advecção upwind mais difusão centrada. Atualização explícita por diferença dos fluxos vizinhos. O cancelamento periódico conserva ΔxΣr_i exatamente com Fraction. Defina C=|c|Δt/Δx e R=DΔt/Δx². Os pesos são1−C−2R,C⁺+R,C⁻+R;C⁺/C⁻ são contribuições não negativas conforme o sentido da deriva. Se C+2R≤1, o passo é uma combinação convexa e preserva positividade. O código não impõe esse limite silenciosamente, não recorta negativos e não renormaliza.

Exemplo original: início(4,0,0,0),Δx1/4,c1/4,D1/32. Com Δt1/4,resultado(2,3/2,0,1/2). Com Δt1,resultado(−4,6,0,2). Ambos têm massa1,mas o segundo é densidade inválida. Inverter c espelha o sentido do transporte.

## Executar e verificar

Da raiz:

```sh
python3 labs/fokker-fluxo/flux.py
python3 -B -m unittest discover -s labs/fokker-fluxo -t .
```

Entradas racionais int/Fraction, sem float/bool nas médias, coeficientes e passos. Entre3 e256 células, médias iniciais não negativas,D≥0,Δt≥0,Δx>0. `weights` explicita a condição do passo; `step` devolve novas médias e fluxos, incluindo o contraexemplo negativo quando o limite é violado.

Cinco testes: vetores/pesos literais e inversão de deriva;360 impulsos periódicos sob combinações admissíveis, com referência convexa independente da diferença de fluxos;uniforme e corrente constante/balanço em três subdomínios;normalização/limites de nove ondas analíticas em64 pontos e resíduo da EDP em três pontos por diferenças centrais;contratos. A integração trapezoidal desses modos trigonométricos é apenas verificação numérica complementar à integral analítica.

Não demonstram convergência geral de malha, precisão de longo prazo ou estabilidade de outros esquemas. A advecção upwind é de primeira ordem espacial e o tempo é Euler explícito. O painel anterior ouDistribution foi preservado e não implementa esta nova geometria ou malha.

## Fonte — 29/10/2026

Pavliotis,Stochastic Processes and Applications,Springer2014,§4.1 pp88–91/PDF100–103: trechos textuais de equação,corrente,conservação,estacionariedade e fronteiras. P90/PDF102 visualmente conferida para Eqs4.11–4.12 e condições de fronteira. Offset desta parte confirmado, sem aplicar o deslocamento de capítulos anteriores. Leitura parcial, sem figuras/exercícios copiados ou PDF privado servido.

Chorin/Hald segue referência temática anterior, sem nova leitura pertinente. Exemplo periódico, método, contas, figura e exercícios próprios preparados com apoio de IA; revisão pessoal e aplicação científica/pedagógica pendentes.
