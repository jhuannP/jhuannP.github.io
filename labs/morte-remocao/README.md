# Apoptose, morte e remoção — notas de aula

Rascunho original assistido por IA; revisão pessoal de Jhuann pendente. Sem experimento, diagnóstico, dado real ou comprovação de domínio pessoal.

## Percurso conceitual

Apoptose contribui para remodelação e manutenção de tecidos. Retração, condensação e corpos delimitados por membrana são aspectos típicos; observação isolada não identifica uma via inteira. Morte e remoção por fagocitose não são o mesmo evento. Remoção eficiente pode manter baixo o estoque de células mortas visíveis; não afirmar ausência absoluta de inflamação em qualquer contexto.

Caspases são proteases, não nucleases. Iniciadoras e executoras têm mecanismos de ativação e funções distintos. Exemplo extrínseco: Fas, adaptadores, DISC e caspase-8. Exemplo intrínseco: regulação pela família Bcl2, efetores Bax/Bak, liberação de citocromo c do espaço intermembrana mitocondrial para o citosol, Apaf1/apoptossomo e caspase-9; convergência em executoras. Família Bcl2 inclui funções pró e antiapoptóticas. Esquema selecionado, vias podem interagir; não é taxonomia completa ou classificador. O livro já menciona necroptose regulada: não reduzir toda necrose a morte acidental.

Separar observação, hipótese molecular e teste discriminante. Não tomar uma imagem arredondada, DNA fragmentado ou atividade isolada de caspase como reconstrução completa do mecanismo. Sem protocolo laboratorial prescrito ou executado neste material.

## Balanço próprio: estoque não é fluxo

V e C: contagens de vivas e de unidades mortas aguardando remoção. B: acréscimo líquido de unidades vivas por produção, não o número de todas as células-filhas. D: mortes entre vivas iniciais; novas B não morrem nesse intervalo no modelo. F: remoção de mortas iniciais ou novas. Sem migração, outras perdas e fragmentação; cada morta conta como uma unidade, mesmo que uma célula biológica se fragmente.

V'=V+B−D; C'=C+D−F. Restrições: D≤V e F≤C+D, inteiros não negativos. Conservação: V'+C'+F=V+C+B. Os fluxos são entradas fornecidas, não previstos por uma rede de apoptose. O intervalo não tem duração dada, portanto não chamar D de taxa por hora.

Exemplo: V100,C4,B10,D10,F12 → V'100,C'2. Houve10 mortes apesar de V constante e C reduzido. Partindo de C0, B=D10: F10 → C'0; F2 → C'8. Mesmas mortes, visibilidades diferentes.

## Resoluções

1. V'=100. 2. C'=2. 3. F=10. 4. C'=8.
5. Proteínas; uma nuclease pode atuar a jusante da clivagem de seu inibidor.
6. Caspase-8 no exemplo Fas/DISC.
7. Citocromo c no citosol, Apaf1/apoptossomo, caspase-9.
8. Não; família inclui membros pró e antiapoptóticos.
9. Não; imagem isolada não prova mecanismo completo.
10. Não; necroptose é exemplo regulado mencionado no livro.
11. Não; B e D podem se compensar.
12. Inválido: só C+D=3 unidades mortas disponíveis para F=4.

## Executar e conferir

Na raiz do protótipo:

```sh
python3 -m unittest discover -s labs/morte-remocao -t .
```

Quatro testes: exemplo e visibilidade; oráculo por células identificadas para V,C,B entre0e4 e todos D/F admissíveis, conservação; sequência de três intervalos com remoção acumulada; contratos e preservação da entrada. Código só usa biblioteca padrão; estados congelados. Testes verificam a contabilidade escolhida, não o mecanismo molecular ou um resultado experimental.

## Referências e limites de leitura

Programa USP, CCM0211: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0211 . Reaberto27/10/2026; item7 morte celular; ativação15/07/2025. Compatibilidade com o período2025/2 não comprova programa ministrado; versão da turma não recuperada.

Alberts e colaboradores, Biologia Molecular da Célula, sexta edição, tradução Artmed2017, capítulo18 pp.1021–1027/PDF1057–1063, leitura parcial em27/10/2026. P.1022/PDF1058 visualmente conferida; trechos das demais páginas lidos por extração, sem alegar leitura integral de capítulo ou todas as legendas. Diagrama e balanço não reproduzem figuras ou exercícios do livro. PDFs privados não distribuídos.

Tentativas de apoio público NCBI Bookshelf e PubMed retornaram verificação/conteúdo indisponível; artigo na Nature redirecionou para autenticação. Essas tentativas não foram usadas como evidência conceitual ou consulta ao texto de recomendações. Recorte sustentado pelo exemplar privado efetivamente lido; taxonomia contemporânea completa continua pendente. Também faltam vias regulatórias completas, fagocitose em detalhe e análise de dados experimentais com controles.

## Registro pessoal

Data: ____ · explicação reconstruída: ____ · dúvida: ____
