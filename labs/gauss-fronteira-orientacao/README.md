# Gauss: fronteira completa,orientação e domínio

Rascunho original. Execute `python3 flux.py`,sem dependências adicionais. Campos polinomiais e sólidos unitários adimensionais;nenhum campo medido ou dado da pesquisa.

## O que foi demonstrado

Sob F C¹ num aberto contendo o volume e sua fronteira regular por partes,Gauss relaciona o fluxo externo em toda a fronteira à integral tripla de divF. Na caixa,a prova agrupa faces opostas e usa teorema fundamental/Fubini em cada componente. O texto não apresenta cancelamento informal como demonstração global para qualquer sólido irregular.

Para F=(x,y,z) no cubo[0,1]³,fluxos0,1,0,1,0,1 somam3. Para F=(x²,y,z) no tetraedro x,y,z≥0,x+y+z≤1,volume1/6,momento de x1/24 e divF2x+2 dão5/12. Faces coordenadas são nulas;face inclinada com r(u,v)=(u,v,1−u−v) tem produto vetorial(1,1,1),fluxo pela integral de u²+1−u no triângulo. Normal unitária e fator de área se compensam;omitir um deles altera o resultado.

Para K=(0,0,1),o fluxo fechado é0,base−1/2 e face inclinada+1/2. Divergência zero não impõe fluxo zero à face aberta,nem campo zero. A conta por fechamento requer todas as partes e sinais.

## Buraco e singularidade

H=r/|r|³ só está definido fora da origem. divH=0 nesse domínio,enquanto o fluxo na esfera centrada é4π. Gauss ordinário não pode ser usado na bola que contém a singularidade. Na casca com raio interno a>0,a normal da borda interna aponta para o centro;fluxos4π e−4π somam0. Não usamos distribuições generalizadas para ignorar as hipóteses do enunciado.

Unidades:se F tem unidade U,fluxo tem U·comprimento² e divF,U/comprimento. O desafio original F=(x,y,z) cresce com a geometria e dá3L³;um campo de amplitude fixa F₀(x/L,y/L,z/L) dá3F₀L². Dizer o que é escalado evita uma lei de potência indevida.

## Fontes parcialmente consultadas em27/10/2026

- Apostol,CálculoVolII,tradução portuguesa do exemplar identificado no acervo,§12.19:título p.511/PDF524 e pp.512–514/PDF525–527,Teorema12.6 e ideia por projeções. OCR imperfeito em símbolos e palavras;enunciado suficiente e álgebra da aula conferidos separadamente. Sem nova inspeção visual,leitura integral ou distribuição do PDF. Não se adota uma extensão a todo sólido irregular com base no OCR.
- [OpenStax CalculusVol3§6.8](https://openstax.org/books/calculus-volume-3/pages/6-8-the-divergence-theorem),enunciado com C¹ em aberto contendo o sólido e explicação de faces internas,recortes.

Prova da caixa,números,tetraedro,figura,código e exercícios próprios,sem reprodução dos exemplos/fontes. Júpiter não reaberto neste bloco;limitações do programa de MatemáticaIV e versão da turma permanecem no mapa existente. Cálculo3 é organização editorial,não equivalência administrativa automática.

## Verificações

Cinco testes:regra racional de Boole exata em graus0..5 e contratos;exemplos cubo/tetraedro;60campos monomiais vetoriais de grau total≤3 nos dois sólidos;campo constante/face aberta;fluxo radial esférico e sinais da casca. Faces são integradas por quadratura racional,sem usar divF. Divergência usa momentos analíticos independentes:cubo,produto de1/(p+1);tetraedro,p!q!r!/(p+q+r+3)!. Parametrização do triângulo u=s,v=(1−s)t tem Jacobiano1−s,e os graus transformados cabem na regra. Linearidade estende essa verificação à combinação desses monômios,no domínio restrito do código.

A esfera usa Simpson em ângulo polar e pontos médios no azimute,avaliando campo,normal e fator de área. É conferência aproximada deste campo,não prova numérica de Gauss ou integração de singularidade. Contratos não abrangem campos arbitrários ou domínios gerais. Revisão pessoal,Windows real e leitor de tela pendentes.

Próxima ação20min:provar a caixa,conferir5/12 por duas integrais e explicar a base−1/2 e a normal da cavidade. Depois registrar dúvidas antes de estudar Stokes.
