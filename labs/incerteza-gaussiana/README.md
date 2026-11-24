# Incerteza e fase espacial de um gaussiano

27/10/2026. Notas originais assistidas por IA,em rascunho para revisão pessoal. Relação de preparação/variâncias,não calibração de aparelho ou resultado experimental.

Na reta,ψ=(2πs²)^(−1/4)exp[−(x−x₀)²/(4s²)]exp(ip₀x/ℏ),s>0. Densidade normalizada com média x₀ e desvio s. Derivar dá(p−p₀)ψ=iℏ(x−x₀)ψ/(2s²),logoΔp=ℏ/(2s). Produto mínimoℏ/2. Exemplo originalℏ1,s2 dáΔp1/4. A prova geral no recorte suave usa Cauchy–Schwarz,comutador[x,p]=iℏ e hipóteses de domínio/decaimento; não é manipulação válida em estados arbitrários sem momentos finitos.

Para x₀0,acrescente exp[iκx²/(4s²)]. A posição mantém a mesma densidade,enquanto(p−p₀)ψ=ℏ(κ+i)xψ/(2s²) e variância de momentoℏ²(1+κ²)/(4s²). Produto(ℏ/2)√(1+κ²). Um gaussiano com fase quadrática não precisa minimizar o produto simples. Isso impede atribuir igualdade a toda distribuição que tenha uma envoltória gaussiana.

## Fontes parcialmente consultadas

Nussenzveig,Curso de Física Básica vol.4,2ª ed.,§8.10 pp.259–262/PDF260–263,flutuação,variância e comutador. Consulta textual parcial em27/10/2026;PDF contado a partir de1. OCR de fórmulas imperfeito;derivações desta aula reconstruídas e conferidas separadamente. Sem leitura integral,nova inspeção visual ou reprodução de figuras/exercícios.

[OpenStax University Physics vol.3 §7.2](https://openstax.org/books/university-physics-volume-3/pages/7-2-the-heisenberg-uncertainty-principle),recortes sobre desvios,cota e pacote gaussiano. Não adotados seus exemplos numéricos/estimativas de átomos ou formulações simplificadas como“se um desvio é grande,o outro é pequeno”sem ressalva: a desigualdade fornece cota,não o valor real. Energia-tempo não desenvolvida aqui. Família com fase quadrática,figura,contas e código próprios. Júpiter não reaberto;limites curriculares de FISICA_4.md mantidos.

## Laboratório

Execute `python3 labs/incerteza-gaussiana/gaussian.py`. Usaℏ1,x₀0 e12 combinações de s(.5,1,2),κ(0,1),p₀(0,.75). Quadratura Simpson em[−8s,8s],512 subintervalos;momento por derivada central com passos0,02s/0,01s/0,005s. Calcula norma,média/variância de posição,média de momento e∫|pψ|²−⟨p⟩². Expressões analíticas são referência independente da derivada numérica.

Quatro testes:normalização/posição e parte imaginária residual da média de momento;refinamento de momentos nos12 casos;invariância da densidade sob fase e exemplos mínimo/não mínimo;contratos. Máximos resíduos de média/variância de momento:5,1241×10⁻⁴;1,2812×10⁻⁴;3,2031×10⁻⁵,aproximadamente quatro vezes menores ao reduzir o passo pela metade. Não são cotas globais ou erros de uma experiência.

Produtos numéricos no exemplo s2:0,4999984375 e0,7071023618,comparados a0,5 e√2/2. O primeiro fica ligeiramente abaixo da cota por discretização;isso não é violação física. A amplitude é avaliada analiticamente também nos pontos de diferença fora do intervalo de quadratura,sem condição artificial de parede. A janela finita não altera o domínio matemático do estado.

Próxima ação de20min:derivar a norma centrada de momento,explicar1/4 e o fator√(1+κ²),distinguindo desvio de erro instrumental. Evolução temporal,medidas conjuntas e domínios gerais de operadores permanecem pendentes. Python opcional;revisão de Jhuann pendente.
