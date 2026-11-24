# Tempo de saída: mesma média não é mesma lei

Notas originais28/10/2026. Pavliotis,Stochastic Processes and Applications,§7.2 pp.238–241/PDF247–250 consultadas parcialmente por texto:tempo de saída,gerador,contorno absorvente e exemplos de uma/duas bordas. Cabeçalhos conferidos diretamente:offset9 neste recorte,não transferido de outros capítulos. A fonte usa gerador d²/dx² no exemplo;nas notas dX=√(2D)dW tem geradorD d²/dx². Sem nova inspeção visual/leitura integral ou distribuição do PDF privado. Segundo momento,contraexemplo discreto,dados,figura e código são deduções próprias.

Convenção do laboratório:intervalo[0,ℓ],ℓ comprimento total. A introdução original preservada usa(−L,L),onde L é meia largura:ℓ=2L e y=x+L. Não confundir os dois símbolos.

Passeio simétrico em m intervalos de tamanho h=ℓ/m,passos±h e tempo determinísticoΔt=h²/(2D). Absorção em0/ℓ;tempo de saída é inteiro de passos×Δt. Não é Browniano amostrado,MonteCarlo ou Euler–Maruyama. Sistema tridiagonal racional resolve primeiro/segundo momentos e chance de sair à direita. Até40intervalos,comprimento/difusão racionais positivos,sem integrações numéricas.

Da raiz: `python3 -m unittest discover -s labs/saida-momentos -t .`; `python3 labs/saida-momentos/moments.py`.

Quatro testes:contraexemplo,171combinações de comprimento/difusão/malha confrontando formas fechadas e recorrências,escala,contratos. Igualdade exata da média neste caso quadrático não certifica trajetórias nem lei de saída. Segundo momento discreto difere do contínuo por−(2/3)Δt m(x). Sem deriva,fronteira refletora no código,horizonte ou estimativa amostral. Revisão pessoal20min:derive m e os contornos;depois explique por que uma malha com2intervalos sai sempre em um passo do centro,mas o Browniano não tem saída determinística.
