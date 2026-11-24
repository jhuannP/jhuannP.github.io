# Seleção e expansão clonal: contagem sintética

Execute `python3 experiment.py`. Na raiz do protótipo: `python3 -m unittest discover -p 'test_*.py'` inclui os quatro testes do laboratório. Não usa rede, dados de pessoas ou dependências adicionais.

Cinco clones, dez células iniciais por clone. A reconhecido pelos clones 1/3; B pelo 2; C pelo 5. Clone 4 não reconhece estes três alvos selecionados. O reconhecimento é hipótese binária fixa. A condição de ativação abstrata resume requisitos sem modelar suas vias. Clones com reconhecimento e condição duplicam a cada divisão permitida; demais ficam constantes.

Exemplo A, g=3, condição presente: [80,10,80,10,10], total 190, acréscimo 140, fração dos reconhecedores 16/19. Sem a condição, o reconhecimento continua mas o total fica em 50. g não é hora, exposição ou dose. Não modela afinidade, maturação, morte, recursos, competição, produção de anticorpos, diferenciação, memória ou eliminação de alvo.

Quatro testes verificam contagens/frações, 42 combinações dos controles, separação reconhecimento/ativação, ausência de geração de linhagem, invariância de escala, composição das divisões e domínio. `reference.json` contém os 42 casos comparados ao JavaScript.

Fontes conferidas em 16/10/2026:

- [Júpiter CCM0221](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0221): consulta direta, ativação 2025, três sistemas possíveis; não confirma execução integral da turma.
- Janeway/Imunobiologia, exemplar local de oitava edição em português já identificado: trechos do capítulo inicial, PDF 29 e 32–35 (incluindo seleção clonal e sinais de ativação), consultados. Não foi declarado livro ou capítulo completo lido. Figuras e enunciados não copiados.
- [Referência pública de Janeway](https://www.ncbi.nlm.nih.gov/books/NBK27090/): localizada pelo índice; acesso direto apresentou verificação. Corresponde a outra edição, não substitui a identificação do exemplar local.

Matriz, valores, desenho, exemplos e código originais com auxílio de IA. Frequências de clones não medem eficácia imune e o interruptor não é mecanismo celular real. O modelo serve para distinguir hipóteses; revisão de Jhuann pendente.
