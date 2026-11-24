# Dielétricos em duas camadas — rascunho original

29/10/2026. Apoio de IA para revisão de Jhuann, não certificação de domínio, medição ou experiência de ensino.

## Pergunta e limites

Como condições locais de interface, tensão das placas e geometria determinam E,D,potencial,cargas e energia? Retomar Gauss, polarização e capacitor uniforme. Modelo eletrostático plano ideal,sem bordas,meios lineares isotrópicos de kappa positivo e geometria fixa. Campo exterior nulo; só cargas nas faces internas dos metais. Uma folha livre prescrita na interface pode ser não nula; ela não é uma terceira placa condutora. Não resolve forças,perdas,ruptura,anisotropia ou preparação física da folha.

## Unidades normalizadas

z,d em lref; E em Eref; phi,V em Eref*lref; D,P,sigma em epsilon0*Eref. Q em epsilon0*A*Eref; C em epsilon0*A/lref; U em epsilon0*A*lref*Eref². O código usa kappa,não epsilon dimensional. Inteiros e Fraction,sem floats ou bool; kappa e espessuras positivos. V e folha podem ter sinal. potential só aceita o intervalo fechado das placas. E na superfície ideal significa limite de cada lado,não valor único atribuído na descontinuidade.

## Reprodução

Da raiz do protótipo:

```sh
python3 -B -m labs.dieletricos-camadas.layers
python3 -B -m unittest discover -s labs/dieletricos-camadas -t .
```

São seis métodos de teste: exemplo exato;324 combinações comparadas a um oráculo de potencial nodal e balanços de carga;20 balanços de energia por cargas livres;36 divisões homogêneas e24 trocas de ordem;resposta afim/sinal;contratos. Casos internos não são métodos adicionais. Energia positiva é verificada neste modelo positivo,sem alegar validação de material real. Não há dependência nova nem alteração da simulação anterior.

## Resoluções e convenções

### Uma mesma letra pode esconder convenções diferentes

Nesta aula D_SI=ε₀E+P=ε₀κE e sua unidade é C/m². No exemplar consultado do Nussenzveig, §5.6, Eq.5.6.15, o autor chama de D_N a grandeza κE, com unidade V/m. Portanto D_SI=ε₀D_N: a divergência e o salto de D_N contam carga livre dividida por ε₀. Não misture a definição do livro com a lei de Gauss SI sem converter. Ao dividir D_SI por ε₀E_ref ou D_N por E_ref, os valores normalizados coincidem; isso não torna suas unidades físicas iguais.

### Fechar a geometria permite resolver o potencial

Considere placas paralelas planas com área A, bordas desprezadas. A camada 1 ocupa 0<z<d₁ e a 2 ocupa d₁<z<d₁+d₂; ε_i=ε₀κ_i>0, constante em cada uma. Fixe φ(0)=V e φ(d₁+d₂)=0, com normal +z. Então E_z=−dφ/dz e V=E₁d₁+E₂d₂. Pode haver uma folha infinitamente fina de carga livre prescrita σ_f na interface; não é uma terceira placa condutora nem uma camada dipolar. Impomos campo exterior nulo no modelo ideal, sem carga nas faces externas dos metais. As condições determinam as cargas induzidas nas faces internas.

### Sem folha livre, as camadas equivalem a capacitores em série

Com σ_f=0, Gauss fornece D₁=D₂=D. Logo V=D(d₁/ε₁+d₂/ε₂) e Q=AD. A capacitância é C=A/(d₁/ε₁+d₂/ε₂). Cada camada tem C_i=ε_iA/d_i e as quedas de tensão se somam, de modo que 1/C=1/C₁+1/C₂. A geometria é de camadas ao longo do campo, não duas regiões lado a lado em paralelo. Uma média aritmética de κ não preserva essa associação.

### Dois materiais: reconstruir quedas, campos e cargas

O novo laboratório usa z em ℓ_ref, E em E_ref, φ em E_refℓ_ref e D/P/σ em ε₀E_ref. Q usa ε₀AE_ref, C usa ε₀A/ℓ_ref e U usa ε₀Aℓ_refE_ref²; os números não são SI medidos. Tome κ₁=2, κ₂=5, d₁=1, d₂=2, V=9/5 e σ_f=0. A soma d₁/κ₁+d₂/κ₂=9/10 dá C=10/9 e D=Q=2 normalizados. Assim E₁=1 e E₂=2/5. As quedas são 1 e 4/5, somando 9/5; a interface está no potencial 4/5. A figura usa eixos separados, pois E e D têm escalas físicas distintas.

### A carga ligada fecha sua própria contabilidade

Nas duas camadas uniformes, ρ_b=0 no interior. Mesmo assim há três superfícies: inferior −P₁, interface P₁−P₂ e superior +P₂. Sua soma é zero por área, coerente com dipolos sem carga líquida adicionada. No exemplo, P₁=1 e P₂=8/5; as três contribuições são −1, −3/5 e 8/5. A interface tem carga total −3/5, igual a E₂−E₁ nas unidades escolhidas, embora σ_f=0. As cargas livres das placas são +2 e −2. Confundir carga livre, ligada e total destruiria esses dois balanços.

