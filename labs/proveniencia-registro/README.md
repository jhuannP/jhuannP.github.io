# Proveniência: rastrear, repetir e avaliar

Pacote sintético original, produzido com apoio de IA; revisão pessoal pendente. Não contém histórico escolar, dados da IC, arquivos de cliente ou material privado. Não implementa um padrão PROV ou um sistema de autenticação.

## O exemplo

EDO y′=−κy, κ em s⁻¹, duração T em s e y na unidade arbitrária U. Euler explícito usa h=T/N e yₙ₊₁=(1−κh)yₙ. Configuração completa: taxa, duração, valor inicial e passos. O laboratório usa strings racionais para as três grandezas e inteiro para N. O exemplo da aula anterior, com três parâmetros e valor inicial implícito, foi preservado.

Com κ=T=y₀=1 e N=4, o resultado é 81/256 U. Em Decimal com precisão 60, a referência e⁻¹ difere por cerca de 0,0514732 U em módulo. A repetição exata do método não elimina esse erro de discretização, nem justifica automaticamente a equação para dados reais.

## Arquivos do pacote

- `config.json`: bytes originais dos parâmetros sintéticos.
- `model.py`: função local de Euler, com validação.
- `record.py`: geração, consistência, reexecução e gravação.
- `result.json`: numerador/denominador do ponto final e unidade.
- `manifest.json`: método, modelo, unidades, ambiente, origem sintética, ausência de sorteio, revisão pendente e tamanho/SHA-256 dos outros quatro arquivos.

O manifesto não calcula um hash de si próprio. Registra a versão/implementação do Python e sistema operacional, sem nome de usuário, caminho absoluto ou identificador da máquina. Não arquiva todo o interpretador, dependências do sistema ou histórico Git.

O exemplo em `exemplo/` foi gerado localmente por este script. Os dois scripts copiados nesse pacote são os bytes usados na geração. A revisão humana continua pendente; metadados não são prova de aprovação pessoal.

## Verificações diferentes

`verify` compara tamanhos e hashes com o manifesto fornecido. Ele permite detectar diferenças em relação ao registro; um manifesto sem assinatura também pode ser reescrito junto com os arquivos. Não autentica o autor nem valida ciência.

`replay` exige os códigos esperados da implementação local conhecida e recalcula seu modelo. Não importa ou executa o `model.py` trazido no pacote. Se a fonte difere da referência local, não afirma reproduzir uma implementação histórica. Concordância da reexecução e comparação com uma solução analítica são camadas separadas.

Casos controlados dos testes: acrescentar um espaço à configuração preserva os parâmetros decodificados, mas muda sua identidade em bytes; trocar a saída por 1 U e atualizar o manifesto passa na consistência, mas falha na repetição; alterar o código registrado e reescrever seu hash não provoca execução desse texto pelo verificador.

## Serialização e limites

Registros gerados usam UTF-8, chaves ordenadas, separadores definidos, `allow_nan=False` e uma quebra de linha final. É uma convenção do esquema restrito, sem alegar canonicalização JSON universal. Na entrada, `parse_constant` rejeita NaN/Infinity e `object_pairs_hook` detecta chaves repetidas. A configuração exige quatro campos, sem bool como inteiro, N entre 1 e 128, frações não negativas com componentes até 10000 e κh≤1. Duração é positiva. Esses limites são escolhas didáticas, não um formato geral de dados científicos.

Um arquivo semanticamente igual pode ter bytes diferentes por espaços ou finais de linha. Ambientes diferentes também podem gerar manifestos diferentes, mesmo com o mesmo resultado racional. Não houve teste em Windows físico nem recriação de ambiente. O cálculo não usa aleatoriedade e não inventa uma semente; experimentos aleatórios precisam de descrição adicional pertinente.

## Executar

Da raiz do protótipo, para imprimir um manifesto sem gravar arquivos:

```sh
python3 labs/proveniencia-registro/record.py
```

Para criar um pacote, escolha uma pasta que ainda não exista:

```sh
python3 labs/proveniencia-registro/record.py --output pasta-nova-de-exemplo
```

A pasta existente é recusada, sem sobrescrever arquivos. A gravação não é uma transação atômica: uma falha de I/O pode deixar uma pasta parcial. O script não remove arquivos do usuário.

```sh
python3 -B -m unittest discover -s labs/proveniencia-registro -t .
```

Seis métodos verificam resultado racional, referência independente de maior precisão e ambiente; bytes versus significado; resultado errado com manifesto recalculado; código registrado tratado como dados; gravação/leitura e recusa de sobrescrita; parsing e domínio. O teste de erro analítico avalia este exemplo, não certifica o modelo para uma pesquisa.

## Fontes — 29/10/2026

[Python3.14 json](https://docs.python.org/3.14/library/json.html): recortes de dumps/loads, serialização, NaN/Infinity e chaves repetidas. [Python3.14 hashlib](https://docs.python.org/3.14/library/hashlib.html): introdução, SHA-256 e digest/hexdigest. A documentação consultada se identifica como3.14.10; a execução local é3.14.5. Código, esquema e casos próprios.

[W3C PROV Model Primer](https://www.w3.org/TR/prov-primer/), nota30/04/2013, §§2.1–2.4: entidades, atividades, uso/geração e responsabilidade. Inspira a distinção conceitual; não implementamos seus formatos ou restrições de conformidade.

Permissões/origem de dados reais, revisão científica, assinaturas, armazenamento durável, ambientes completos e contribuição pessoal exigem evidência própria; não estão resolvidos pela existência deste pacote.
