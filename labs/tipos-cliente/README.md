# Usar tipos: contratos de cliente

30/10/2026. Rascunho original para revisão de Jhuann.

`label_key` exige string não vazia apósstrip,NFC,casefold eNFC. Preserva o original,não remove acentos/espaços internos;é política local de rótulos. Chave igual não prova entidade igual;não aplicar a símbolos/unidades com significado de caixa. Desafio antigo semNFC/validação preservado,contrato adicional não substitui silenciosamente o anterior.

Listas: atribuição compartilha;appendmuda e retornaNone;cópia externa isolaappendexterno,não elementos aninhados. Anotação não é validação runtimeautomática. Complexos: z3+4j,w−3+4j têm módulos5/5,soma8j,módulo8;quadrado64=25+25+14,termo cruzado2Re(zconj(w)). Sem unidades implícitas. Aritmética aproximada;helper rejeita entradas/resultados não finitos,sem cálculo simbólico geral.

Fontes: Sedgewick/Wayne,ComputerScience©2017,§3.1pp330–331/PDF351–352,consulta textual parcial30/10/2026,emJava;sem copiar atividades. PáginaPythonPrinceton retornou403,não usada como corpo lido. [TiposPython3.14](https://docs.python.org/3.14/library/stdtypes.html),[Unicode](https://docs.python.org/3.14/library/unicodedata.html),[anotações](https://docs.python.org/3/library/typing.html)consultados parcialmente30/10. [JúpiterCCM0118](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0118)reaberto,ativação15/07/2024 posterior à turma;versão ministrada não comprovada.

```sh
python3 labs/tipos-cliente/client.py
python3 -B -m unittest discover -s labs/tipos-cliente -t .
```

Cinco testes:três paresUnicode/original/idempotência/acentos/comprimentos;mutação,alias,cópia externa/aninhada eanotação;referência complexa/zero;625pares porcomponentes comidentidade independente e material antigo;contratos. Não certifica Unicode geral,toda a linguagem ou habilidade pessoal. Exemplos e gráfico locais;semPDF privado.
