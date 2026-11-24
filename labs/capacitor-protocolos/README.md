# Capacitor: carga fixa, tensão fixa e energia da fonte

22/10/2026. Aula f3-capacitor ampliada de3 seções/2 exercícios para14/12. Texto, valores, figura e código originais com apoio de IA; rascunho para revisão de Jhuann. Não é experimento pessoal nem especificação de componente.

## Hipóteses e unidades

Capacitor ideal linear, inicialmente vazio entre placas e ao final preenchido por dielétrico uniforme linear. C1=kappa*C0, kappa>=1; área e separação fixas, bordas desprezadas. Processo quase estático reversível, sem perdas, histerese, mudança final de energia cinética ou deformação mecânica relevante. O modelo não fornece posição intermediária, força ou duração.

C em microfarad(μF), V em volt, Q em microcoulomb(μC); U, energia da bateria e trabalho em microjoule(μJ). μF*V²=μJ. C0=2μF,V0=3V dão Q0=6μC,U0=9μJ. Variar kappa no painel compara estados finais de materiais ideais, não uma trajetória real de inserção de um material fixo.

Ucap=Q²/(2C)=CV²/2 é energia reversivelmente armazenada no capacitor linear, incluindo a resposta efetiva de polarização no caso dielétrico. Não é apenas a integral da densidade de energia do campo de vácuo dentro de material, sem considerar sua resposta.

## Dois protocolos a partir do mesmo estado

Carga fixa: fonte desconectada, sem fuga. Q1=Q0,V1=V0/kappa,U1=U0/kappa. Isso não proíbe trabalho mecânico; isolamento de carga não equivale a isolamento energético. A bateria não participa.

Tensão fixa: bateria ideal conectada mantém V1=V0. Q1=kappa*Q0 e U1=kappa*U0. Ela fornece carga adicional DeltaQ e energia elétrica V0*DeltaQ. A variação da energia da bateria é DeltaEbat=−V0*DeltaQ.

Defina Wext positivo como trabalho mecânico fornecido pelo agente externo ao conjunto. No processo ideal:
DeltaUcap+DeltaEbat=Wext.
O trabalho retirado pelo agente corresponde a Wext negativo.

Com carga fixa Wext=U0*(1/kappa−1).
Com tensão fixa DeltaUcap=(kappa−1)U0, DeltaEbat=−2(kappa−1)U0 e Wext=−(kappa−1)U0.
Portanto ambos permitem retirar trabalho para kappa>1 e carga inicial não nula. Usar só DeltaUcap em tensão fixa omite a fonte.

## Exemplo original e limites

C0=2μF,V0=3V,kappa=3; C1=6μF.
Carga fixa: Q1=6μC,V1=1V,U1=3μJ; DeltaUcap=−6μJ,DeltaEbat=0,Wext=−6μJ.
Tensão fixa: Q1=18μC,V1=3V,U1=27μJ; DeltaUcap=+18μJ,DeltaEbat=−36μJ,Wext=−18μJ.
No segundo caso a fonte perde36μJ, o capacitor ganha18μJ e o agente retira18μJ.

kappa=1 não altera o estado; V0=0 deixa carga/energia/trabalho nulos. Inverter a referência de tensão inverte Q,V sem mudar energias. Duas capacitâncias finais/iniciais não determinam força local: seria necessário C(posição) e um modelo mecânico consistente. Materiais deformáveis/nonlineares e perda resistiva não são calculados.

## Executar e testar

Na raiz do site:
    python3 -m labs.capacitor-protocolos.experiment
    python3 -m unittest discover -s labs/capacitor-protocolos -t .

protocol(C0,V0,kappa,mode), com mode charge/voltage, usa int/Fraction e rejeita bool/float,C0<=0,kappa<1 e modo desconhecido. Retorna estados e todos os termos do balanço. Cinco testes: exemplo;80 trios de parâmetros nos dois protocolos(160 estados); escalas de C e V; identidade/zero/polaridade; contratos. Referências36 trios racionais alimentam a comparação JavaScript dos72 estados de protocolo.

capacitor-protocol-models.js implementa o painel capacitorProtocols com parâmetros finitos e guarda de saídas numéricas finitas. Normaliza zero da energia da bateria para evitar−0 na interface. Duas tabelas separam estado final e balanço. CSS móvel restrito ao painel. Sem plugin, instalação ou dados privados.

## Fontes

Fonte primária oficial Feynman, Leighton e Sands, volumeII online:
https://www.feynmanlectures.caltech.edu/II_08.html
Consulta parcial em22/10/2026 a §8–2, energia do capacitor e trabalho da fonte em capacitância variável. A explicação da fonte alerta que omitir o trabalho elétrico em V fixo inverte incorretamente o sinal mecânico.
https://www.feynmanlectures.caltech.edu/II_10.html
Consulta parcial a §10–1 para capacitância e constante dielétrica; trechos adicionais de §10–5 delimitam a dificuldade de forças em dielétricos deformáveis. Exemplo e balanços acima são próprios; não copiamos figuras, exercícios ou casos numéricos.

Programa CCM0212 aberto em22/10/2026:
https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0212
Retorno com captura de dois meses antes. Ativação15/07/2025 compatível com aprovação2025/2, sem comprovar versão ministrada. Tentativa2024/2 e aprovação2025/2 permanecem as do panorama; histórico não reaberto. Eletrostática/energia e dielétricos constam do programa. Circuitos RC são apoios editoriais, sem criar novo item oficial.

Acervo anterior: Nussenzveig3 localizado em edição posterior à citada; Purcell/Jackson não identificados nominalmente. Não repetimos busca de acervo ou identificação editorial neste bloco. Nenhum PDF privado foi servido.

## Continuidade

Revisão pessoal: calcular os dois protocolos e explicar por que Ucap cresce em V fixo enquanto Wext é negativo. Depois: forças com geometria intermediária, meios não lineares e outras geometrias. FísicaIII mantém sete grupos parciais e duas lacunas;14 aulas/85 exercícios, seis recortes desenvolvidos/oito introduções. Nenhum domínio pessoal ou curso completo certificado.

Verificação do bloco: 894 testes Python aprovados; 511 estruturas MathML conferidas. Suíte JavaScript aprovada com 286 demonstrações/858 cenários básicos, mais 36 trios de referência racional comparados nos dois protocolos e contratos, incluindo normalização de zero. Após esclarecer os valores fixos dos exercícios, 12 testes de catálogo/correção repetidos e aprovados. Navegador: κ=1 com todos os incrementos/trabalhos zero; tensão negativa muda polaridade sem energia negativa; tensão nula zera os balanços; −36 aceito na questão10. Duas tabelas e esquema inspecionados a390px, sem transbordamento horizontal ou erros de console observados; viewport restaurado. Prévia capacitor-protocolos-mobile.jpg. Catálogo496 aulas/2846 exercícios,285 introduções com até três seções; todos rascunhos para revisão pessoal. Próxima revisão: fechar os dois balanços e explicar a fonte. Próximo preparo global: conferir lacunas e fontes de Biologia IV. Saldo semanal95%; parada operacional65%.
