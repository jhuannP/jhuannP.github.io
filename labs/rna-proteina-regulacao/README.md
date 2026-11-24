# Regulação pós-transcricional — notas de aula

Rascunho original; revisão pessoal pendente. miRNAs/RISC e distinção entre estabilidade do mRNA e tradução. Não é preditor de alvos ou protocolo executado.

Modelo sintético: dM/dt=α−δM; dP/dt=βM−γP. M em uR, P em uP; α uR/h, δ/γ h⁻¹, β uP/(uR h). Tradução não consome RNA no balanço. M*=α/δ, P*=βM*/γ. P/M só restringe β/γ. Tabela e resoluções na aula `#aula/b2-regulacao-pos-transcricional`.

Fonte: Alberts e colaboradores, Biologia Molecular da Célula, tradução da6ª edição, Artmed2017, cap.7 pp.429–430/PDF465–466. Consulta textual parcial em27/10/2026; sem nova inspeção visual. Fundamentos: regulação por pequenos RNAs, complexo RISC/Argonauta, reconhecimento e destinos diferentes do mRNA. Dados quantitativos de prevalência e figuras não reproduzidos. Exemplo, balanços, números, figura, código e exercícios próprios. PDF privado não distribuído.

Rodar na raiz: `python3 -m unittest discover -s labs/rna-proteina-regulacao -t .`. Biblioteca padrão. Estado estacionário/razões com int/Fraction; transiente de proteína em float com RNA artificialmente constante, sem resolver o sistema geral acoplado. Não fornece garantia de precisão arbitrária, ajusta dados ou implementa cinética de miRNA.

Os parâmetros não são estimados de abundâncias e nenhuma experiência de bancada foi realizada aqui. Crescimento/diluição, transporte, ruído e redes não implementados. Proposta de revisão: reconstruir os dois contraexemplos e indicar uma medida adicional com controles.

## 27/10/2026 — regulação pós-transcricional e observáveis

Nova aula `b2-regulacao-pos-transcricional`:12 seções/12 exercícios, após tradução. Item II.7 passou de lacuna a parcial. miRNAs/RISC e destinos diferentes dos alvos; balanço sintético de RNA e proteína com unidades distintas. Tabela de parâmetros diferentes produz os mesmos M*=5 e P*=10, demonstrando ambiguidade de inferência. Proteína/RNA restringe β/γ, não tradução isolada. Relação com ensaio temporal ideal e controles propostos, sem atividade experimental pessoal ou previsão de alvos.

Fonte: Alberts e colaboradores, Biologia Molecular da Célula, tradução da6ª edição/Artmed2017, cap.7 pp.429–430/PDF465–466, recorte textual parcialmente consultado em27/10/2026. Paginação conferida na extração; sem nova inspeção visual, leitura integral, cópia de figuras ou distribuição do livro. Balanços, dados, contraexemplos, figura, código e exercícios próprios. Versão da turma ainda não comprovada; Júpiter não reaberto nesta sessão.

Verificação:14 testes do catálogo e cinco locais aprovados,778 estruturas MathML conferidas. Laboratório verifica36 balanços estacionários, famílias inversas com observáveis idênticos, razões exatas, transiente de proteína com RNA mantido constante e comparação Euler independente/refinamento, meia-vida e contratos. Um teste inicialmente produzia float por divisão de inteiros; corrigido para Fraction sem afrouxar o contrato. Comparação recusa RNA zero para não apresentar P/M indefinido como observável válido. Sem solução do sistema acoplado geral, ajuste experimental ou modelo cinético de RISC.

No navegador390px, exercício de razão rejeitou0,25 e aceitou0,5 pelo Enter; limite de inferência sobre β/γ aceito. Figura inspecionada e corrigida para setas separadas/legíveis; captura`rna-proteina-regulacao-mobile.jpg`. Documento390px e console sem erros; leitor de tela, Windows real e revisão pessoal não realizados.

BiologiaII:9 aulas/106 exercícios,12 grupos parciais/6 lacunas. Global:51 trilhas,544 aulas/4229 exercícios e206 introduções curtas. Não significa curso completo ou competência pessoal demonstrada. Próxima ação: reconstruir referência/A/B e propor um observável adicional com controles em20min; próximo bloco global, inspecionar uma introdução curta de ComputaçãoIII para aprofundar o percurso numérico. Saldo semanal82%; parada operacional65% mantida.
