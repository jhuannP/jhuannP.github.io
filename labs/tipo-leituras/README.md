# Tipo-valor Leituras — rascunho original

29/10/2026. Apoio de IA para revisão pessoal de Jhuann;não é aplicação pessoal concluída,medição real ou certificação de domínio.

## Reprodução e contrato

Da raiz do protótipo:

```sh
python3 -B -m labs.tipo-leituras.readings
python3 -B -m unittest discover -s labs/tipo-leituras -t .
```

Biblioteca padrão,Python com dataclass/slots e uniões de tipos (3.10+). Referência consultada3.14 não é declaração da versão local. Entrada é unidade exata m ou s e lista/tupla não vazia de int/Fraction,sem bool,float,texto ou contêiner aninhado. Unidade é etiqueta distinta,não análise dimensional/conversão. Ordem e repetições preservadas;negativos e zero são válidos. Estado interno tupla de racionais,cópia defensiva e campos frozen. Nenhuma fronteira de segurança prometida.

## Deduções e exemplos

### Um contrato dá significado ao valor antes da implementação

O vetor das três seções iniciais continua como primeiro exemplo. Vamos agora projetar Leituras, um conjunto ordenado não vazio de valores racionais com unidade m ou s. Os números são prescritos para estudo, não medições reais nem uma amostra estatística validada. O estado deve conservar ordem, repetições e unidade; valores negativos e zero são permitidos. Uma média é definida porque a coleção não pode estar vazia. Escolher esses requisitos torna explícito o que o tipo promete e o que precisa rejeitar.

### Anotar o tipo não valida a entrada em execução

A representação interna declara valores como tuple[Fraction,...], mas a anotação sozinha não impede receber True, uma lista ou texto. O construtor verifica a unidade, aceita lista/tupla não vazia e converte apenas int ou Fraction em Fraction, rejeitando bool e float. Essa política evita conversões silenciosas de texto, bool como inteiro e aproximação binária neste exemplo; não é uma regra universal para programas científicos. Valores e unidades exigem decisões de domínio, não apenas decorar a classe.

### Um snapshot corta o vínculo com a lista recebida

Se origem=[1,2,3] e a=Leituras("m",origem), o construtor cria uma tupla própria de racionais. Depois origem[0]=100 não altera a.valores. Copiar apenas uma referência manteria o mesmo objeto mutável compartilhado; frozen bloquearia reatribuir a.valores, mas não impediria origem de mudar seus elementos. Aqui a cópia defensiva tem propósito observável: preservar o valor que foi construído. Não há uma cópia profunda genérica; aceitamos somente elementos racionais imutáveis nesse contrato.

### Congelar uma referência não congela tudo a que ela aponta

Uma dataclass frozen com campo lista continua contendo uma lista mutável; um método append naquela lista altera seu conteúdo sem reatribuir o campo. Leituras combina campos congelados, uma tupla e elementos racionais. slots reduz atributos dinâmicos comuns, mas não é uma prova de imutabilidade ou uma barreira de segurança. A promessa é de estabilidade pelas operações normais da interface, não de resistência a alguém que force a alteração do objeto pelos mecanismos avançados da linguagem.

### Validar por inteiro antes de guardar o estado

No laboratório, dataclass usa frozen=True,slots=True,init=False. Escrevemos __init__ explícito para que a assinatura aceite lista ou tupla, enquanto o campo interno continue sendo tupla. Primeiro validamos e construímos snapshot local; só depois atribuímos unidade e valores via object.__setattr__ durante a inicialização. Não usamos esse caminho para editar uma instância já pronta. O Vetor2D antigo conserva seu __post_init__ chamado pelo construtor gerado; com init=False, esse gancho não é chamado automaticamente. São duas escolhas de construção, com responsabilidades diferentes.

### Uma atualização pode devolver um novo valor

b=a.com_acrescimo(6) constrói Leituras da mesma unidade com os elementos anteriores seguidos de 6. Não altera a, sua tupla ou os dados de entrada. Se a contém 1,2,3m, sua média continua 2m; b contém 1,2,3,6m e tem média 3m. Uma variável pode passar a apontar para b, mas isso não faz o objeto a mudar. O nome da operação informa que ela devolve o novo valor; ignorar esse retorno não atualiza a coleção antiga.

### Compor operações não requer herança artificial

Leituras contém uma tupla de Fraction e oferece media, desvios, com_acrescimo e juntar. A aritmética racional é responsabilidade de Fraction; o novo tipo cuida de sequência, unidade e invariantes. Não fazemos Leituras herdar de list para receber métodos mutantes que contradizem o contrato. juntar aceita outro Leituras desse contrato, exige a mesma unidade e preserva as duas ordens ao concatenar. Não soma elementos ponto a ponto nem converte metros em segundos. Herança e polimorfismo continuam como assuntos a justificar em outros domínios.

### Uma propriedade derivada pode evitar estado redundante

