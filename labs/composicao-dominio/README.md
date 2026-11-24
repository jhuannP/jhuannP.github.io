# Composição, domínio e inversa — preparação escolar

27/10/2026. Notas originais assistidas por IA, em rascunho para revisão de Jhuann e uso com aluno. Não certificam domínio pessoal ou cobertura completa do ensino médio.

Definir uma função exige domínio e contradomínio; imagem são as saídas atingidas. Composição f∘g aplica g primeiro. Para f(x)=2x+3,g(x)=x²,em2 as duas ordens dão11 e49. A ordem também pode mudar o domínio: com r(x)=1/(x−1),q(x)=x²,r∘q exclui−1 e1,enquanto q∘r exclui somente1. Em−1,uma ordem é indefinida e a outra dá1/4.

x² emℝ é uma função, mas não tem inversa funcional em sua imagem porque duas entradas podem produzir a mesma saída. Restringir domínio/contradomínio a[0,∞) permite a raiz principal como inversa. Restrição x≤0 daria outra escolha,−√y. Para todos os reais,√(x²)=|x|; a inversa depende do domínio, não só da aparência da fórmula. Inversa não é recíproco. Gráfico invertido troca(x,y) por(y,x) e reflete sobre y=x com escalas iguais.

## Fontes parcialmente consultadas

[OpenStax Algebra and Trigonometry2e §3.4](https://openstax.org/books/algebra-and-trigonometry-2e/pages/3-4-composition-of-functions): definição/composição e trecho Finding the Domain of a Composite Function. [§3.7](https://openstax.org/books/algebra-and-trigonometry-2e/pages/3-7-inverse-functions): inversa versus recíproco, troca de domínio/imagem, restrição e gráficos. Consulta parcial em27/10/2026,sem copiar exercícios,figuras ou exemplos contextualizados. Álgebra e exemplos desta aula elaborados separadamente; regras lógicas e reais conferidas. Não adotar automaticamente trechos tipográficos ambíguos da fonte,como unir exclusões por“ou”: aqui as duas condições devem ser cumpridas juntas. Nenhum currículo brasileiro ou prova específica auditado neste bloco.

## Laboratório e suas fronteiras

Execute `python3 labs/composicao-dominio/functions.py`. Quatro testes:41 pontos racionais nas duas ordens afim/quadrado e racional/quadrado,incluindo entradas excluídas;41 conferências das duas composições da inversa afim;41 candidatos de raiz não negativa para quadrados e distinção de recíproco;contratos.

O código não calcula raízes irracionais nem domínios simbólicos gerais. Para x racional,o candidato|x| é racional,tem quadrado x² e é não negativo; essa é a verificação usada. A prova real de unicidade da raiz não negativa pertence à matemática, não à grade de exemplos. Funções escolares mantêm domínio real; o domínio de representação do laboratório é int/Fraction,sem alterar o enunciado matemático.

Figura própria de quadrado restrito e raiz,janela0..4,5 e escalas iguais. O recorte visual não restringe os domínios reais. Próxima ação de20min: obter11 versus49,explicar a entrada−1 e distinguir F⁻¹(4)=2 de1/F(4)=1/16. Python opcional; aula guiada e revisão pessoal pendentes.
