# Contrato de função: energia cinética em SI

Implementação didática própria energy_si(mass_kg, velocity_m_s). Entradas: apenas tipos embutidos int/float, sem bool, texto, complexos, Fraction ou tipos externos. Converte a float finito; massa não negativa, inclusive zero; velocidade assinada. Nomes documentam kg e m/s, sem detectar unidades passadas incorretamente. Saída float finita não negativa em joules.

Falhas: ValueError para entrada inválida ou não conversível a float finito; OverflowError para energia fora da representação finita; ArithmeticError se energia positiva arredondaria para zero. Inteiros podem arredondar na conversão; 2**53+1 vira o mesmo float de 2**53. Fraction representa os floats já convertidos, sem recuperar precisão original. Calcular o produto racional evita estouros intermediários deste pequeno exemplo, com custo maior; não é recomendação automática para grandes vetores.

Referências de conta: 3 kg a −4 m/s dão 24 J; inverter sentido preserva energia; duplicar massa dá 48 J e duplicar velocidade dá 96 J. Para 2 kg a 72 km/h, converta a 20 m/s antes: 400 J. Passar 72 como m/s calcula 5184 J, valor 12,96 vezes maior. O validador de números não descobre essa troca de unidades.

Na raiz do site:

    python3 -m labs.contratos-energia.energy
    python3 -m unittest discover -s labs/contratos-energia -t .

Cinco testes cobrem referências, zero, valores negativos, tipos excluídos, NaN/infinito, inteiro enorme, limites da saída, escala física em 153 pares pequenos e repetição sem estado. O laboratório calcula energia clássica: não certifica regime não relativístico, medições, unidades reais, resultado da IC ou software de produção.

Aula sw-contratos: onze seções/doze exercícios. Exemplo de contagem de massas preservado; exemplos curtos Python corrigidos para tratar inteiro não conversível como ValueError. Próxima revisão: escrever sua versão do contrato e distinguir o erro de passar km/h do erro de passar NaN. Outras aulas de ambiente, tolerância, CLI e proveniência continuam introdutórias.

