# Regressão afim — notas de aula

Rascunho original assistido por IA; revisão pessoal pendente, sem experiência profissional ou resultado científico presumido.

## Derivação e mínimo

Modelo ŷ=wx+b, perda S=Σ(wx+b−y)². Intercepto livre:Σe=0→b=ȳ−wx̄. Inclinação:Σxe=0→w=Sxy/Sxx, com somas centradas e Sxx>0. Perturbar parâmetros soma à perda ótima Σ(δw x+δb)² porque os termos cruzados zeram. É mínimo global, único quando há dois x distintos. Com x constante c, só wc+b=ȳ é identificado; laboratório rejeita inclinação não única em vez de selecionar um par.

S,S/N,S/2 têm mesmos mínimos sem penalização; valores e gradientes diferem. Com regularização a escala relativa importa. Prova não requer ruído gaussiano: essa hipótese só entra numa interpretação probabilística adicional, que exige seu próprio desenho e independência condicional apropriada.

## Dados próprios e respostas

Original preservado:treino(0,1),(1,3),(2,5),reta2x+1,MSE0; painel, Python e desafio anteriores mantidos. Novo treino(0,1),(1,2),(2,2):x̄1,ȳ5/3,Sxx2,Sxy1,w1/2,b7/6. Previsões7/6,5/3,13/6,resíduos previsão−alvo1/6,−1/3,1/6. SSE1/6,MSE1/18;Σe=Σxe=0.

Nova previsão x3→8/3. Se alvo novo hipotético4, erro−4/3 e quadrado16/9. Não reajustar com esse alvo ao alegar teste intocado; um ponto não estima erro populacional confiável. Constante aprendida no treino5/3:MSE2/9. A reta ganha em treino, sem garantir generalização. Nova tabela é distinta dos pontos colineares do painel.

Respostas novas:1/2;7/6;1/18;0;8/3;16/9;2/9;inclinação não única se x constante;não precisa supor normalidade para otimizar;não usar teste e dizer que ficou intocado. Respostas anteriores preservadas.

## Unidades e limites

w tem unidade y/x e b unidade y. Conversão consistente de x e seus coeficientes preserva previsões, mas altera a inclinação numérica. Não inferir causalidade, lei física, precisão fora do domínio ou inferência de incerteza apenas da reta. O solver exato é univariado, sem pesos, intercepto fixado ou regularização; não é rotina numérica multivariada.

```sh
python3 -m unittest discover -s labs/regressao-afim -t .
```

Executar na raiz. Cinco testes:exemplos;27conjuntos de alvos com25perturbações cada para resíduos/decomposição exata da perda;equações normais2×2 por Cramer sem centragem no oráculo;unidades/translações/ordem;contratos e x constante. Int/Fraction sem bool/float, sem dependências novas ou instalação. Testes verificam código; a prova nas notas sustenta o caso geral.

## Fontes

Bishop, Pattern Recognition and Machine Learning2006, §§3.1–3.1.1 pp.138–142/PDF157–161 parcialmente consultados27/10/2026; p.141/PDF160 visualmente conferida. Sem leitura integral do capítulo, reprodução de figuras ou exercícios. Fórmula matricial com inversa no livro requer posto adequado; não estendida ao caso singular. Nossa derivação de uma variável e exemplos próprios. PDF privado não distribuído.

Apoio oficial parcial: https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares . Objetivo de mínimos quadrados e cuidado com dependência de colunas. Não afirma equivalência com solver, versão instalada ou desempenho do pacote; scikit-learn não foi instalado/executado.

Percurso complementar próprio, não disciplina formal cursada. Permanecem regressão múltipla,erro de medição,diagnóstico de resíduos,intervalos robustos,regularização e desenho de avaliação amplo. Registro pessoal: data____;derivação reconstruída____;dúvida____.
