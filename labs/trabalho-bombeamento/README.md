# Trabalho de bombeamento — notas de aula

Novo recorte original das aplicações de integração; rascunho para revisão pessoal. ConeH4/raio2, coordenaday desde vértice, saída6m,ρ1000kg/m³,g10m/s². Fluido uniforme, pressão atmosférica, sem perdas/energia cinética/tubulação. Não calcula bomba real ou consumo elétrico.

Fonte:Apostol, CalculusI,2ª edição1967,§2.14 pp.115–116/PDF135–136, consulta textual parcial em27/10/2026: trabalho por força variável, aditividade e relação integral/Teorema2.8. Não houve nova inspeção visual ou leitura integral. Bombeamento não foi atribuído a essas páginas como exercício; geometria/números/figura e contas próprios. PDF privado não distribuído.

ÁreaA=πy²/4; peso10000A dy; elevação6−y. W=160000π J, volume16π/3m³ e centro3m. Ao drenar até superfície2m,W=130000π J. Fatores deπ representados por Fraction. Soma de fatias é balanço de energia entre estados, não hipótese de partículas imóveis. Unidades e limites completos na aula `#aula/c1-trabalho-bombeamento`.

Rodar na raiz:`python3 -m unittest discover -s labs/trabalho-bombeamento -t .`. Biblioteca padrão,int/Fraction. Cone r=cy e saída acima do tanque; sem densidade variável, vazão, pressão de linha, franja dinâmica ou rendimento. Riemann implementado apenas para o exemplo e sua monotonicidade, com1≤n≤4096. Campos work_pi/volume_pi/peso expressam fatores deπ, não os valores físicos semπ. Não confundir estimativa de quadratura com incerteza física.

## 27/10/2026 — trabalho por fatias e bombeamento

Nova `c1-trabalho-bombeamento`,12 seções/12 exercícios: área por semelhança, volume/massa/peso, distância até saída e trabalho ideal. ConeH4/raio2, saída6m,ρ1000 e g10: W=160000πJ, centro3m e drenagem até2m com130000πJ. Somas de Riemann inferior/superior, energia inicial/final, limites da potência/consumo e rigor de unidades. Pressão atmosférica e perdas/energia cinética desprezadas, sem projeto de equipamento. Fatias não pressupõem moléculas imóveis durante drenagem. Modelo/figura/números próprios.

Fonte: ApostolI,2ª ed.1967,§2.14 pp.115–116/PDF135–136, consulta textual parcial em27/10/2026. Propriedades de trabalho e Teorema2.8 sobre integral; sem nova inspeção visual, leitura integral ou distribuição do PDF privado. Bombeamento não atribuído como exercício dessas páginas. Júpiter não reaberto, versão da turma permanece pendente. Não havia introduções≤3 seções em CálculoI; bloco preenche uma insuficiência temática explicitada no mapa em aplicações, sem declarar conclusão.

Verificação:14 testes do catálogo e cinco locais aprovados;799 estruturas MathML conferidas. Referência/volume/centro/parte removida,24 integrais cúbicas confrontadas por Simpson independente,33 cortes com aditividade/energia, limites de Riemann e refinamento, escala de comprimento/peso e contratos. Frações exatas para fatores deπ; não é solver hidráulico ou quantificação de incerteza física. No navegador390px, drenagem parcial rejeitou80000 e aceitou130000 no fator deπ pelo Enter; altura metade não significar volume metade aceito. Figura/cotas inspecionadas em`trabalho-bombeamento-mobile.jpg`; documento390px, console sem erros. Sem experimento pessoal, leitor de tela, Windows real ou revisão pessoal.

CálculoI26 aulas/258 exercícios, dez grupos curriculares ainda parciais. Global51 trilhas,547 aulas/4335 exercícios e199 introduções curtas. Nenhum curso completo ou domínio pessoal certificado. Próxima ação: montar dW e reconstruir centro3m/trabalho160000π em20min. Próximo bloco global: inspecionar introdução de ComputaçãoII e a referência disponível. Saldo semanal80%; parada operacional65% mantida.
