# β-oxidação: inventário de cadeia saturada par

Modelo didático de uma cadeia não ramificada, saturada e com n carbonos pares. Assume-se β-oxidação mitocondrial completa e depois oxidação completa do acetil-CoA no ciclo cítrico; não se modelam transporte, cinética, regulação, compartimentos ou organismo. Intervalo4≤n≤40 é limite do programa; não afirma que toda cadeia nesse intervalo tenha o mesmo destino fisiológico.

A rotina encurta a cadeia passo a passo. Cada volta fornece um NADH e um par de elétrons via FAD ligado/ETF para Q; não uma reserva de FADH2 livre nem entrada pelo complexoII. A última cadeia C4 sofre uma volta e gera dois acetil-CoA. Assim ciclos=n/2−1,acetil=n/2; em toda linha2×acetil_emitido+carbonos_restantes=n.

Exemplo próprio C14:seis voltas,sete acetil-CoA,seis NADH e seis paresETF na β-oxidação. Após três voltas:três acetil-CoA e cadeia C8. Não há liberação de CO2 pela sequência básica da β-oxidação; os carbonos ainda estão em acetil-CoA/cadeia residual.

Estimativa separada: por acetil,3NADH,1par paraQ e1GTP; suponha2,5 equivalentesATP/NADH e1,5/parQ,GTP equivalente a1ATP. Para C14:27NADH,13paresQ e7GTP dão94 equivalentesATP brutos. Partindo do ácido livre,ativação ATP→AMP+PPi custa dois equivalentesATP:saldo92. Partindo do acil-CoA já ativado,o custo fica fora da fronteira:saldo94. Não são dois ATP consumidos como moléculas nessa etapa. A fórmula7n−6 só vale com essas hipóteses; não prevê rendimento celular medido. Frações exatas conferem contabilidade,não tornam razõesP/O exatas na natureza.

```sh
python3 labs/beta-oxidacao-par/inventory.py
python3 -m unittest discover -s labs/beta-oxidacao-par -t .
```

Quatro testes:fixtureC14;19 cadeias pares contra fórmulas fechadas e invariante de carbono por etapa;mudança de rendimentos/fronteira;contratos. Zero nos rendimentos é cenário matemático de sensibilidade,não simulação de desacoplamento em célula. Sem dependências,dados experimentais ou recomendação clínica/alimentar.

Fonte:Nelson e Cox,Princípios de Bioquímica de Lehninger,6ªed.tradução2014,§17.1 pp.670–671/PDF700–701 e§17.2 pp.674–676/PDF704–706,consulta textual parcial29/10/2026:ativação,etapas,ETF e hipóteses de rendimento. Cabeçalhos e deslocamento de30 páginas conferidos no texto extraído;sem nova inspeção visual/leitura integral. Não copiados exemplos,tabela,figura ou exercícios;C14,redação,desenho,código e exercícios próprios. Exemplar privado não distribuído. Síntese de lipídios,insaturados,ímpares,peroxissomos,regulação e integração permanecem pendentes;revisão pessoal também.
