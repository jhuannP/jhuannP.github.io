# Gram–Schmidt em aritmética decimal controlada

Extensão original assistida por IA; revisão pessoal pendente. Preserva laboratório racional,painel,IDs,exemplo,snippet e desafio de `al-gram-schmidt`. Não é benchmark de software,teste estatístico ou medida experimental.

Entrada prescrita A4×3:colunas(1,ε,0,0),(1,0,ε,0),(1,0,0,ε). ε é texto decimal em[1e−8,1]. Colunas independentes para ε>0 pelo bloco inferiorεI. AᵀA=J+ε²I;κ₂=√(3+ε²)/ε. Escala/condicionamento não são dependência exata.

`factor`:Decimal8…80 dígitos significativos,ROUND_HALF_EVEN;CGS usa coluna original,MGS usa resíduo atualizado,MGS2 repete a passagem antes da normalização e acumula correções emR. Contexto local restaurado. Não usa float,numpy,aleatoriedade,precisão adaptativa,pivotamento ou Householder. Norma decimal zero interrompe,não classifica posto universalmente.

`diagnostics`:máximo absoluto por entrada deQᵀQ−I eA−QR,avaliados a90 dígitos. Não são norma espectral ou erro relativo. `analytic_columns`:normaliza fórmulas fechadas u1=(1,ε,0,0),u2=(ε,−1,1+ε²,0),u3=(ε,−1,−1,2+ε²),sem chamar a fatoração.

Emε=.0001,precisão8,CGS:E⊥.4999999700376976,Erec3.356064e−13;MGS:E⊥.000070710676,Erec5.6438166e−13;MGS2:E⊥5.7760548437120759e−8,Erec6.643936e−13. A raiz√1.00000001 arredonda para1.0000000;vetores computados podem ter normas verdadeiras diferentes de1. Esse caso não prova ranking/garantia para qualquer problema ou para float binário.

## Reprodução da raiz
```sh
python3 labs/gram-schmidt-arredondamento/decimal_qr.py
python3 -B -m unittest discover -s labs/gram-schmidt-arredondamento -t .
```
Seis métodos:cancelamento literal ecolunas CGS8;15 fatorações60 comparadas a fórmulas fechadas90 (5ε×3métodos);diagnósticos de3saídas8 por Fractions exatas;limites específicos do exemplo e ortogonalidade das fórmulas cruas;isolamento de contexto;contratos. Não confundir esses casos com prova geral de estabilidade.

## Fontes realmente consultadas em29/10/2026
- ElonLagesLima,ÁlgebraLinear,IMPA2014,exemplar privado complementar já localizado:§10 pp124–125/PDF135–136,recortes textuais sobre construção/prefixos e p125 visualmente conferida. O material não copia figura ou exercício. Apostol da aula anterior não foi relido nesta extensão. Bibliografia nominal IF permanece não identificada segundo auditoria anterior,sem nova busca nominal.
- [Netlib—Basic Algorithm](https://netlib.org/utk/people/JackDongarra/etemplates/node138.html),capítuloJacobi–Davidson,G.Sleijpen,versão de página2000:fases3–5/comentário de refinamento consultados parcialmente. Não implementar o algoritmo de autovalores ou atribuir ao nosso procedimento a garantia/critério adaptativo da fonte;duas passagens fixas são escolha local.
- [CatálogoBCC/IME2017—MAT0122](https://bccdev.ime.usp.br/principal/catalogo2017/disciplinas/MAT0122.html) reaberto. Júpiter direto não recuperado;fonte2017 não prova turma IF2022/1, RN preservado. Aprovação posterior emMatemáticaIII é outro registro. Complemento numérico não chamado de obrigação da turma.
- CERFACS teve timeout,UCI502 eUMD exibiu verificação antirrobô. Não contornados nem usados como corpo de fonte;resultados de busca não substituíram leitura.

Faltam tolerância de posto com escala/incerteza,pivotamento,Householder,implementações gerais e verificação pessoal. A figura original separa os dois diagnósticos sem sugerir que uma tabela de caso demonstra teoria completa.
