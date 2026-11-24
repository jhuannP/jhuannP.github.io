# Joule–Thomson — balanço antes do sinal

29/10/2026. Rascunho assistido por IA; revisão pessoal pendente. Sem experimento,protocolo ou dados de gás real.

## Roteiro

1. Estrangulamento: escoamento estacionário,uma entrada/saída,composição fixa,adiabático,sem trabalho de eixo e mudanças desprezíveis de energia cinética/potencial. Conserve entalpia,h1=h2. Na expansão livre isolada e rígida de sistema fechado,conserveU. Não confundir com adiabática reversível/isentrópica.
2. Derive dH_m=Cp,m dT+[V_m−T(∂V_m/∂T)p]dp por Maxwell. Logoμ_JT=[T(∂V_m/∂T)p−V_m]/Cp,m. UnidadeK/Pa;pressão decrescente eμ>0 implicam resfriamento local. Gás idealμ=0. Um valor local não define toda queda finita.
3. Confira o exemplo local sintético:2×10⁻⁵K/Pa=2K/bar; queda1bar dáaproximadamente−2K se o coeficiente for suficientemente constante na faixa. Não é dado de material.

## Modelo reduzido consistente

Escalas T*,p* positivas;τ=T/T*,π=p/p*,v=V_m p*/(RT*),h=H_m/(RT*),σ=S_m/R. Prescreva v=τ/π+d,h=cτ+dπ,σ=c lnτ−lnπ+constante,c=Cp,m/R>1. Assim τdσ+v dπ=dh e u=h−πv=(c−1)τ. Volume/temperatura/pressão positivos. É modelo didático,não equação completa de gás real,vdW integral,transição ou inversão prevista.

Na isoentálpica,τ2=τ1+(d/c)(π1−π2);inclinação reduzida−d/c. Comc=3,τ1=1,π1=1/10,π2=1/20:

|d|τ2|Comportamento|
|---|---|---|
|−1|59/60|resfria|
|0|1|temperatura constante|
|+1|61/60|aquece|

São três modelos diferentes. Em cada linha,h é igual antes/depois. A queda não é isentrópica:Δσ=c ln(τ2/τ1)−ln(π2/π1)>0 nos exemplos. Na família,u depende apenas deτ;expansão livre comU fixo mantémτ,mesmo quando o estrangulamento mudaτ. Não generalizar para fluidos reais.

## Executar e verificar

```sh
python3 labs/joule-thomson/throttle.py
python3 -B -m unittest discover -s labs/joule-thomson -t .
```

Estado/temperatura de saída em Fraction,entropia por log em float. Entradasint/Fraction,c>1,τ,π,v>0 e quedaπ2<π1. Sem integração de aparelho ou troca de fase. Cinco testes:marcos;48 combinações por balanço independenteΔu=π1v1−π2v2;derivada de v/composição de quedas;contrasteU/H;contratos. Entropias positivas verificadas nesses casos,não teorema universal para toda escolha externa ao domínio.

## Fontes efetivamente consultadas

- Levine,Physical Chemistry6ª,copyright2009,§2.7: consulta textual parcial29/10/2026,pp.55–57/PDF73–75; p.57/PDF75 visualmente inspecionada paraH1=H2,definição e sinais. Nome do arquivo diz2008,mas ano editorial já confirmado2009. Não copiados gráficos,números experimentais,exercícios ou capítulo integral; PDF privado não servido.
- [PennState PNG520,Joule–Thomson Coefficient](https://courses.ems.psu.edu/png520/print/m19_p3.html),Eqs.19.21–19.24,consulta parcial29/10/2026:identidade em volume/entalpia e coeficiente ideal. A fonte usaη; nossaμ_JT. Não incorporamos suas generalizações sobre dutos/turboexpansores ou dados reais.
- [ProgramaCCM0124](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0124):consulta anterior28/10 mantida,item2;ativação2025 posterior à turma2024/1. Não reaberto neste bloco;versão ministrada não recuperada.

Modelo reduzido,estados,derivação de sua entropia,figura e exercícios próprios para estudo. Revisão pessoal e cálculos com propriedades reais continuam pendentes.
