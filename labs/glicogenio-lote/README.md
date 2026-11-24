# Glicogênio: produtos e balanço glicolítico

Notas,diagrama,lote e código originais assistidos por IA para revisão pessoal. Primeiro recorte do item16 de BiologiaI,não capítulo completo ou experiência experimental.

Glicogênio animal tem cadeias α(1→4) e ramos α(1→6). Fosforilase libera G1P por fosforólise nas pontas não redutoras;não usa ATP nessa reação. Para perto do ramo;desramificação combina transferência e hidrólise de uma ligação α1→6,liberando glicose livre. O modelo NÃO deduz proporções de produtos a partir de uma árvore ou do número de ramificações. O lote já liberado é fornecido como entrada e não representa degradação completa de uma partícula.

A mutase converte G1P em G6P sem gasto líquido de ATP. Para glicose livre,a hexocinase gasta1ATP. No destino escolhido,glicólise clássica até lactato:4ATP brutos por unidade de seis carbonos,gasto1na PFK para todas e1na hexocinase apenas para livres. Saldo3nP+2nF. Dois NADH produzidos por unidade são consumidos na formação de dois lactatos;netNADH0. Carbono6(nP+nF)=3×2(nP+nF). Não é balanço elementar completo de H,O,P,água ou carga.

Exemplo nP4,nF1:20ATP brutos,PFK5,hexocinase1,saldo14;10lactatos/carbono30. Todas as cinco como glicose livre dariam10ATP,sendo economia4. Não é rendimento energético global:exclui síntese prévia de glicogênio e UDP-glicose,transportes,manutenção e respiração. G1P/ATP etc são contagens estequiométricas abstratas,não fluxos medidos ou orientação clínica.

```
python3 -m unittest discover -s labs/glicogenio-lote -t .
python3 labs/glicogenio-lote/balance.py
```
Entrada de contagens inteiras0..1000000,sem bool ou float. Quatro testes:exemplo;441lotes/carbono/NADH/ATP;aditividade e casos-limite;contratos. Código confere o modelo escolhido,não regula vias ou comprova atividade enzimática.

## Fontes e alcance —28/10/2026

- Júpiter CCM0111 https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0111 : programa reaberto,ativação15/07/2024,captura indicada de três semanas antes;item16 metabolismo de glicogênio. Versão efetivamente ministrada em2024/2 não comprovada. Bibliografia lista Lehninger sem edição.
- Nelson/Cox,Princípios de Bioquímica de Lehninger,6ªedPT2014,exemplar privado autorizado:cap15 p.614/PDF644 e trecho p.615/PDF645 para produtos,desramificação e destinos; p.618/PDF648 e trechos p.619/PDF649 para UDP-glicose/síntese e ramificação. Consulta textual parcial,sem nova inspeção visual ou leitura integral. Figuras,tabelas e exercícios não reproduzidos,PDF não distribuído. Retomada dos balanços já desenvolvidos nas aulas de glicólise/piruvato para a dedução própria do lote. Não presume que esse exemplar seja a edição da turma.

Síntese não é tratada como reversão simples da fosforilase:usa UDP-glicose,sintase e enzima ramificadora;detalhes de iniciação e controle ficam pendentes. A distinção fígado/músculo é conceitual,sem conselho de saúde. Ação hormonal permanece lacuna;esta aula não encerra regulação.
