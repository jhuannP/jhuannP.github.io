# Condicionais e agregação

Rascunho original, 22/10/2026; revisão de Jhuann pendente. Pré-requisitos: condicionais, partições e probabilidade total. Aula `condicional-agregacao`, complemento do percurso probabilístico de Computação IV, sem equivalência administrativa adicional.

## Fontes e limites

Consultados parcialmente os trechos locais autorizados: Magalhães e Lima, *Noções de Probabilidade e Estatística*, 7ª ed., §2.2, pp.54–59 (PDF69–74), especialmente partição e probabilidade total pp.58–59; Magalhães, *Probabilidade e Variáveis Aleatórias*, 2ª ed., §1.3, pp.26–30 (PDF18–20 em páginas duplas), especialmente a demonstração de Bayes por produto e probabilidade total em p.30. Releitura dos extratos disponíveis; não houve leitura integral. O primeiro PDF tem avisos de extração de fluxo registrados em consultas anteriores; os trechos usados permanecem legíveis.

O exemplo de inversão, a padronização com pesos comuns, a prova por diferenças e os exercícios são desenvolvimento próprio dessas regras. Não se atribui aos livros este exemplo nem uma teoria causal. Nenhuma página, figura ou arquivo dos livros acompanha o site.

## Modelo

Dois grupos, duas opções, sucesso/falha. Linha=(sucessos_A,total_A,sucessos_B,total_B): (9,10,72,90) e (27,90,2,10). Escolha uniforme entre 200 registros sintéticos. A: taxas 9/10 e 3/10; B: 4/5 e 1/5. Agregadas: A=9/25, B=37/50. P(G=0|A)=1/10; P(G=0|B)=9/10. Com pesos comuns w=1/2, A=3/5, B=1/2. A diferença padronizada é 1/10 para qualquer w em [0,1].

São perguntas descritivas diferentes, não um experimento nem evidência causal. O peso comum não é automaticamente a resposta correta. Escolher ajuste exige conhecer o processo e a pergunta. O contrato rejeita totais nulos em qualquer opção/grupo; não extrapola taxas não identificadas. Aceita contagens inteiras e pesos racionais; evita arredondamento nas comparações.

## Organização e verificação

Preserva o desenho existente: leitura sequencial, exemplo resolvido, exercícios com feedback e código consultável, sem controles decorativos. Duas fórmulas MathML. Não cria painel com simulação aleatória para uma tabela completamente especificada.

Execute na raiz: `python3 -m unittest discover -s labs/condicional-agregacao -t .` e `python3 labs/condicional-agregacao/experiment.py`. Testes independentes materializam objetos distintos para conferir taxas agregadas; verificam decomposição por pesos, escala, troca de grupos, ordem com pesos comuns e contratos.

Próxima ação pessoal: reconstruir as quatro taxas sem solução; depois explicar por que usar 1/2 responde a outra pergunta. Próxima ampliação possível: comparar graficamente pesos específicos e comuns após revisão; inferência amostral, dados observados e causalidade permanecem fora deste recorte.

## Painel de pesos — 22/10/2026

Tese visual: quatro pares de barras sobre o mesmo eixo 0–1, com rótulos A/B e frações, separam taxas internas, mistura e padronização. Conteúdo: controles de composição, barras, tabela exata e interpretação. Interação: teclado altera um peso por vez; leitura acompanha imediatamente a mudança de ordem e a diferença. Sem animação ornamental.

Pesos de G=0 em porcentagem: a para A, b para B, w para alvo comum. Taxas internas A=(9/10,3/10), B=(4/5,1/5). Mistura A=(300+6a)/1000; B=(200+6b)/1000. Comuns usam w em ambas. Para pesos fracionários x, inversão se x_B−x_A>1/6. Nenhum par de porcentagens inteiras fica exatamente no limiar. Componentes ausentes conservam parâmetros fornecidos, não condicionais identificadas. O painel permite peso zero, enquanto `compare` exige tabelas com totais positivos: contratos diferentes explicitados.

363 estados de referência por enumeração de mil objetos distintos por opção (não amostragem); taxas alvo por Fraction. JavaScript compara todos e verifica 10201 pares inteiros pelo limiar analítico. As contagens ampliadas recuperam as proporções do exemplo inicial e constroem outros cenários sintéticos; não são novos dados observados.

Fontes conceituais permanecem as consultas parciais aos dois livros registradas acima, sem nova leitura ou reprodução. Derivação, painel e números são próprios. A aula tem agora 12 seções/10 exercícios. Próxima ação pessoal: prever o cruzamento ao diminuir apenas b, depois explicar por que w não muda a mistura.

Verificação do painel: suíte JS aprovada (363 referências e 10201 pares), catálogo 12 testes e 410 MathML. Teclado, mudança do alvo sem alterar mistura, peso zero e resposta −19/50 conferidos no navegador; 390 px sem transbordamento horizontal, console sem erros observados. Prévia móvel `condicional-pesos-mobile.jpg` na raiz. Rascunho pendente de revisão pessoal. Saldo 77%; parada 65%.
