# Aldo-hexoses abertas e Fischer — rascunho

Primeiro recorte de carboidratos emBiologiaI/CCM0111:14seções/12exercícios,2MathML,Python e painel. Não cobre anéis,anômeros,dissacarídeos,polímeros,glicobiologia ou metabolismo.

## Fontes e autoria

Consulta parcial ao acervo autorizado em22/10/2026:Lehninger6PT/Artmed2014,§7.1,pp.244–246(PDF274–276),texto de famílias,projeções e centros; página246 visualmente conferida para orientação dos padrões. Partes cíclicas aparecem nessas páginas,mas não foram desenvolvidas nesta aula. Consulta pública parcial complementar:OpenStax Organic Chemistry [25.3](https://openstax.org/books/organic-chemistry/pages/25-3-d-l-sugars) e[25.4](https://openstax.org/books/organic-chemistry/pages/25-4-configurations-of-the-aldoses). DuasURLs inicialmente presumidas falharam;as corretas foram localizadas por busca e abertas diretamente. Não se declara leitura integral.

Glicose,manose e galactose são exemplos conceituais comuns. Enumeração,contrastes,exercícios,SVG e testes próprios;não se reproduzem figuras,tabelas ou soluções dos livros. PDF/imagem privada permanecem fora do site.

## Contrato do modelo

Forma aberta,mesma conectividade:C1=CHO no topo,C6=CH₂OH na base. C2–C5 são quatro centros independentes,sem forma meso neste esqueleto. Bit0=OH à esquerda,1=à direita na Fischer;horizontais para frente,verticais para trás. D-glicose referência(1,0,1,1). D-manose(0,0,1,1),D-galactose(1,0,0,1),L-glicose(0,1,0,0). O nome comum de outros padrões não foi cadastrado,sem afirmar ausência de identidade química.

Entre padrões correspondentes:0mudanças=identidade,1=epímeros/diastereoisômeros,4=enantiômeros,2/3=outros diastereoisômeros. Essa regra não classifica esqueletos ou conformações gerais. SérieD/L depende sóC5,não de todos os centros;oposição de série não basta para enantiomeria. D/L não determina(+)/(−),nem corresponde a atribuirR/S por lado doOH em cada centro.

O painel escolhe um padrão,sem simular reação,energia,rotação óptica ou geometria quantitativa. Faixas e tabela indicam centros alterados. Não fornece funções biológicas por contagem.

## Verificação e exploração

`python3 -m unittest discover -s labs/aldoses-fischer -t .`

Quatro testes:256pares comparados por sinais de volumes orientados de tetraedros com ligantes identificados(sem regrasCIP);enumeração16,espelhos,involução e contagens binomiais;nomes/exemplo de sérieL que não éL-glicose;contratos.16estados de referência Python/JS.

Tese visual:uma Fischer legível em azul,sem animação de conversão;controle por centro e tabela de referência. Sequência didática:orientação→configuração→comparação→limites. Próxima revisão pessoal:explicar por que inverter sóC5 não produz L-glicose. Próximo aprofundamento específico:formas cíclicas e anômeros,após nova consulta de fonte,sem antecipar cobertura.
