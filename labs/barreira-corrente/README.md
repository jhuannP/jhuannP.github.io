# Barreira retangular: amplitudes e correntes

Rascunho original, 12 seções/12 exercícios em `f4-tunelamento`. Partícula não relativística 1D, massa constante, potencial real, 0<E<V₀ e incidência da esquerda. T é probabilidade/razão de fluxos; t é amplitude complexa. A notação das fontes pode diferir.

A derivação casa ψ e ψ′ nas duas bordas, elimina a reflexão e calcula o módulo da amplitude. Uma única exponencial interna não permite em geral casar a barreira finita; a componente crescente não é descartada por condição em infinito inexistente nessa região. Componentes evanescentes combinadas podem transportar corrente, sem perda de energia.

## Fontes e limites

Nussenzveig vol.4, 2ª ed.2014/digital2018, §10.4: pp.306–307/PDF307–308, modelo/contorno; pp.310–311/PDF311–312, região evanescente e aproximação espessa. Consulta textual parcial em27/10/2026, OCR de fórmulas imperfeito, sem nova inspeção visual ou leitura integral. A álgebra foi reconstruída com convenção de fases própria.

[OpenStax University Physics3 §7.6](https://openstax.org/books/university-physics-volume-3/pages/7-6-the-quantum-tunneling-of-particles-through-potential-barriers), início sobre modelo e condições de contorno parcialmente consultado em27/10/2026; não se copiaram figura ou problemas. Não adotamos a descrição de tunelamento como violação de conservação de energia. Programa oficial não reaberto; versão da turma mantém as limitações já registradas.

## Laboratório

```sh
python3 labs/barreira-corrente/barrier.py
```

Usa e=E/V₀ e z=κa. Contrato numérico: 10⁻⁶≤e≤1−10⁻⁶, 0≤z≤20; casamento linear direto limitado a z≤5 para evitar regime mal condicionado. Essas faixas são computacionais, não fronteiras físicas. O sistema linear usa V₀=1 e 2m=ℏ=1, com quatro amplitudes complexas e eliminação com pivô parcial. Não importa bibliotecas externas.

Cinco testes: 25 comparações independentes entre casamento e fórmula, conservação R+T; continuidade e corrente interna em12 parâmetros/quatro pontos; caso simétrico e erro assintótico; largura zero/monotonicidade; contratos. Não confundir grade finita com prova geral. T≈0,4199743416 para e=1/2,z=1, versus exp(−2)≈0,1353352832 e 4exp(−2)≈0,5413411329. Em z=3, erro relativo do prefator ≈0,00496365.

Revisão em duas sessões de20min: derivar t/T a partir do contorno; comparar as aproximações. Outros potenciais, pacotes, tempos, testes experimentais, estados acima da barreira e relatividade pendentes. Revisão pessoal ainda não realizada.


## 27/10/2026 — barreira: contorno, amplitudes e corrente

`f4-tunelamento` ampliada de3 seções/2 exercícios para12/12, preservando IDs, exemplo κ=2, Python inicial e desafio. Modelo estacionário1D real, massa constante e regiões externas iguais. Quatro condições de continuidade determinam r,C,D,t; derivação própria com fase transmitida referida à borda direita. T=|t|² por razão de correntes; duas exponenciais internas e corrente de termos cruzados. Exato versus limite espesso com prefator, limites de largura e restrições computacionais. Não implica absorção/perda de energia, trajetória de energia cinética negativa ou extensão relativística.

Fontes textuais parciais em27/10/2026: Nussenzveig4 §10.4 pp.306–307/PDF307–308 e pp.310–311/PDF311–312. OCR de fórmulas imperfeito; álgebra reconstruída, sem nova inspeção visual ou leitura integral. OpenStaxUP3§7.6 https://openstax.org/books/university-physics-volume-3/pages/7-6-the-quantum-tunneling-of-particles-through-potential-barriers , início sobre modelo/contorno. Notação t amplitude/T probabilidade declarada, distinta da convenção de algumas fontes. Figura, exercícios e código próprios; programa não reaberto.

Cinco testes de `labs/barreira-corrente/barrier.py` aprovados:25 comparações de sistema linear independente versus expressão fechada, R+T, condições nas bordas/corrente interna em12 parâmetros/quatro pontos, simetria e erro assintótico, limites/monotonicidade e contratos. Fórmula usa10⁻⁶≤E/V₀≤1−10⁻⁶,0≤κa≤20; sistema direto limitado aκa≤5 por condicionamento. Em e=1/2,z=1:T0,419974341614, exponencial0,135335283237, prefator0,541341132946; em z=3 erro relativo do prefator0,004963648566. Testes finitos não substituem a derivação.14 testes do catálogo e862 estruturas MathML aprovados. Navegador390px rejeitou0,135335 e aceitou0,419974;documento390/390px, console sem erros observados. Figura inspecionada em `barreira-corrente-mobile.jpg`; viewport restaurada. Windows real, leitor de tela e revisão pessoal pendentes.

FísicaIV18 aulas/193 exercícios, duas introduções curtas,18 grupos parciais/oito lacunas, nenhum completo. Global51 trilhas/574 aulas/5246 exercícios,143 introduções curtas. Próxima ação:duas sessões de20min para reconstruir contorno/T e comparar os regimes. Próxima elaboração global:conferir uma lacuna curricular de BiologiaIII ou IV, com fonte, alternando áreas. Saldo semanal antes/depois67%;parada operacional65% preservada.
