# Esperança condicional em seis estados

Rascunho original para revisão de Jhuann. Distribuição estipulada, sem dados da IC ou evidência de domínio pessoal.

## Fontes consultadas em 16/10/2026

- Pavliotis, Stochastic Processes and Applications: apêndice B.3, páginas impressas 310–311, PDF 317–318 do exemplar autorizado. Definição por informação, propriedades e torre. Leitura parcial; não capítulo integral, figura ou exercício reproduzido.
- [MIT OCW RES.6-012, transcrição L16.1](https://ocw.mit.edu/courses/res-6-012-introduction-to-probability-spring-2018/1937367208c8d3b6f1d9ae0a7e2a4373_MlsVWPWIxHI.pdf): critério de erro quadrático e média condicional.
- [MIT OCW RES.6-012, transcrição L17.2](https://ocw.mit.edu/courses/res-6-012-introduction-to-probability-spring-2018/55e1f98550110cea4b1980ec9df6224d_HL7qwWvON4.pdf): diferença entre regras gerais e afins. Consulta das transcrições, sem alegação de assistir às aulas integrais.

O percurso conserva Chorin–Hald como referência temática; não houve nova leitura desse livro neste bloco. Exemplos, distribuição, derivação finita, código e figura são próprios. PDFs privados não são servidos.

## Distribuição e informação

Y em −1,0,1 tem massas 1/4,1/2,1/4. Z independente em ±1 é equiprovável. X=Y²+σZ, σ≥0. As seis massas são 1/8,1/8,1/4,1/4,1/8,1/8. Nenhuma grandeza tem unidade física atribuída.

Informações aninhadas: nenhuma → Y → (Y,Z). Médias: 1/2 → Y² → X. Erros quadráticos mínimos: 1/4+σ² → σ² → 0. A regra escolhida g=m+δ acrescenta δ² ao erro. A figura enumera estados; segmentos verticais mostram erros individuais e não intervalos estatísticos. Tamanho/posição do ponto não codifica probabilidade.

Cov(X,Y)=0 por simetria, mas E[X|Y]=Y². Assim o ótimo afim é constante e pode ser inferior ao ótimo geral. Em σ=1, Y=0,Z=+1: observar Y piora o erro desse estado de 1/4 para 1, apesar da melhora média de 1/4. Não se conclui redução ponto a ponto das variâncias condicionais ou erros.

## Verificações

Na raiz: `python3 -m unittest discover -s labs/esperanca-condicional -t .`.

Quatro testes: referência racional por evento e fórmulas analíticas em 48 configurações; ortogonalidade contra todos os indicadores de grupo, torre e ganho entre todas as informações aninhadas; contraexemplo de covariância e erro individual; eventos nulos e domínio. `reference.json` fornece 27 configurações JS/Python, conferidas no teste de simulações. A comparação entre linguagens não substitui a prova finita ou os balanços analíticos.

Eventos de probabilidade zero recebem versão arbitrária zero no código, sem efeito nas médias; não se usa quociente por zero. No painel todos os eventos elementares têm massa positiva.

## Limites e próximos estudos

A lei conjunta é conhecida. Não há estimação, ajuste a amostras, intervalo de confiança, previsão temporal ou resultado de pesquisa. Projeção estática não produz, por si só, dinâmica Markoviana nem remove memória. Teoria de existência geral, distribuições contínuas, inferência com dependência temporal e fechamento dinâmico continuam pendentes. Todo o curso permanece em elaboração.