### Com folha livre, resolver duas condições em vez de impor D constante

Agora D₂=D₁+σ_f. Substitua em V=D₁d₁/ε₁+D₂d₂/ε₂ e isole D₁. Para S=d₁/ε₁+d₂/ε₂, resulta D₁=(V−σ_fd₂/ε₂)/S e D₂=D₁+σ_f. Depois obtenha E_i=D_i/ε_i e o potencial contínuo por integração em cada camada. Mesmo com V=0, uma folha não nula pode gerar campos opostos entre as placas; tensão líquida nula não obriga cada campo a ser nulo.

### A mesma tensão pode induzir cargas diferentes nas placas

Mantenha os dados e V=9/5, mas imponha σ_f=1. Agora D₁=14/9 e D₂=23/9; E₁=7/9, E₂=23/45 e φ_interface=46/45. As quedas 7/9 e 46/45 somam 9/5. As placas têm cargas livres normalizadas 14/9 e −23/9; somadas à folha +1, dão zero. P₁=7/9 e P₂=92/45, logo σ_b,interface=−19/15 e σ_total,interface=−4/15, exatamente E₂−E₁. Os dois terminais já não têm cargas opostas: parte da carga livre está dentro. Para σ_f fixo, dQ_inferior/dV=A/S, mas Q_inferior tem um termo de offset; não vale simplesmente Q_inferior=CV.

### Energia de campo inclui a folha interna

Para dielétricos lineares reversíveis de geometria fixa, U=(A/2)∑ε_iE_i²d_i. Integrar ∇·(φD)=−E·D+φρ_f entre placas e exterior nulo dá também U=(1/2)∑Q_livre φ sobre todas as superfícies livres. Sem folha, isso reduz a QV/2=9/5 no exemplo normalizado. Com σ_f=1, dá U=[(14/9)(9/5)+1×(46/45)]/2=86/45. Usar só Q_inferior V/2 daria 7/5 e perderia 23/45. Não contamos carga ligada de novo nessa soma: sua resposta já entra na constitutiva e na energia. A igualdade é um balanço de energia eletrostática, não uma descrição do trabalho de montar ou mover a folha.

### Verificar antes de generalizar

O laboratório resolve o mesmo problema por fluxos D e o confere usando outra incógnita: o potencial da interface. Verifica as cargas livres, ligadas e totais, a energia por campo e por cargas livres, o limite homogêneo e a troca de ordem das camadas sem folha. Trocar a ordem nesse caso preserva C e U, mas muda o potencial da interface. Fraction torna as contas racionais exatas; isso não valida a idealização física. Bordas, curvas, anisotropia, materiais não lineares, forças, perdas e experiência real permanecem fora do recorte. Revisar e explicar o exemplo pessoalmente ainda é uma etapa de Jhuann.

## Verificações independentes

O solver isola D1 a partir da soma das quedas de tensão. O teste resolve primeiro o nó phi=[sigma+k1*V/d1]/[k1/d1+k2/d2],deduz E1=(V−phi)/d1 e E2=phi/d2 e compara. Confere as cargas totais de cada superfície,incluindo placas,sem confundir seus sinais. Verifica derivadas do potencial dentro da primeira camada,continuidade e valores extremos. A energia pela integral de campo é comparada ao balanço de cargas livres ponderadas por potencial;sem folha,à associação em série e ao limite homogêneo. Não é uma solução numérica de geometrias gerais.

## Fontes e alcance efetivamente consultado

- Nussenzveig,Curso de Física Básica,vol.3,exemplar2ªed.revista/ampliada2015,reimpressão2017/digital2018. §§5.6–5.7,pp.93–96/PDF94–97,consulta textual parcial29/10/2026;p.93/PDF94 inspecionada visualmente para Eq.5.6.15. O autor define D_N=kappa E;site usa D_SI=epsilon0*D_N. Sua figura/exemplo de meia área não foi copiada: esta geometria são camadas ao longo do campo,com números próprios. Edição difere da1997 do programa,não presumir mesma paginação.
- [FeynmanII capítulo10](https://www.feynmanlectures.caltech.edu/II_10.html),§§10–1,10–3,10–4:corpo parcial de capacitor,polarização e Gauss. [Capítulo11](https://www.feynmanlectures.caltech.edu/II_11.html):somente introdução/§11–1. Sem leitura integral ou equivalência de paginação com tradução privada.
- [JúpiterCCM0212](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0212),reaberto29/10/2026,item4 e bibliografia,ativação15/07/2025. Compatível com semestre de aprovação,não comprova versão ministrada;tentativa2024 sem programa recuperado. Histórico permanece distinto do IF.

Textos,derivações do capacitor em camadas,números,figura,código e exercícios locais originais. Nenhum PDF privado servido ou copiado. Anisotropia,microscopia,geometria finita e revisão pessoal pendentes.
