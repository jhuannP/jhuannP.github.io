# Semelhança: correspondência antes da proporção

Material original assistido por IA, revisão de Jhuann pendente. Curso próprio de apoio escolar, sem equivalência com disciplina USP. A auditoria identificou que proporções, Pitágoras e escala já existiam, mas não uma sequência própria de critérios/correspondência/paralela. Não substituir ou duplicar aquelas aulas.

Exemplo original: A=(0,0),B=(15,0),C=(0,20), unidadescm; k=3/5 dáD=(9,0),E=(0,12),DE=15,áreas150e54cm²,restante96cm². Parte/total3/5 é distinta de parte/restante3/2. Figura original com eixos escalados igualmente, sem copiar notas. Sombras: alturas e comprimentos prescritos1,8/2,7/10,5m dão7m, apenas nas hipóteses de postes verticais, mesmo instante, chão horizontal e raios paralelos; sem dados coletados.

`triangles.py`: int/Fraction apenas, rejeita float/bool; triângulos não degenerados; pontos rotuladosA,B,C. `similarity_ratio2` comparaAB/AC/BC na correspondência dada, retorna k² ouNone, não a escala k e não procura automaticamente uma permutação. `parallel_cut` exige0<k<1, não trata prolongamentos. `transform` usa escala positiva, quartos de volta0..3, reflexão opcional e translação. `shadow_height` exige três comprimentos positivos na mesma unidade, não verifica as hipóteses físicas. Nada lê desenhos/fotos ou decide semelhança de medidas aproximadas.

## Reprodução da raiz
```sh
python3 -B -m unittest discover -s labs/semelhanca-triangulos -t .
```
Seis métodos: marcos/6 permutações simultâneas e correspondência errada;192 transformações (8 triângulos×3 escalas×4 rotações×2 reflexões);9 cortes comparados à interseção independente de retas por determinantes;4 áreas por contagem de pontos/Pick;contraexemplos e3 conversões de unidade das sombras;contratos. Pick é só referência de teste, não pré-requisito escolar. Raízes não são arredondadas para decidir similaridade; áreas e razões quadráticas são exatas.

## Fontes consultadas parcialmente em29/10/2026
- [MóduloIMPA/OBMEP](https://portaldaobmep.impa.br/index.php/modulo/ver?modulo=10), índice para localizar as notas; vídeos não assistidos.
- [Jocelino Sato — Semelhança entre triângulos,ParteI](https://cdnportaldaobmep.impa.br/portaldaobmep/uploads/material_teorico/5vlz1w30j008o.pdf), revisãoAntonio Caminha M.Neto,04/05/2026: definição/correspondência pp1–2/PDF2–3 e critérios pp4–6/PDF5–7. Recortes textuais; pedidos de screenshot não produziram imagem inspecionável nesta sessão, portanto não se registra conferência visual. Não é leitura integral. A argumentação local usa dilatação+congruência e exemplo próprio.
- [Marcelo Mendes/Antonio Caminha — Tales,ParteI](https://cdnportaldaobmep.impa.br/portaldaobmep/uploads/material_teorico/crlc010v9bswo.pdf),05/02/2026: razão de segmentos pp1–2/PDF2–3. Sem copiar exemplos/soluções. O recorte triangular paralelo é deduzido localmente porAA e por vetores no laboratório; não se apresenta como prova de Tales geral.
- Resultado inicial TalesParteIII abriu, mas não corresponde ao recorte escolhido e não foi usado como corpo de fonte; outro PDF de resultado de busca deu cachemiss. Fontes utilizadas foram encontradas pelos links do módulo oficial, sem insistir em URLs presumidas.

Revisão do aluno, bissetrizes, Tales geral, polígonos, relações métricas e medições incertas seguem pendentes. Código e rascunho não certificam domínio ou aula aplicada.
