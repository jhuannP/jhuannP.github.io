# Adição iônica:contabilidade não seleciona mecanismo

Rascunho28/10/2026,assistido por IA,revisão pessoal pendente.Sem experimento real,condições de bancada ou predição de rendimento.

## Referências efetivamente consultadas

Brown/Poon,Introduction to Organic Chemistry,6ª edição,exemplar anteriormente identificado como2016 (diverge do2017online registrado no programa). Folha de rostoPDF3 reconferida textualmente;§5.3 pp.130–134/PDF150–154 consultadas em recortes por texto em28/10/2026:orientação de HX,passos e comparação qualitativa de carbocátions.Sem leitura integral,nova inspeção visual ou PDF servido.Propeno é caso clássico discutido no livro,não descoberta desta atividade.Marcação,contabilidade,código e diagrama próprios;sem transcrever exercícios/soluções.
[McMurry/OpenStax§7.8](https://openstax.org/books/organic-chemistry/pages/7-8-orientation-of-electrophilic-additions-markovnikovs-rule),consulta parcial28/10/2026.Não adotamos generalização de regiosspecificidade a todas as adições biológicas;sem porcentagens universais.
Programa CCM0224:item8,adição/eliminação,segundo registro anterior.Abertura direta USP em28/10 indisponível,não nova leitura;data/limite anterior preservados.

## Reconstruir os pares

C1H2=C2H–C3H3;Ha é o H do HCl.
Via secundária:π→Ha criaC1–Ha;H–Cl→Cl criaCl⁻ eC2⁺.Depois par deCl→C2 criaC2–Cl.
Alternativa formal:Ha vai aC2;C1⁺ é capturado porCl.Os dois desenhos passam no balanço,não têm probabilidade1/2 inferida.
Em C2⁺:três ligações,6elétrons em torno,CF+1.NoCl⁻:4pares,CF−1.Total26elétrons nos três estados,repartidos20+6,18+8,20+6 em ligantes/não ligantes.
Preferência qualitativa do caso iônico simples leva ao2-cloropropano;grafo não representa solvente,barreiras,geometria ou dinâmica.

## Executar

```sh
python3 labs/adicao-alceno/addition.py
python3 -m unittest discover -s labs/adicao-alceno -t .
```

Contrato restrito aos átomos marcados do caso.O auditor calcula soma de ordens,elétrons,carga formal e camada.Rejeita átomos desconhecidos,auto-ligações,ordens não inteiras/bool e camadas acima de8 (H2).Não verifica todos os estados químicos possíveis ou plausibilidade.Compartilhamento de átomos/elementos fixo;não é simulador químico universal.

## Balanço quantitativo separado

0,030mol de alceno +0,020mol deHCl,transformação1:1:teto0,020mol de produto e sobra0,010mol de alceno,se atingido.Sem conversão/seletividade/perdas medidas,não é rendimento.

## Revisão pessoal20min

Desenhe os pares,confira26 e os octetos/sexteto.Explique por que os dois produtos passam no balanço,mas isso não justifica mistura1:1.Separe intermediário,estado de transição e contribuinte de ressonância.

Pendentes:outras adições,rearranjos,estereoquímica,cinética,solvente e evidência experimental.Sem marcação de domínio ou estudo em nome deJhuann.
