# Potencial químico e mistura ideal

Rascunho original28/10/2026. Fonte privada autorizada: Levine,Physical Chemistry,6ªed2009,§9.5 pp.276–277/PDF294–295 e§9.6 pp.278–279/PDF296–297,consulta textual parcial. P.275/PDF293 consultada para contexto molecular;apenas começo de p.279 para entalpia,não derivação de pressão de vapor. Cabeçalhos impressos/PDF conferidos por extração paginada. Sem nova inspeção visual/leitura integral,cópia de tabelas,exemplos ou figuras;PDF privado não distribuído. Fonte curricular: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0124 ,reaberta28/10,ativação01/01/2025 posterior à turma2024/1,versão ministrada desconhecida.

Modelo binário ideal em uma fase a T,P fixas,componentes distintos não reagentes. Estado de referência é cada componente puro na mesma T,P/fase,sem confundir com gás puro a1bar. Quantidades em mol,R em J/(mol K). h=ΔmixG/(RT) tem unidade mol;não é a grandeza molar adimensional h/n. `muA/muB` são apenas deslocamentos em relação aos potenciais puros,não valores absolutos. Em quantidade zero,retornaNone para potencial do componente ausente;G usa limite xlnx=0. Sem solubilidade real,cinética ou fase não ideal.

Da raiz: `python3 -m unittest discover -s labs/mistura-potencial -t .`; `python3 labs/mistura-potencial/mix.py`.

Quatro testes:fixtures/limites,100composições para Euler/extensividade/simetria,12derivadas por diferenças finitas,81pares de convexidade e contratos. Aritmética flutuante,tolerâncias declaradas;não certifica extremos arbitrários. A adição finita deve comparar energias finais/iniciais,sem congelar μ. Revisão pessoal20min:derive ∂h/∂nA=lnxA e compare a adição de1mol de A a1molA+1molB com a previsão diferencial. Sem experimento ou evidência de domínio pessoal.
