# Conformações: primeiro recorte no etano

21/10/2026. Rascunho original para revisão de Jhuann. Fonte: Brown/Poon, Introduction to Organic Chemistry, sexta edição Wiley2016, §3.6, pp. impressas73–75/PDF93–95. Consulta parcial, página74/PDF94 inspecionada visualmente; o trecho de nomenclatura no começo da página73 não foi usado. Páginas posteriores da seção extraídas para localização, sem alegação de leitura integral ou desenvolvimento de ciclos. PDF privado não distribuído.

Geometria própria: três vetores C–H por carbono com componente axial ±1/3 e raio projetado √(8/9), comprimentos unitários. A ligação C–C é o eixo; produtos escalares entre ligações em cada carbono são −1/3. Os120° projetados diferem do ângulo tetraédrico arccos(−1/3). A figura alonga graficamente raios de trás e separa rótulos para evitar ocultação em eclipsadas; não tem escala molecular. Os seis substituintes são H; identificadores f/t não os tornam diferentes.

φ=0 é eclipsada, cresce anti-horário olhando frente→trás. Frente fixa e trás gira; somar120° permuta os H equivalentes de trás. φ=60 mod120° é alternada. Intermediários também são conformações.

Perfil próprio e hipotético: E=B[1+cos(3θ)]/2, θ em radianos; B escolhido entre0 e18kJ/mol, padrão12. Nenhum valor do painel é apresentado como barreira experimental. B=0 dá perfil plano sem alterar a classificação geométrica. O modelo não calcula distribuição térmica, taxa, trajetória, otimização molecular ou energia eletrônica. Não usar os três mínimos como três estados exaustivos de uma distribuição contínua sem hipóteses adicionais.

## Reproduzir

Na raiz do protótipo:

```sh
python3 labs/conformacoes-newman/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Quatro testes locais: produtos escalares e ângulos em37 orientações; matriz de rotação independente e permutação em25 orientações; potencial em361 ângulos/quatro barreiras com extremos, periodicidade e derivada por diferenças centrais em radianos; perfil plano e domínio. JSON com52 estados para confronto Python/JS de vetores, classificação e perfil. Não é validação química experimental.

Faltam tradução cunha/Newman, butano anti/gauche, ciclos e cadeiras, axial/equatorial, energias com fontes/condições e aplicações integradoras. Estereoquímica CIP/R/S permanece unidade distinta. A aula amplia parcialmente o item conformacional e não conclui QuímicaIV.
