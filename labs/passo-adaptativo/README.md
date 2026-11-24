# Passo adaptativo por duplicação de RK4

Rascunho didático original de 22/10/2026, para revisão de Jhuann. Exemplo escalar adimensional; sem dados de pesquisa ou evidência pessoal de domínio.

`experiment.py` é autônomo em Python 3 e imprime todas as tentativas para y′=−y em [0,3], y(0)=1, h inicial 1, atol=10⁻⁶ e rtol=0. Aceita dois meios passos diretamente, sem extrapolação. Não é RK–Fehlberg. A opção `record_attempts=True` adiciona o histórico de candidatos, estimativas, escalas, razão, decisão e fator; o retorno padrão preserva as chaves trace/accepted/rejected. O solver correspondente em numerics4.py e os exemplos da aula foram atualizados em conjunto.

## Referência e convenção

Burden, Faires e Burden, *Análise Numérica*, tradução da 10ª edição, exemplar privado anteriormente identificado como Cengage 2016. Consulta visual parcial nesta data: §5.4, início p. 309 (PDF 323) e p. 314 (PDF 328); §5.5, pp. 322–325 (PDF 336–339). Não foi lida a totalidade de §§5.4–5.5. As páginas impressas 308 e 321 também foram abertas para localizar a numeração; seus exercícios não foram usados. Offset físico confirmado nesta região: +14, corrigindo a hipótese anterior de +13. Não transferir esse offset a outras partes sem verificar.

O livro apresenta uma convenção de erro de truncamento local dividido por h, de ordem h⁴ para o método de ordem 4; o controlador ali discutido usa quarta raiz. Esta implementação compara o defeito no estado, de ordem h⁵, e usa quinta raiz. O fator 15 é derivado na aula por duplicação de passo, com suavidade e regime assintótico explícitos. A leitura do par embutido de Fehlberg fundamenta a distinção: seis avaliações compartilhadas no par apresentado, versus 12 por tentativa nesta implementação simples, sem reaproveitamento. Não se copiaram exercícios, figuras ou páginas; PDFs privados não são distribuídos.

## Como explorar

```sh
python3 labs/passo-adaptativo/experiment.py
python3 -m unittest discover -p 'test_*.py'
```

O padrão produz uma rejeição e dez aceitações. A primeira razão é aproximadamente 455,277; após rejeitar h=1 sem avançar, tenta h≈0,264598. O erro global observado ao fim é aproximadamente 9,87545×10⁻⁷ neste exemplo. Não é garantia geral de erro menor que atol: para y′=y, com os mesmos parâmetros, o erro global supera atol embora as tentativas aceitas satisfaçam o critério local.

A normalização usa máximo por componente e atols/rtols escalares. Integração só para a frente, sem eventos, rigidez resolvida automaticamente, saída densa, recuperação de trajetória parcial após exceções ou certificação global. Entradas, derivadas, estados, escalas e razões não finitos são diagnosticados. Orçamento ou resolução temporal insuficiente interrompem o cálculo. Não usar atol escalar sem reflexão em estados com unidades diferentes.

Quatro testes: referência Decimal de 70 dígitos por polinômio de estabilidade e erro assintótico; história e custo de todas as tentativas; compatibilidade de API/solver/exemplo e contraexemplo à promessa de erro global; casos de defeito zero, orçamento, resolução temporal e validação. Os testes não substituem revisão conceitual nem cobrem EDOs gerais.


22/10/2026 — Passo adaptativo aprofundado: 14 seções/12 exercícios, fator 15, quinta raiz, erro local/global e diagnóstico opcional de tentativas. Burden 10 §§5.4–5.5 consultados parcialmente; convenções distinguidas e fonte em labs/passo-adaptativo/README.md. 590 testes Python, suíte JS e 333 MathML aprovados; UI desktop/móvel e 0,0002/0,45 conferidos. Computação IV 26 aulas/119 exercícios, 20 introduções curtas, dez grupos parciais. Catálogo 463 aulas/2084 exercícios em rascunho; revisão pessoal pendente. Próxima ação: auditar cobertura/referências de Química IV para butano e ciclos, alternando áreas. Saldo 89%, parada 65%.
