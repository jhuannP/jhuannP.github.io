# Uma CLI para comparar decaimento

Rascunho para revisão pessoal. Laboratório original com biblioteca padrão. Modelo u′=−ku,u(0)=u0,T>0,k≥0,u0≥0. Tempo em s,taxa s⁻¹,estado em U. Euler iterado e referência u0 exp(−kT). Não é dado físico,estimativa de parâmetro ou resultado de IC.

Na raiz do protótipo,no Mac use o interpretador Python3 disponível;no Windows o executável configurado pode chamar-se python ou py. Windows físico não foi testado. Exemplo com nome genérico:

```sh
python labs/cli-decay/cli.py --steps 4 --duration 1 --rate 1 --initial 1
python labs/cli-decay/cli.py --help
python labs/cli-decay/cli.py --steps 0
```

Primeiro:status0,um JSON em stdout,stderr vazio. endpoint81/256=0.31640625,reference≈0.36787944117144233,erro absoluto≈0.05147319117144233. Ajuda:status0,ajuda em stdout,stderr vazio. Inválido:status2,stdout vazio,diagnóstico em stderr. Forma da ajuda pode variar por versão de Python;testes não dependem do texto completo. Nenhuma opção escreve arquivo ou usa rede. Evite redirecionar para arquivo existente;redireção é ação do shell,não feita pelo programa.

Steps inteiro1..100000,demais números finitos;T>0,k/u0≥0 e kT finito. Perfil Euler exige0≤kT/n≤1 para manter decaimento não negativo monótono:mais restritivo que estabilidade absoluta,é decisão desta ferramenta. Exact não usa steps no cálculo,mas registra configuração para comparação. JSON usa allow_nan=False. Entrada decimal da CLI usa ponto;vírgula do texto em português não muda o parser. Opções abreviadas rejeitadas. Última opção repetida segue comportamento normal do argparse;isso não é um arquivo de proveniência completo.

Separados parser,modelo puro e main(argv). Importar o arquivo não lê parâmetros,não imprime resultado. O guard chama main() sem argumentos apenas na execução direta; chamadas explícitas a main com lista usam essa lista. Testes executam subprocessos com lista de argumentos,shell=False,interpretador atual e timeout,sem mexer em serviços ou arquivos externos.

## Fontes consultadas em29/10/2026

Documentação oficial Python3.14 argparse:ArgumentParser,add_argument,parse_args,types,choices,help,error e allow_abbrev;json.dump/dumps com sort_keys/allow_nan. Recortes textuais,sem copiar tutorial/exemplo. https://docs.python.org/3.14/library/argparse.html e https://docs.python.org/3.14/library/json.html . A URL genérica redirecionou a3.15;conferida explicitamente3.14 para compatibilidade com interpretador local3.14.5. Não usa parâmetros novos de3.15,nem comprova outras versões. CLI e testes próprios;sem livro privado novo/oferta curricular reconferida. Biblioteca padrão não requer instalação.

## Verificar

```sh
python -B -m unittest discover -s labs/cli-decay -t .
```

Seis métodos:nove casos numéricos contra Decimal60;duas execuções idênticas/JSON;ajuda;11 entradas CLI inválidas;importação sem efeito e método exact;contratos diretos. Testes de produto/erro não certificam utilidade pedagógica,formação pessoal ou validade científica de um modelo real. Reprodutibilidade local não garante mesmos bits em todo sistema.
