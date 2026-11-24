# Dois eixos, um relógio — conferência opcional

Modelo: origem no lançamento, solo plano no mesmo nível de chegada, apenas gravidade constante, sem ar. x direita/y cima; v0x,v0y,g positivos, SI. Estado em T é imediatamente antes do contato; após a chegada o modelo não se aplica. Não calcula forças de impacto, arrasto, alturas distintas ou lançamento horizontal.

OpenStax Physics§5.3, https://openstax.org/books/physics/pages/5-3-projectile-motion , consulta textual parcial em27/10/2026: hipóteses, componentes e equações por eixos. Sem copiar tabela, figura, exemplo numérico ou assistir ao vídeo. Exemplo6/8/10, derivação do limite de alcance por quadrado não negativo, checagens e figura próprios. Não houve experimento ou uso com aluno.

Na raiz: `python3 labs/lancamento-dois-eixos/projectile.py`. Biblioteca padrão, int/Fraction sem bool/float. Tempo racional em[0,T]. Conferência de378estados em18cenários: energia específica, simetria temporal, velocidade/altura de topo, equação de trajetória e alcance máximo; contratos e caso de referência. Verificações complementam a derivação, não são comparação com medições reais.

Exemplo v0=(6,8)m/s,g10m/s²: topo0,8s/3,2m, voo1,6s, alcance9,6m. No topo v=(6,0)m/s e a=(0,−10)m/s². Em1s, posição(6,3)m e componente vertical−2m/s. Altura máxima não implica velocidade/aceleração totais nulas. g10 é parâmetro didático, não medição local.

Próxima revisão20min: desenhar as duas grandezas em três instantes e resolver o retorno positivo. Notas e exercícios não exigem programação. Revisão pessoal, validação com aluno, medições e modelos mais amplos pendentes.


## 27/10/2026 — lançamento oblíquo e componentes

Nova `ef-lancamento-obliquo`,12 seções/12 exercícios, com Python opcional. Modelo de voo após lançamento até antes do impacto, solo plano e mesma altura, gravidade constante/sem ar. Eixos e sinais, componentes versus módulo, topo, raízes do retorno, alcance, parábola e energia específica. Exemplo6/8 m/s,g10 m/s²: topo0,8s/3,2m, voo1,6s e alcance9,6m; no topo v=(6,0) e a=(0,−10). Limite R≤v0²/g derivado por quadrado não negativo, sem afirmar ângulo ótimo universal. Figura e roteiro originais, demais aulas preservadas.

Fonte pública parcialmente consultada em27/10/2026: OpenStax Physics§5.3, https://openstax.org/books/physics/pages/5-3-projectile-motion . Hipóteses e equações por eixos; não copiados tabela, exemplo, figura ou vídeo. Dados, derivações adicionais, script e atividades próprios. Sem experimento ou trajetórias reais reivindicados; g10 é parâmetro didático.

Verificação:14 testes de catálogo aprovados;829 estruturas MathML conferidas. Script racional executado com378estados de18cenários: energia específica constante, simetria temporal, equação da trajetória, topo e alcance; casos de referência/contratos. Não valida arrasto, medições ou impacto. No navegador390px, exercício3 rejeitou0 e aceitou6 pelo Enter; figura inspecionada em `lancamento-dois-eixos-mobile.jpg`, documento390/390px e console sem erros observados. Setas de v/a com unidades/escalas distintas explicitadas. Windows real/leitor de tela/uso com aluno não testados; revisão pessoal pendente.

FísicaEscolar:14 aulas/166 exercícios, sem recortes de até três seções, sem implicar cobertura completa. Global51 trilhas,554 aulas/4573 exercícios,184 introduções curtas. Nenhum curso completo ou domínio pessoal certificado. Próxima revisão20min: desenhar v/a em três instantes e justificar as duas raízes do retorno. Próxima elaboração global: conferir uma introdução de ComputaçãoIII/análise numérica e o material de referência antes de ampliar. Saldo semanal77%; parada65% preservada.
