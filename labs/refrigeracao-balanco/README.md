# Refrigeração: duas leis e dois COPs

Modelo original de dois reservatórios ideais e dispositivo cíclico:TC<TH absolutos emkelvin,QC>0 retirado da fria,W≥0 recebido,QH=QC+W entregue àquente. Energias emJ por ciclo e entropia emJ/K. Sem fluido,pressões,ciclo completo,dinâmica,área de trocadores ou equipamento real. Exemplo prescrito,não medido.

`proposal` aceitaint/Fraction,rejeita bool/float e domínio incompatível com orientação. PermiteW0 para mostrar que energia fechada não garante segunda lei. COP_R=QC/W eCOP_H=QH/W retornamNone emW0. Geração S=QH/TH−QC/TC pode ser negativa:flagcompatible verificaS≥0,sem cortar valores. Compatível é condição necessária nesses balanços,não projeto fisicamente demonstrado. Não verifica automaticamente unidades semânticas:Celsius positivo digitado comoK não é detectado pelo tipo numérico.

Wmín=QC(TH−TC)/TC;COP_R≤TC/(TH−TC),COP_H≤TH/(TH−TC),W−Wmín=THS. Última identidade usa osmesmos QC/temperaturas/hipóteses e referência reversível. Energia não é destruída. Geração negativa éproposta incompatível,não entropia de um aparelho possível. EmTC280/TH320/QC840/W140:QH980,COP6/7,Wmín120,S1/16 e excesso20. W80 fecha energia comQH920 masS−1/8;W0 produzS−3/8 eCOP indefinido. W120 dáS0 eCOP7/8.

`rates` divide energias e geração pelo tempo positivo de um ciclo,não modela dinâmica. Em2s:QC420W,QH490W,W70W,S1/32W/K. COP não é capacidade frigorífica nem potência. Limite reversível não implica potência finita. ComTC280/TH360,mesmoQC840, Wmín240 eCOP_R3,5. Temperaturas de reservatórios mantidas,constantes;sem extensão automática a corpos finitos.

Da raiz:
```
python3 labs/refrigeracao-balanco/cycle.py
python3 -B -m unittest discover -s labs/refrigeracao-balanco -t .
```
Seis testes:fixture;81 balanços construídos independentemente por retirada de entropia fria e geração prescrita;propostas que fecham energia mas violam segunda lei;escalas e diferença de temperaturas;taxas médias e unidades;contratos. Snippet próprio conferido. Sem validação pedagógica ou domínio pessoal certificado.

Fontes parciais29/10/2026:Nussenzveig2,5ª2014,reimpressão2017,§10.3(b),pp253–254/PDF254–255,texto;p253/PDF254 visual parafluxos. Trecho deCarnot pp256–257 lido textualmente,sem nova inspeção visual. Questão10.3 foi localizada na busca masnãoadotada comoatividade ou fonte de valores;deduções e números próprios. PDF privado não distribuído. OpenStaxUP2§4.3 consultado parafinalidades e definições deCOP,sem copiar figuras/exemplos.
https://openstax.org/books/university-physics-volume-2/pages/4-3-refrigerators-and-heat-pumps
JúpiterCCM0122 reaberto29/10,ativação01/01/2025 posterior àturma2024/1,item6 segunda lei;versão ministrada não recuperada.
https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0122

Revisão pessoal pendente. Ciclos completos,fluidos reais,irreversibilidade local e aplicações próprias continuam pendentes. Sem dados de equipamento ou inferência de desempenho comercial.
