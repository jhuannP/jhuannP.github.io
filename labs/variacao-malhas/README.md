# Variação quadrática e malhas

Material original em elaboração, 27/10/2026. Revisão pessoal de Jhuann pendente. Pré-requisitos: momentos gaussianos, independência, soma de variâncias e desigualdade de Chebyshev. Percurso complementar, sem equivalência curricular ou resultado da IC presumidos.

## Estudo em dois blocos

1. Derive E[Z⁴]=3 integrando por partes; obtenha E[Q]=T e Var(Q)=2Σhᵢ². Explique como a largura máxima da partição controla a convergência L².
2. Agrupe dois incrementos e compare com interpolação. Reconstrua a identidade exata W(T)²=2ΣW(tᵢ₋₁)ΔWᵢ+Q. Explique por que igualar expectativas não iguala variáveis.

## Código e limites

Execute `python3 labs/variacao-malhas/variation.py` a partir da pasta do protótipo. Sem dependências externas.

A enumeração usa uma lei de três valores com os mesmos momentos gaussianos até ordem quatro, em 12 configurações de passos: confere média e variância de Q, não a distribuição gaussiana nem convergência browniana. A enumeração de séries finitas confere agrupamento de pares e telescopagem de quadrados. O refino por interpolação linear é tratado separadamente. A amostra gaussiana acopla duas malhas por soma de pares; uma realização não comprova teorema nem melhora monotônica. A figura mostra exemplos determinísticos, sem probabilidade positiva atribuída a incrementos gaussianos exatos.

A prova da aula estabelece L² e probabilidade para partições determinísticas. Quase certeza, teoria geral de Itô, partições adaptativas, deriva, saltos, erro de medida e inferência ficam pendentes. No modelo X=σW, σ é constante. Tempo adimensionalizado nos exemplos.

## Referências e alcance da consulta

- Pavliotis, Stochastic Processes and Applications (2014), §3.2 p.61, PDF74 do acervo autorizado: leitura textual parcial sobre variação quadrática da integral estocástica. Não é leitura integral do capítulo ou de Chorin–Hald; sem nova inspeção visual nem distribuição do PDF privado.
- [MIT OCW 18.642, Stochastic Processes II, Fall 2024](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/mit18_642_f24_lec14_1.pdf), slide19, PDF69–74: consulta textual parcial do teorema e da relação qui-quadrado. A aula explicita sua própria prova em L²; não adota uma afirmação de quase certeza sem hipóteses. O horizonte é T geral, sem confundir o caso T=1 com todos os horizontes.

Redação, exemplos, prova organizada, figura e exercícios próprios, sem copiar questões ou figuras das fontes. O conteúdo preparado não comprova estudo ou domínio pessoal de Jhuann.


## 27/10/2026 — variação quadrática: prova, agrupamento e interpolação

Aula `variacao-quadratica` ampliada de 3 seções/2 exercícios para 12/12. Preservados IDs antigos, exemplo T=1/n=100, Python, desafio e painel existente. Definidas partição determinística, largura máxima, incrementos e Q. Derivados momentos gaussianos por integração por partes, E[Q]=T e Var(Q)=2Σhᵢ²≤2T|π|; prova em L² e probabilidade, sem inferir quase certeza ou monotonicidade amostral. Comparação com curvas C¹, deslocamento total ao quadrado, escala X=σW e identidade telescópica que prepara a correção para W². Agrupamento de pares usa a mesma realização; interpolação linear de pontos fixos leva artificialmente Q/r a zero. Sem dados físicos, ruído de medida, estimação ou claim de resultado da IC.

Fontes parcialmente consultadas: Pavliotis (2014), §3.2 p.61/PDF74, extração textual do acervo autorizado sobre variação quadrática de integral estocástica; MIT OCW 18.642 (Fall2024), Stochastic Processes II, slide19/PDF69–74, consulta de texto público do teorema. A redação explicita sua própria prova em L², sem adotar afirmação irrestrita de quase certeza. Chorin–Hald não relido. Sem leitura integral dos livros, nova inspeção visual dos PDFs ou reprodução de figuras/exercícios. Fonte pública: https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/mit18_642_f24_lec14_1.pdf . Exemplos, organização da dedução, figura e código próprios.

Verificações: `python3 labs/variacao-malhas/variation.py` aprovado: 12 leis finitas de momentos, 2184 átomos ponderados por Fraction, 729 séries de seis incrementos para agrupamento e telescopagem, refinos de interpolação, exemplos e contratos. A lei de três valores coincide nos quatro primeiros momentos gaussianos, mas não é uma lei browniana. Amostra gaussiana acoplada apenas ilustrativa; não prova convergência. 14 testes de catálogo aprovados e 836 estruturas MathML conferidas. Primeira execução de catálogo sinalizou recurso externo no campo reservado a arquivos locais: URL movida para a bibliografia do curso e README; suíte reaprovada. No navegador390px, variância em malha irregular rejeitou1 e aceitou5/4 via Enter; largura390/390, console sem erros observados. Diagrama inspecionado em `variacao-malhas-mobile.jpg`; viewport restaurada. Painel antigo preservado, sem auditoria funcional adicional nesta rodada. Windows real, leitor de tela e revisão pessoal pendentes.

Processos estocásticos:25 aulas/130 exercícios próprios, oito recortes desenvolvidos e17 introduções curtas. Global:51 trilhas,558 aulas/4745 exercícios,172 introduções curtas. Contagens não certificam completude ou domínio pessoal. Próxima ação20min: derivar a variância em passos1/4 e3/4, explicar a cota da malha e distinguir agrupamento de interpolação. Próxima elaboração global: retomar lacuna de Química ou Biologia do ciclo básico após conferir cobertura oficial, preservando o equilíbrio entre disciplinas. Saldo semanal antes/depois75%; parada operacional65% mantida.
