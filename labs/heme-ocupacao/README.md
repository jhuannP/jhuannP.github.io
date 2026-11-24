# Heme e ocupação de um sítio

Material original preparado com IA, revisão de Jhuann pendente. Primeiro recorte de bioinorgânica, sem certificar domínio ou pesquisa realizada. A química do heme é o contexto; o programa não calcula orbitais ou estrutura eletrônica.

## Hipóteses e unidades

H representa sítio de heme-proteína apto a ligar oxigênio, não heme livre. Estados exclusivos H,HO,HX; não há HOX. Kd,O e Kd,X condicionais, em concentração, para meio/temperatura fixos e aproximação diluída. x=[O2]livre/Kd,O, y=[X]livre/Kd,X são não negativos e sem unidade. Reservatórios ou depleção desprezível permitem prescrever ligantes livres. X é hipotético; não uma parametrização de CO/NO.

As populações são 1,x,y normalizados por 1+x+y. `from_pressure` requer p≥0 e P50>0 na mesma unidade e a hipótese [O2]=αp com α fixo. P50=Kd,O/α. Com y constante, P50 aparente=P50(1+y). Não substituir oxigênio total por livre sem balanço; a aula de complexação 1:1 já explora estoques finitos.

`drift` é um modelo cinético efetivo adicional, não consequência única de uma curva. ao/ax são associações pseudo-primeira ordem k_on[L], bo/bx dissociações, todas em unidade comum de tempo⁻¹. Escolher x=ao/bo e y=ax/bx anula os fluxos de equilíbrio. Escalar todas as taxas preserva esse equilíbrio e muda derivadas fora dele. Valores prescritos, não taxas medidas.

A mioglobina tem um sítio de oxigênio; a hemoglobina cooperativa não é descrita automaticamente por este modelo. Distal e proximal têm papéis diferentes. Oxidação, spin, enzimas, transporte de metais, ambiente e implicações fisiológicas não são resolvidos pela curva. Nenhuma recomendação clínica ou toxicológica é produzida.

## Roteiro

Da raiz:

    python3 -B labs/heme-ocupacao/binding.py
    python3 -B -m unittest discover -s labs/heme-ocupacao -t .

Confira x3,y2 → (1/6,1/2,1/3); sem X → (1/4,3/4,0). Explique por que a meia ocupação aparente é x3 com y2. Compare fluxos iniciais (-5,3,2) e (-50,30,20), de taxas com mesmas razões. A soma dos fluxos é zero; soma dos sítios conservada não significa população de cada estado constante fora do equilíbrio.

Cinco métodos de teste: 49 enumerações de pesos inteiros por rótulos; 81 conjuntos de taxas racionais com balanços independentes; marcos e12 conversões/semissaturações por pressão; monotonicidade, fluxos e conservação; contratos. Apenas biblioteca padrão. Entradas int/Fraction, sem bool/float. Figura sintética própria; não medições, ajuste estatístico ou identificação de uma proteína/ligante.

## Fonte consultada

Nelson e Cox, *Princípios de Bioquímica de Lehninger*,6ª edição brasileira2014 (original2013), §5.1, recortes textuais pp.158–160 e162/PDF188–190 e192, e parágrafo sobre curva/cooperação p.165/PDF195, em29/10/2026. P.160/PDF190 inspecionada visualmente para equações5-1–5-6. Apoio complementar ao programa CCM0214, sem substituir as referências oficiais. A busca no texto do Miessler disponível não localizou capítulo dedicado ao recorte; isso não comprova ausência de outras passagens.

Não foram reproduzidos capítulos, figuras, valores de afinidade ou exercícios da fonte. Balanço competitivo, exemplos, código e figura próprios. Documentos privados não são distribuídos pelo site.