Fontes consultadas parcialmente em 22/10/2026: [Python — bool](https://docs.python.org/3/library/stdtypes.html#boolean-type-bool), [math.isfinite](https://docs.python.org/3/library/math.html#math.isfinite) e [Fraction](https://docs.python.org/3/library/fractions.html). As decisões desta API, exemplos e testes são próprios; não são API oficial, prova de domínio pessoal ou contrato de pesquisa. Conteúdo assistido por IA para revisão de Jhuann, sem instalação de dependências.

Verificação: cinco testes novos e 13 de catálogo aprovados; 541 estruturas MathML conferidas. Em 390 px, leitura de unidades/conversão conferida e largura da página igual à tela; exercício rejeitou 5184 e aceitou 400. Nenhum erro de console observado. Prévia: contratos-energia-mobile.jpg. Não houve revalidação integral de painéis ou suíte global; nenhum sistema externo, dependência ou contrato de pesquisa foi alterado. Catálogo: 501 aulas/3108 exercícios em rascunho. Saldo semanal após bloco: 92%; parada em 65%.


## Funções puras e borda de arquivos — 22/10/2026

pipeline.py reutiliza energy.py; não duplica sua fórmula. energy_batch recebe lista/tupla não vazia de pares (massa_kg,velocidade_m_s) e devolve tupla de energias sem modificar os pares. parse_request transforma texto JSON em pares; run_text combina parsing, cálculo e serialização em memória. main concentra leitura de arquivo e saída. Não confundir serializar texto com gravar disco.

Entrada measurements.json: objeto com exatamente unit_system="SI" e measurements=[[3,-4],[2,20],[0,10]]. Resultados na mesma ordem: 24,400,0 J. Chaves duplicadas, campos extras, pares inválidos, constantes NaN/Infinity e entradas físicas fora do contrato são rejeitados. Declarar SI não comprova conversão correta das medições. Este programa local de estudo não oferece limites de recursos para JSON hostil ou serviço de rede.

Execute a partir da raiz do site, com Python 3 e os arquivos do pacote preservados:

    python3 -m labs.contratos-energia.pipeline labs/contratos-energia/measurements.json
    python3 -m labs.contratos-energia.pipeline labs/contratos-energia/measurements.json --output meu-resultado.json
    python3 -m unittest discover -s labs/contratos-energia -t .

No Windows, use o executável Python 3 configurado (python ou py -3). O primeiro comando imprime no terminal; o segundo exige caminho de saída novo. Entrada nunca é sobrescrita. Falha de validação em qualquer par ocorre antes de abrir o destino. Arquivo existente é preservado por abertura exclusiva. Falha durante uma escrita pode deixar arquivo incompleto: não se reivindica transação atômica.

Seis testes novos verificam preservação profunda da entrada, silêncio do núcleo, repetição, parsing/relatório, esquemas inválidos, valores não finitos, colisão de saída, ausência de saída com último par inválido e execução real do módulo por subprocesso. Os arquivos usados nos testes de I/O ficam em diretórios temporários. Não foi alterado contrato ou resultado de pesquisa, nem código de cliente.

Aula sw-funcoes-puras ampliada para onze seções/doze exercícios. Exemplo de normalização e desafio anteriores preservados. Figura original camadas.svg acompanha o lote. Próxima revisão: implementar uma função sem print/open e depois uma borda que só publica após validar. Aulas de CLI, ambiente e proveniência continuam introdutórias; esta ponte prática não as torna completas.

Fontes consultadas parcialmente em 22/10/2026: [Python — Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html), introdução; [json](https://docs.python.org/3/library/json.html), loads/dumps e customização; [pathlib](https://docs.python.org/3/library/pathlib.html), leitura/abertura de arquivos. Decisões da API, exemplo e testes próprios, assistidos por IA, em rascunho para revisão de Jhuann. Nenhuma instalação de dependência ou publicação.

Verificação desta continuação: 24 testes aprovados (13 de catálogo e 11 do laboratório, incluindo seis novos de pipeline); 541 estruturas MathML conferidas. Módulo CLI executado em subprocesso com resultados 24/400/0 J; saídas existentes e entradas preservadas, lote inválido sem saída nova. Em 390 px, figura e leitura conferidas, exercício sobre lote inválido rejeitou 1 e aceitou 0; sem transbordamento horizontal ou erro de console observado. Prévia: funcoes-puras-mobile.jpg. Não houve revalidação integral dos painéis ou suíte global. Catálogo: 501 aulas/3118 exercícios em rascunho. Saldo semanal após bloco: 92%; parada em 65%.


## Ambiente e pacote completo — 22/10/2026

Aula sw-ambiente ampliada para onze seções/doze exercícios. Novo download /labs/contratos-energia.zip inclui as fontes locais necessárias, os testes e o lote. Extraia o ZIP inteiro, abra terminal na raiz com labs/ e MANIFEST.json e siga LEIA-ME.md. Sem dependências externas a instalar. Não copie .venv entre dispositivos.

    python3 -m labs.contratos-energia.environment
    python3 -m labs.contratos-energia.environment --verify
    python3 -m unittest discover -s labs/contratos-energia -t .
    python3 -m labs.contratos-energia.pipeline labs/contratos-energia/measurements.json

No Windows, use python ou py -3 conforme o executável já configurado. Execução lá ainda não verificada. Ambiente observado na construção: CPython 3.14.5, Darwin arm64. BUILD_ENVIRONMENT.json descreve essa observação, não valida o destino. O comando --verify vale na raiz do pacote extraído; a árvore do site não possui esse manifesto de distribuição.

O registro inclui apenas versão, implementação, sistema, arquitetura, lista vazia de dependências externas e parâmetros float. Não contém usuário, hostname, caminhos pessoais ou variáveis de ambiente. MANIFEST.json lista hashes SHA-256 dos arquivos do pacote, exceto ele próprio; o verificador não audita extras, não é assinatura e não prova correção científica. Empacotamento só de fontes explícitas, sem caches ou PDFs privados. Fontes e metadados iguais produzem bytes do ZIP iguais; ambiente registrado diferente também muda o pacote.

Três testes novos verificam formato do registro, construção repetida, extração, execução do pipeline com -S, conferência do manifesto, mudança/ausência de arquivo e rejeição de caminhos fora da lista prevista no manifesto. A saída esperada continua [24,400,0] J. Não basta comparar textos de ambiente ou só hashes para concluir reprodução física.

Fontes consultadas parcialmente: [Python — venv](https://docs.python.org/3/library/venv.html), [platform](https://docs.python.org/3/library/platform.html) e [hashlib](https://docs.python.org/3/library/hashlib.html), em 22/10/2026. O pacote e roteiro são próprios, assistidos por IA para revisão pessoal. Sem criação de ambiente, instalação, publicação ou alteração de pesquisa. Próxima revisão: extrair o pacote num diretório separado e distinguir integridade das fontes, contexto de execução e concordância numérica. Compatibilidade com Windows e outras versões continua pendente.

Verificação desta continuação: 27 testes direcionados aprovados (13 de catálogo e 14 do laboratório); 541 estruturas MathML conferidas. O pacote de 14 arquivos foi extraído em pasta temporária e seus 14 testes executados com -S, sem falha. Pipeline e manifesto do pacote extraído conferidos; saída [24,400,0] J. No navegador, link ZIP presente, questão sobre Windows aceitou Não, largura 390 px sem transbordamento horizontal e nenhum erro de console observado. Prévia: ambiente-pacote-mobile.jpg. Windows não executado; suíte global de simuladores não repetida. Total: 501 aulas/3128 exercícios em rascunho. Saldo semanal após bloco: 92%; parada em 65%.
