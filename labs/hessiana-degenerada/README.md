# Hessiana degenerada — rascunho para revisão

Aprofundamento de `c3-hessiana`,14seções/12exercícios,4MathML;exemplo de sela,D=−4 e dois IDs anteriores preservados,assim como desafio por direções.

## Fontes

CCM0213 reconferido diretamente em22/10/2026:[USP](https://portalservicos.usp.br/jupiterweb/obterDisciplina?codcur=1020&codhab=0&sgldis=CCM0213),ativação15/07/2024;compatibilidade temporal não comprova versão ministrada. Vínculo amplo com aplicações diferenciais,não item oficial autônomo chamado Hessiana. Bibliografia oficial continua distinta de Apostol.

Acervo autorizado:Apostol,CálculoII,exemplar português previamente identificado (Reverté1996/reimpressão2004),consulta textual parcial §§9.10–9.12,pp.347–351(PDF361–365). Extração maior incluiu páginas vizinhas;sem declaração de leitura integral. Paginação confirmada no trecho,não transferida automaticamente de caches anteriores. Taylor,formas quadráticas e teste consultados. Fonte pública parcial [OpenStax Calculus3§4.7](https://openstax.org/books/calculus-volume-3/pages/4-7-maxima-minima-problems). Não foram copiados figuras,exercícios,provas completas dos textos ou PDF privado;derivações e organização próprias.

## Modelo e prova

Seis modos:0=x²−y²,1=x²+y²,2=−x²−y²,3=x²+y⁴,4=x²−y⁴,5=x². Origem estacionária em todos. Modos3–5 têm H=diag(2,0),D=0;verdades pela expressão: mínimo estrito,sela,mínimo não estrito. O painel exibe separadamente o teste inconclusivo e a conclusão por prova algébrica. Não classifica por amostragem.

Cortes0=(t,0),1=(t/√2,t/√2),2=(0,t);raio em décimos1..10. Azul=f no corte;tracejado=q=(1/2)hᵀHh. Escala vertical adaptativa com zero,explícita. Nas degeneradas,resto±y⁴ satisfaz|resto|/‖h‖²≤‖h‖²→0,mas decide o sinal ondeq=0. Não há superfície3D,numérica de mínimos ou prova de positividade por varrer cortes.

Tese visual:gráfico comparativo com tabela de H/teste/conclusão,sem superfície perspectiva que esconda sinais. Controles em coluna no celular;legendas deixam escala e alcance claros. Movimento apenas na exploração deliberada dos controles;sem animação decorativa.

## Verificar

`python3 -m unittest discover -s labs/hessiana-degenerada -t .`

Quatro testes:estênceis de segunda derivada com extrapolação exata que elimina termos de quarta ordem;resto uniforme em1734pontos racionais;provas de sinal nos casos escolhidos,escala e180configurações;contratos/exemplo preservado.54referências Python/JavaScript. Testes apoiam,mas não substituem as demonstrações e a revisão pessoal.

Próxima ação pessoal:explicar como os modos3–5 têm mesma matriz e conclusões distintas. Lagrange,fronteiras,funções gerais e cobertura integral continuam pendentes. Alternar área antes de prolongar aplicações diferenciais.
