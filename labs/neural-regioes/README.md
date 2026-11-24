# Mapa de origem regional do encéfalo

Material original preparado com IA, revisão de Jhuann pendente. Não experimento de embriologia, simulação temporal ou domínio pessoal certificado.

## Contrato das relações

O mapa começa no tubo **rostral**. `ancestry` segue correspondências regionais selecionadas: três categorias primárias, cinco secundárias e nove exemplos adultos. Não são árvores de genealogia de células, migração, conectividade por axônios ou descrição de funções. Medula, retina, crista e todas as outras estruturas não listadas ficam fora do código, não fora da biologia.

Mesencéfalo primário e secundário são IDs diferentes para distinguir o nível da classificação, conservando o nome anatômico. Telencéfalo conta como uma categoria, sem contar novamente os hemisférios. Os espaços são outra relação: laterais, terceiro, aqueduto e quarto são quatro **rótulos**, não uma nova contagem de regiões ou de todas as cavidades físicas. Metencéfalo e mielencéfalo apontam ao mesmo rótulo quarto ventrículo; a união elimina duplicação do rótulo.

Uma consulta sem espaço atribuído (por exemplo ao córtex) só significa que o catálogo não fez essa associação naquele nível. Não demonstra ausência de relação anatômica com ventrículos. IDs desconhecidos ou de tipo errado geram ValueError. Sem medidas, unidades, pesos de arestas, probabilidade ou mecanismo dinâmico inventados.

## Atividade

Da raiz:

    python3 -B labs/neural-regioes/regions.py
    python3 -B -m unittest discover -s labs/neural-regioes -t .

Reconstrua cerebelo←metencéfalo←rombencéfalo. Compare bulbo raquidiano e olfatório. Explique o que uma seta NÃO demonstra e por que dois links podem referir-se ao mesmo quarto ventrículo.

Cinco métodos de teste: nove caminhos contra tabela literal independente; níveis e ausência de ciclos nas18 regiões; quatro rótulos de cavidades e deduplicação; nomes semelhantes/limite semântico das consultas; tipos/IDs fora do mapa. São verificações de consistência de dados bibliográficos, não confirmação experimental das relações ou teste de uma hipótese de linhagem.

## Fontes e limites

Bear, Connors e Paradiso, *Neurociências: Desvendando o Sistema Nervoso*,4ª edição brasileira2017,cap7. Recortes textuais pp.193–196 e199–200/PDF235–238 e241–242 consultados parcialmente29/10/2026; p.195/PDF237 visualmente conferida para categorias primárias e orientação. Sem figura, exercício ou capítulo reproduzido. Figura e tabela de exemplos são seleção própria, não digitalização da fonte.

A frase abrangente sobre todos os neurônios periféricos não foi adotada como regra: placódios também contribuem em estruturas sensoriais cranianas. Apoio complementar: resumo indexado de *Making a head: Neural crest and ectodermal placodes in cranial sensory development* (2022), DOI10.1016/j.semcdb.2022.06.009. Abertura PubMed não trouxe corpo; PMC pediu verificação. Consulta ao resumo indexado, sem artigo integral, métodos ou figuras lidos.
https://doi.org/10.1016/j.semcdb.2022.06.009

Programa CCM0221 mantém consulta anterior28/10/2026,ativação01/01/2025 e lista de sistemas possíveis; seleção da turma não comprovada. Neurulação molecular, migração, diferenciação visual, retina, regeneração e evolução do desenvolvimento continuam pendentes. Sem diagnóstico, intervenção ou aconselhamento clínico; documentos privados não distribuídos.