media é calculada por sum(valores)/n; desvios devolve a tupla x_i−media. Como os valores internos não mudam, cada consulta dá resultado coerente sem guardar também soma, média e contagem editáveis. A identidade ∑(x_i−media)=0 vem de ∑x_i−n media=0 e é um bom invariante de verificação. Em b, desvios=(−2,−1,0,3)m e somam zero. Isso testa o contrato aritmético, não calibração, incerteza ou qualidade dos dados.

### Média de médias exige os pesos corretos

Se a possui n leituras e b possui m na mesma unidade, a média de a.juntar(b) é (n media_a+m media_b)/(n+m). Para [0,2]m e [10]m, as médias são 1m e 10m, mas a média conjunta é 12/3=4m; a média simples das médias seria 5,5m. O objeto guarda os valores e consegue preservar o inventário completo. Descartar as contagens perderia a informação necessária para essa composição. Este exemplo não afirma que medições de precisões diferentes devam ter peso estatístico igual.

### Igualdade de valor não é identidade do objeto

Dois Leituras com mesma unidade e mesma sequência racional são iguais pelo valor, ainda que sejam instâncias distintas. Trocar m por s ou inverter a ordem muda a igualdade, mesmo se a média coincidir. Como a representação validada é hashable e a classe é frozen/eq, o hash gerado permite usá-la como chave de dicionário. Igualdade implica hash igual; hash igual sozinho não prova igualdade e seu número não é identificador persistente entre execuções. Não usamos unsafe_hash para tornar arbitrariamente segura uma estrutura mutável.

### Preservação também precisa valer quando a operação falha

Tentar juntar m com s gera ValueError, e tentar juntar com uma lista gera TypeError. Acrescentar True é inválido. Em todos esses casos, a instância original permanece intacta, pois os métodos criam outro valor após validar em vez de editar o antigo por etapas. O laboratório verifica esse comportamento junto com alterações da lista de origem, valores fracionários, igualdade, ordem e pesos. Evite capturar toda exceção e devolver média 0: isso apagaria a distinção entre entrada inválida e média realmente nula.

### O custo e os limites fazem parte da escolha

Construir ou acrescentar uma leitura copia a sequência: custo O(n) em referências/novas representações na construção e armazenamento O(n). Repetir acréscimos isolados até N itens pode acumular custo Θ(N²) de cópias; não é estrutura persistente com compartilhamento de nós ou algoritmo de streaming. Para ingestão grande, um construtor mutável controlado e um snapshot final podem ser melhores. O exemplo não implementa conversão de unidades, incertezas, serialização, concorrência ou desempenho de aplicação. Proteger invariantes não substitui revisão pessoal do código e de seu uso.

## Verificações independentes

Seis métodos aprovados:snapshot após mutação/append da origem e atualização com novo valor;120 sequências exaustivas de tamanho1…4,valores−1/0/2,comparadas a statistics.mean,desvios e invariantes de inversão/translação;16 composições de tamanhos e exemplo que distingue média conjunta de média das médias;igualdade/ordem/unidade/hash/dicionário;atribuição comum bloqueada e falhas sem alterar a origem;contratos e frações. Casos internos não são métodos adicionais. O objetoéq usa campos,mas não se testa colisão de hash como igualdade ou hash como identificador persistente.

O primeiro rascunho de laboratório usava construtor gerado com anotação tuple e aceitava lista em post-init. Antes da integração,foi ajustado para init=False e assinatura explícita que aceita lista/tupla,guardando tuple;isso evita confundir a anotação da representação com o tipo de entrada. Os seis métodos passaram após a mudança. Exemplo Vetor2D anterior e seu post-init preservados,no código da aula;snippet/desafio antigos conferidos e executados separadamente,Python local3.14.5. Não é biblioteca de unidades,estatística inferencial,serialização ou benchmark.

## Fontes efetivamente consultadas

- Sedgewick/Wayne,Computer Science,exemplar copyright2017,§3.3 pp.439–441/PDF460–462,consulta textual parcial29/10/2026 de imutabilidade,aliasing,custo e cópia defensiva;correspondência de cabeçalhos individuais conferida. Sem nova inspeção visual/capítulo integral ou cópia de exemplo,figura ouPDF. Livro emJava;Leituras é exemplo próprio emPython. Programa cita2016;copyright do exemplar não é data de impressão.
- [Python3.14 dataclasses](https://docs.python.org/3.14/library/dataclasses.html),recortes init/eq/frozen/slots/hash e Post-init/Frozen instances,consulta parcial29/10/2026. Anotações não validam por si,init=False não chama post-init automaticamente e frozen não é imutabilidade profunda. Não instalamos dependências nem reproduzimos o exemploInventoryItem da fonte.
- [JúpiterCCM0118](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0118),reaberto29/10/2026,ativação15/07/2024 posterior à aprovação2023/2;versão ministrada não recuperada. Classes/projeto de tipos não são item isolado no programa listado;apoio editorial deSedgewick,ligado a bibliotecas/clientes e prática,não prova de linguagem/sequência cursada.

Materiais e figura originais,sem PDF/caminho privado servido. Custos contam cópia de sequências,não todas as operações de bits da aritmética racional. Revisão pessoal,uso real e percursos amplos continuam pendentes.
