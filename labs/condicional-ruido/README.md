# Observação com ruído — notas de aula

Rascunho original; revisão pessoal pendente. Modelo adimensional conhecido: X,E uniformes independentes em [0,1], Z=X+E. Erro não negativo com média1/2, não instrumento sem viés.

O corte é [max(0,z−1),min(1,z)], e a marginal triangular é seu comprimento. A posterior é uniforme no corte para0<z<2. Sua média éz/2 e variânciaℓ²/12. A informação Z≤b,0<b≤1, dá posterior2(b−x)/b² em[0,b], média b/3 e variância b²/18. Assim z=1/2 dá média1/4, mas a faixa Z≤1/2 dá1/6. Integrais e resoluções detalhadas estão na aula `#aula/pe-condicional-ruido`.

Fontes: Magalhães e Lima, Noções de Probabilidade e Estatística,7ª ed.,§2.2 pp.54–55/PDF69–70: restrição e renormalização. Magalhães, Probabilidade e Variáveis Aleatórias,2ª ed.,§3.2 pp.128–133/PDF69–71: distribuição/densidade condicional; §5.3 pp.260–265/PDF135–137: momentos e esperança iterada. Releitura textual parcial dos recortes paginados em27/10/2026; colunas da PVA intercaladas. Sem nova inspeção visual nem leitura integral. Modelo, transformação, contas, figura e exercícios próprios; PDFs privados não distribuídos.

Executar na raiz: `python3 -m unittest discover -s labs/condicional-ruido -t .`. Usa apenas biblioteca padrão. Entradas int/Fraction, rejeita floats/bools. None nos extremos0,2 e fora do suporte não significa distribuição nula. Faixas gerais e erro com sinal não implementados; não ajusta parâmetros nem processa medições reais.

## 27/10/2026 — condicionamento com ruído aditivo

Adicionada `pe-condicional-ruido`, 12 seções/10 exercícios, após previsão por faixas. Modelo conhecido X,E uniformes independentes em[0,1], Z=X+E. Erro explicitamente não negativo/com viés. Transformação com jacobiano1, suporte variável, evidência triangular e posterior uniforme no corte. Derivados média z/2, variância ℓ²/12 e decomposição1/12=1/24+1/24. Informação Z≤b produz posterior triangular, não a posterior pontual emz=b. Exemplo próprio b=1/2: médias1/6 e1/4. Sem estimação de parâmetros, sensor real ou conclusão causal.

Fontes dos Magalhães: Noções,7ª ed.,§2.2 pp.54–55/PDF69–70; PVA,2ª ed.,§3.2 pp.128–133/PDF69–71 e§5.3 pp.260–265/PDF135–137. Recortes textuais parciais reutilizados; fundamentos de condicionamento/esperança iterada. Nesta sessão reconferida a extração paginada de§3.2 e a regra do produto de Noções. Sem nova inspeção visual, leitura integral ou distribuição dos livros. Deduções, figura, exemplo, código e exercícios próprios.

Verificação:14 testes do catálogo e5 locais aprovados;774 estruturas MathML conferidas. Cortes/momentos confrontados com integrais de Simpson exatas para os polinômios envolvidos; faixas com integração de momentos independente; esperança iterada, variância total, caudas, extremos e contratos. No navegador em390px, exercício da média por faixa rejeitou0,25 e aceitou0,1666666666667 pelo Enter; distinção de independência aceita. Figura inspecionada em`condicional-ruido-mobile.jpg`, largura do documento390px e console sem erros. Leitor de tela, Windows real, experimento e revisão pessoal pendentes.

Probabilidade:24 aulas/299 exercícios em rascunho,14 etapas propostas. Global:51 trilhas,542 aulas/4205 exercícios e206 introduções curtas. Contagens não comprovam cobertura integral ou domínio pessoal. Próxima ação: Jhuann reconstruir os dois suportes e as médias ponto/faixa em20 minutos; depois considerar erro com sinal e diagnóstico de adequação sem confundir modelo conhecido com ajuste a dados. Saldo semanal83%; parada operacional em65% mantida.
