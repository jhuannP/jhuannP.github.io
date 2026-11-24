# Transporte e energia eletroquímica

Rascunho para revisão pessoal. Pergunta: uma concentração interna maior impede entrada passiva? Use soluções ideais diluídas, mesma espécie/estado padrão, mesma temperatura e pressão hidrostática; potenciais e concentrações são reservatórios prescritos. Sem cinética, balanço de cargas de uma célula fechada ou experiência de bancada.

Para fora→dentro: Δμ=RT ln(c_i/c_o)+zF(V_i−V_o). `affinity` retorna Δμ/(RT), adimensional. Concentrações devem estar na mesma unidade, positivas; ψ=FΔV/(RT), z inteiro com |z|≤8. Rótulos entrada/saída exigem via passiva permeável; energia favorável não fixa taxa. Valores muito perto de zero exigem tolerância, sem interpretação automática de ruído de ponto flutuante. Logaritmos separados evitam formar uma razão numérica com overflow. Não há correção de atividades não ideais.

Exemplo original: c_i/c_o=8, ψ=−ln16. z=+1 dá −ln2 (entrada), z=−1 dá 7ln2 (saída). ψ=−ln8 e z=+1 dá zero termodinâmico. Não são concentrações/potenciais de tecido real. A figura usa energia em RT ln2, não velocidade.

`coupled` soma energia de um soluto-alvo e n íons motores por ciclo acoplado ideal: n inteiro 1..100. Alvo 2ln2 e motor −ln2 dão zero para n=2 e −ln2 para n=3. Zero é limite reversível, não prova transporte a taxa finita; energia negativa é condição termodinâmica, não comprovação de mecanismo, acoplamento obrigatório ou velocidade. Não se inventa uma bomba biológica com esta conta.

## Fontes efetivamente consultadas em 29/10/2026

Nelson/Cox, Princípios de Bioquímica de Lehninger, 6ª edição portuguesa Artmed2014 (original2013), cap11 §11.3: recortes textuais pp.403–404 e409–410/PDF433–434 e439–440; p410/PDF440 também inspecionada visualmente para Eq11-4, carga e diferença de potencial. Edição diferente da oitava oficial; fonte privada não distribuída. Não copiar problemas resolvidos, figura ou código. O mapa CCM0121 mantém consulta oficial29/10/2026, ativação01/01/2025, versão ministrada não comprovada; não foi reaberto neste bloco.

Busca NCBI/Alberts4 (2002), Principles of Membrane Transport: apenas trecho indexado; abertura direta devolveu verificação de navegador. Não alegamos leitura do corpo. O desenvolvimento usa os recortes privados acima e dedução própria. Não foi necessário contornar acesso.

## Verificação

Na raiz do protótipo:

```sh
python3 -B -m unittest discover -s labs/transporte-eletroquimico -t .
python3 labs/transporte-eletroquimico/energy.py
```

Cinco métodos:60 combinações contra logaritmo Decimal70 independente; três marcos e28 estados de equilíbrio; reversão e nove reescalas mais extremo numérico;48 ciclos por soma de eventos independente; contratos. Esses testes sustentam contas do modelo, sem certificar fisiologia real ou revisão pessoal. Experimento e cinética de canais, saturação de carreadores, bombas e atividades reais permanecem pendentes.
