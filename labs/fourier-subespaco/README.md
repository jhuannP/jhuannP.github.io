# Fourier finito — família escolhida não é completude

Funções reais emL²[0,1], produto interno por integral, s_n=sen(2πnx) eV_N=span{s_1,...,s_N}. Família ortogonal com norma²1/2, mas não completa emL²[0,1]. Não confundir com a família sen(nπx) de outro problema de contorno. Preservados exemplo, código, desafio, painel e IDs fo1/fo2 anteriores.

Fonte pública parcialmente consultada em27/10/2026: NIST DLMF§1.8(i), eq1.8.1–1.8.2, https://dlmf.nist.gov/1.8 . Fonte define série periódica completa com constante/cossenos/senos e coeficientes em[-π,π]. A adaptação de intervalo, a restrição a senos selecionados, provas finitas, exemplos, aliasing e figura são próprios. A consulta também exibiu fórmulas de Parseval, sem adotá-las como prova de completude da família restrita. Não houve leitura integral ou derivação de teoremas gerais.

Na raiz: `python3 labs/fourier-subespaco/projection.py`. Biblioteca padrão,float; quadratura por pontos médios e soma de amostras uniforme. Confere36 produtos de modos,6coeficientes de função finita conhecida, Pitágoras do exemplo,9variações de coeficientes com identidade de mínimos quadrados, constante e aliasing em4 versus16amostras. Os erros de arredondamento são tolerados; não é FFT/transformada geral, integração adaptativa ou garantia para sinais arbitrários. As funções auxiliares são de laboratório, com m inteiro1..8192; não recebem dados externos.

Exemplo f=1+s1+s2/2+s3/4: P2f=s1+s2/2, norma²5/8, resíduo²33/32 e total53/32. Constante1 tem todos os coeficientes senoidais zero, mas erro²1 para qualquerN. Quatro amostras confundem s3 com−s1 e dão coeficiente0,75 em vez de1. Não é erro da integral contínua nem reconstrução validada de dados reais.

Próxima revisão20min: derivar fator2 e identidade de erro, reconstruir a constante perdida e separar projeção de amostragem. Completude, convergência geral, Gibbs, transformadas e EDPs permanecem pendentes. Revisão pessoal de Jhuann não realizada.


## 27/10/2026 — Fourier: projeção finita e limite da família escolhida

`fourier-modos` ampliada de3 seções/2 exercícios para12/12. Preservados exemplo, Python, desafio, painel e IDs fo1/fo2. Derivadas ortogonalidade/norma1/2, coeficientes e melhor aproximação única emV_N=span{sen(2πnx),n1..N}, com identidade de erro finita. Limitada explicitamente a família: constante1 é ortogonal a todos os modos e não pode ser aproximada nesse subespaço com erro tendendo a zero. Não confundir com a família sen(nπx) ou a Fourier periódica completa.

Exemplo próprio f=1+s1+s2/2+s3/4 tem projeção emV2=s1+s2/2, norma²5/8 e resíduo²33/32; total53/32. Quatro amostras j/4 confundem s3 com−s1 e dão coeficiente0,75 em vez de1; dezesseis recuperam o coeficiente deste sinal finito. Isso não garante reconstrução de sinais arbitrários. Curvas originais e interpretação física sem inventar dinâmica/energia.

Fonte pública parcialmente consultada em27/10/2026: NIST DLMF§1.8(i), equações1.8.1–1.8.2, https://dlmf.nist.gov/1.8 . Fonte usa família periódica completa em[-π,π]. Adaptação de intervalo, restrição, provas finitas, exemplo/figura e aliasing próprios. A consulta exibiu Parseval sem adotá-lo como prova de completude da família restrita. Sem leitura integral ou reprodução de exercícios.

Verificação:14 testes de catálogo aprovados;825 estruturas MathML conferidas. Script executado com36 produtos de modos,6coeficientes por quadratura, Pitágoras do exemplo,9variações de coeficientes com identidade de erro, constante e aliasing. A quadratura é de exemplos finitos conhecidos, não integração geral ou FFT. No navegador390px, exercício5 rejeitou1/32 e aceitou33/32 pelo Enter; figura inspecionada em `fourier-subespaco-mobile.jpg`, documento390/390px e console sem erros observados. Windows real/leitor de tela não testados; revisão pessoal pendente.

FísicaMatemática:25 aulas/100 exercícios,20 introduções curtas. Global51 trilhas,552 aulas/4549 exercícios,184 introduções curtas; sem curso completo ou domínio pessoal certificado. Próxima revisão20min: derivar fator2, reconstruir erro e explicar a constante que não é representada; depois comparar integral e quatro amostras. Próxima elaboração global: consultar uma introdução de matemática do ensino médio para manter esse eixo da biblioteca em desenvolvimento. Saldo semanal78%; parada65% preservada.
