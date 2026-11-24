# Primeiro programa: executar,observar e diagnosticar

Notas originais em rascunho. Começar com uma previsão em unidades físicas;texto preparado não comprova prática pessoal.

## Executar

Na pasta deste laboratório: `python3 viagem.py` ou `py viagem.py`,conforme o interpretador já disponível. Confira o comando no ambiente antes de usá-lo. Saída esperada:velocidade15.0m/s,tempo20.0s. Não foi realizado teste físico no Windows. Sem instalação ou alteração de ambiente.

Na raiz do protótipo: `python3 labs/primeiro-diagnostico/run_cases.py`; testes:`python3 -m unittest discover -s labs/primeiro-diagnostico -t .`.

O roteiro lê somente viagem.py/cases.json e cria cópias temporárias para observação de processos,com limite3s. Não é sandbox nem avaliador para código não confiável;nenhum endpoint de execução foi criado no site. Não envia dados ou modifica arquivos do usuário.

Sintaxe:chamada incompleta impede toda execução do arquivo,inclusive o primeiro print. NameError:primeiro print executa,e os seguintes ao erro não são alcançados. Unidades:300/54 rotulado como segundos roda normalmente,mas é conta inadequada. Correto:54km/h=15m/s,300m/15m/s=20s. Arquivo ausente falha antes de executar seu conteúdo. Mensagens completas podem variar por versão/idioma;testes verificam categorias,canais e resultados.

## Fontes

Sedgewick e Wayne,Computer Science,§1.1 pp.2–5/PDF23–26,consulta textual parcial29/10/2026 ao acervo autorizado,cabeçalhos conferidos. Exemplar com copyright2017;programaUSP lista2016,sem corrigir silenciosamente a bibliografia. FonteusaJava/compilação/JVM;instruções Python são adaptação própria,sem copiar código ou figura. Sem nova inspeção visual/leitura integral ou PDF servido.

[Python Tutorial§§8.1–8.2](https://docs.python.org/3/tutorial/errors.html) e [apêndice§16.1.1](https://docs.python.org/3/tutorial/appendix.html#interactive-mode),consulta parcial29/10/2026. Páginas exibidas3.15.2;testes usam o interpretador local disponível,sem presumir mesma versão. [JúpiterCCM0118](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0118),reaberto29/10,ativação15/07/2024;versão da turma2023/2 não recuperada.

## Próxima prática

Prever15m/s e20s,executar,alterar somente300→450m,esperar30s e explicar o resultado. Prática pessoal,Windows físico,debugger,tratamento de exceções e cobertura ampla de depuração permanecem pendentes.
