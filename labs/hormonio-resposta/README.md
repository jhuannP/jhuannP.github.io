# Sinal, ocupação e resposta de dois estados

Modelo original reduzido. Constantes prescritas, sem dados experimentais, ajuste para um hormônio real ou interpretação clínica. O exemplo não substitui rede bioquímica completa.

## Contrato do modelo

Concentração livre h≥0 mantida por reservatório; Kd>0 na mesma unidade de concentração; sítios independentes e ligação rápida. Fração ocupada u=h/(Kd+h). A ocupação não é número absoluto de complexos, concentração total ou dose administrada.

O alvo abstrato tem fração ativa x, ativação αu(1−x) e desativação βx. α≥0 e β>0 em tempo⁻¹. O total do alvo é constante e a ligação não é simulada dinamicamente. Não há adaptação, internalização de receptor, depleção de ligante, cooperação ou retroalimentação do alvo.

Equilíbrio x∞=αu/(αu+β); taxa de relaxamento αu+β. Para α>0, máximo=α/(α+β) e concentração de meia-resposta H₅₀=βKd/(α+β). Se α=0, resposta zero para todo h: a função devolve H₅₀=None, porque não há concentração única identificável.

Exemplo com h=Kd=2, em unidades arbitrárias: estado A, α=4 e β=1, dá u=1/2,x∞=2/3,máximo4/5,H₅₀=2/5. Estado B, α=1 e β=4, dá a mesma u e resposta1/9,máximo1/5,H₅₀=8/5. Valores são prescritos, não medidas de tecidos. x não é glicemia ou produção de um órgão.

Sob h constante, x(t)=x∞+(x₀−x∞)exp[−(αu+β)t]. Se h é retirado, o modelo fixa h=0 e decai com β. Multiplicar α e β por10 mantém equilíbrio e meia-resposta, mas acelera o tempo por10. Não infere mecanismo molecular de um ajuste ou garante dinâmica de um receptor real.

## Executar e verificar

Da raiz:

```sh
python3 labs/hormonio-resposta/response.py
python3 -B -m unittest discover -s labs/hormonio-resposta -t .
```

Entradas exatas: int/Fraction, sem floats/booleanos nos parâmetros. Domínios de sinal e taxas explicitamente validados. `transient` converte taxa/tempo representáveis para float e usa expm1 para evitar perda de precisão em resposta inicial pequena. Valores muito próximos ao equilíbrio podem arredondar para ele; não afirmar igualdade física exata em tempo finito.

Cinco testes: marcos racionais;45 combinações para balanço, fronteiras e identidade algébrica; nove cenários para meia-resposta e escala comum das taxas;24 transientes comparados a Decimal65, estacionariedade e escala temporal; contratos inválidos. Testes não são dados biológicos, prova completa de identificação ou validação pedagógica.

## Fontes — 29/10/2026

Nelson e Cox, Princípios de Bioquímica de Lehninger,6ª ed.portuguesa,Artmed2014,original2013. Trechos textuais cap12 p433–434/PDF463–464,§12.2 pp438–440/PDF468–470 e trecho p444/PDF474;§12.3 p453/PDF483, localização textual em p454/PDF484. P439/PDF469 visualmente conferida para sequência de sinalização. Leitura parcial; sem tabelas, números estimados de amplificação, casos clínicos, exercícios ou figuras copiados. A figura local representa o modelo abstrato, não uma cópia da rota β-adrenérgica.

Programa CCM0111 mantém consulta28/10/2026, ativação15/07/2024 e versão efetiva da turma2024/2 não comprovada. Não reaberto neste bloco. Integração metabólica entre órgãos e mecanismos hormonais completos continuam pendentes. Revisão pessoal de Jhuann e uso com aluno pendentes.
