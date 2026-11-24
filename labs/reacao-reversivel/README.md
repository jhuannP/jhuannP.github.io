# Reação reversível — notas de aula

Rascunho original; revisão pessoal pendente. Sistema homogêneo fechado A⇌B1:1, T e volume constantes, leis de primeira ordem. Taxas em mol L⁻¹ s⁻¹; constantes s⁻¹.

Derivação completa na aula `#aula/q2-reacao-reversivel`: conservação A+B=C; Aeq=C kb/(kf+kb); A=Aeq+(A0−Aeq)exp[−(kf+kb)t]. Equilíbrio dinâmico exige taxas iguais, não nulas. A meia-vida do desvio ln2/(kf+kb) não implica A=A0/2.

Fonte: Levine, Physical Chemistry,6ª ed.,2009,§16.3 p.524/PDF542, eqs.16.31–16.34. Consulta textual parcial em27/10/2026, extração com avisos de fontes já registrados; sem nova inspeção visual. A fonte nomeia produto C; aqui B. Modelo, exemplo numérico, figura, laboratório e exercícios próprios. PDF privado não distribuído. A conexão Q/K ideal foi derivada explicitamente das hipóteses, não apresentada como regra de mecanismo geral.

Executar na raiz: `python3 -m unittest discover -s labs/reacao-reversivel -t .`. Biblioteca padrão; solução analítica float, sem ajuste experimental ou garantia universal de erro numérico. Constantes estritamente positivas, inventário positivo, concentrações/tempo não negativos. Comparação RK4 independente nos testes. O exemplo de acelerar ambas as constantes por5 é um modelo de comparação, não garantia de fator comum para qualquer catalisador real.

## 27/10/2026 — reação reversível e relaxação

Nova aula `q2-reacao-reversivel`, 12 seções/12 exercícios próprios: sistema A⇌B1:1 homogêneo fechado, T/V constantes e primeira ordem nas duas direções assumida. Inventário, solução, equilíbrio dinâmico, meia-vida do desvio, tolerância e comparação de constantes escaladas. Relação K=kf/kb limitada ao mecanismo ideal declarado. Exemplo sintético kf=0,30 e kb=0,10s⁻¹; Aeq=0,25, Beq=0,75mol/L. Na meia-vida do desvio A=0,625, não0,50mol/L. Conexão algébrica de Q/K com sentido líquido separada de qualquer cálculo de Gibbs total no recipiente de volume fixo.

Fonte: Levine6,2009,§16.3 p.524/PDF542, equações16.31–16.34, consulta textual parcial nesta sessão. Fonte nomeia produto C, nosso B. Sem nova inspeção visual, leitura integral, reabertura do Júpiter ou distribuição de material privado. Versão da turma continua não recuperada. Figura, exemplo, código e questões originais.

Verificação:14 testes do catálogo e cinco do laboratório aprovados;776 estruturas MathML conferidas. Testes: referência/taxas não nulas, inventário/PVI/derivada em múltiplos estados, RK4 independente com refinamento, mudança de escala, tolerância, sinal Q/K e contratos. No navegador390px, exercício da meia-vida rejeitou0,5 e aceitou0,625 pelo Enter; equilíbrio com taxas iguais não nulas aceito. Figura inspecionada em`reacao-reversivel-mobile.jpg`; documento390px, console sem erros. Sem experimento, leitor de tela, Windows real ou revisão pessoal.

Estado: QuímicaII12 aulas/142 exercícios,15 grupos ainda parciais. Catálogo51 trilhas,543 aulas/4217 exercícios e206 introduções curtas. Nada declarado completo ou como domínio pessoal demonstrado. Próxima ação: reconstruir balanço e meia-vida do desvio em20min; próximo bloco global, inspecionar lacuna curricular de BiologiaII para preservar equilíbrio do escopo. Saldo semanal82%; parada operacional65% mantida.
