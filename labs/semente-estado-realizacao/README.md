# Semente, estado e realização

Material original em rascunho,percurso próprio de software para pesquisa. Sem dados pessoais,observacionais ou da IC. Não representa disciplina cursada ou domínio demonstrado por Jhuann.

Execute `python3 draws.py` para os cinco testes. `python3 draws.py --report` produz um JSON no terminal,sem escrever ou substituir arquivos. O `example.json` desta pasta foi gerado no Mac com CPython3.14.5. Não foi executado no Windows. Não exige bibliotecas adicionais.

## Protocolo explícito

Uma instância random.Random(42),uma chamada randrange(1,7) por dado,12 chamadas em ordem sequencial. O registro contém os valores,a média racional,implementação/versão do Python,plataforma e SHA-256 do código. Não guarda caminhos privados,credenciais ou metadados pessoais. Hash identifica bytes,sem certificar correção ou validade científica.

O código recebe o gerador local como dependência. Recriar a mesma instância dentro de cada lote repete a realização. Usar uma instância continuada consome os trechos seguintes; getstate/setstate retoma um ponto posterior ao prefixo. A função que consome rng tem efeito sobre seu estado. Outras instâncias não compartilham esse estado,nem alteram a instância global nesse exemplo.

Método,ordem de chamadas e implementação também importam. Não garantimos que toda alteração de chamada produza valores diferentes,pois coincidências são possíveis. Sementes diferentes não provam independência. Paralelismo exige um protocolo de fluxos/ordem,ainda não implementado.

## Referência probabilística separada

No modelo ideal,os lançamentos D são uniformes em1..6 e independentes. E[D]=7/2,E[D²]=91/6,Var(D)=35/12. Para média de N,Var=35/(12N),pela independência. O laboratório enumera todas as6ⁿ tuplas para N1..4,1554 tuplas no total,e calcula as leis/momentos com Fraction,sem amostragem pseudoaleatória. Em N4,são1296 casos e variância35/48.

As médias de vinte cópias de um lote reiniciado são idênticas,com variância empírica zero; isso não estima a variância35/48 da lei ideal. Uma semente fixa é determinística; as hipóteses probabilísticas não decorrem do controle do software. Não é teste de uniformidade,qualidade geral de gerador ou validação de processo físico. Reduzir variância teórica com N não garante queda monótona do erro em toda realização.

## Fontes consultadas parcialmente em27/10/2026

[Documentação oficial Python3.14,random](https://docs.python.org/3.14/library/random.html): introdução,Random,randrange,getstate/setstate,choice/choices e Notes on Reproducibility. A revisão online identificada foi3.14.10;ambiente executado3.14.5. A abertura inicial do endereço geral retornou3.15.2,e não foi usada como descrição da versão executada. Nenhum ambiente alterado ou pacote instalado.

A documentação limita a garantia de continuidade entre versões ao método random() com inicialização compatível; não a estendemos automaticamente ao amostrador randrange. A distinção entre choice e choices também está documentada. Leitura parcial,sem auditoria de toda a implementação ou do artigo do Mersenne Twister. Modelo ideal,figura,distribuição exata,código e exercícios próprios.

## Verificações e limites

Cinco testes: repetição e isolamento do estado local/global; lote segmentado versus sequência inteira; captura/restauração de continuação;1554 tuplas com normalização,momentos e evento extremo; vinte reinicializações e metadados/contratos. Todas as comparações probabilísticas exatas são finitas. Nenhum teste de amostra aleatória precisa acertar casualmente uma tolerância estatística. Leitor de tela,Windows real,revisão pessoal e avaliação de fluxos paralelos continuam pendentes.

Próxima ação de20min: executar testes e relatório,explicar reinício/continuação/checkpoint e reconstruir35/48 para a média de quatro dados. Depois conectar a documentação de uma execução científica real quando houver material pessoal revisado e publicável.
