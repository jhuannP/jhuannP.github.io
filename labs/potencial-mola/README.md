# Potencial da mola e escolha do zero

Rascunho original de 22/10/2026, revisão pessoal pendente. Aprofunda `f1-energia`, preservando IDs, exemplo e desafio harmônico anteriores. Quatorze seções e doze exercícios. Não é experimento ou evidência de pesquisa pessoal.

## Fonte consultada parcialmente

Nussenzveig, *Curso de Física Básica 1 — Mecânica*, 5ª edição, Blucher 2013, reimpressão 2017: §§6.5–6.6, pp.150–157 (PDF151–158), leitura parcial sobre força/potencial, acessibilidade e oscilador; §7.3, pp.166–167 (PDF167–168), força conservativa e zero arbitrário; início de §7.4 p.169 (PDF170), relação força/derivada. Trechos locais autorizados, não leitura integral. Exemplos, perguntas e implementação próprios; nenhuma página ou imagem do livro incluída.

## Modelo e contrato

Mola horizontal ideal, m=2 kg, k=8 N/m, amplitude 1 m, sem dissipação. U=4x²+C, E=4+C, K=4−4x² quando não negativo, F=−8x. Para m=2 kg, |v|=√K nas unidades SI fixadas; a forma geral é √(2K/m). Zero deslocado simultaneamente em E e U; não modifica forças ou movimento. O painel não determina sinal de v ou tempo. Retorno x=±1 m tem v=0 e F diferente de zero; equilíbrio x=0 tem F=0 e rapidez máxima nesta órbita.

Posição candidata q em centésimos de metro, inteiro −150..150; C inteiro −10..10 J. Fora de [−1,1] m, diferença E−U é negativa e não representa K física; K e rapidez retornam None/null. O potencial e sua força continuam definidos como funções, sem que a posição seja alcançada pela órbita selecionada.

## Visual e testes

Tese: duas curvas sobre o mesmo eixo fixo separam potencial, energia e diferença; tabela dá valores e unidades. Conteúdo: posição candidata, zero, gráfico, tabela e limite físico. Interação: teclado altera posição ou zero; o relatório distingue ponto permitido, retorno e região proibida. Sem trajetória ou animação que sugira atravessar região proibida. Escala vertical fixa −10..20 J; horizontal −1,5..1,5 m.

Quatro testes: integral exata da força linear por trapézios e invariância em 1281 estados; extremos/energia negativa; energia ao longo da solução independente de Newton em 201 tempos; contratos. Referências JS: 39 estados racionais por trabalho e 6321 mudanças de zero preservando força, rapidez e permissão. Biblioteca padrão apenas.

Execute: `python3 -m unittest discover -s labs/potencial-mola -t .`, `node test_simulations.cjs`, `node test_math.cjs` na raiz do protótipo.

Próxima revisão pessoal: explicar por que E=−6 J pode permitir movimento e por que v=0 no retorno não implica equilíbrio. Pendentes: barreiras, múltiplos poços, dissipação e potenciais dependentes do tempo; este recorte não encerra energia ou Física I.

Verificação final: 712 testes Python, suíte JS com 268 modelos/804 cenários básicos e comparações adicionais, 414 MathML e catálogo aprovados. Casos C=−10/x=0, x=1,5 proibido e x=1 retorno conferidos no navegador; resposta −2,25 aceita. 390px sem overflow observado, console sem erros, prévia `potencial-mola-mobile.jpg` na raiz. Saldo77%; parada65%.
