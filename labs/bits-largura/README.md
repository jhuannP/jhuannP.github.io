# Bits sem sinal, largura e ordem dos bytes

27/10/2026. Material original com apoio de IA, rascunho para revisão pessoal. Percurso próprio, sem equivalência administrativa ou comprovação de domínio.

## Modelo e provas

Palavra w bits, b_i∈{0,1}, índice 0 à direita mas escrita MSB à esquerda. n=Σb_i2^i. Há 2^w padrões, faixa 0..2^w−1. Divisões n=2q+r extraem bits de baixo peso; após k etapas, n=q_k2^k+Σ_{i<k}r_i2^i. n<2^w dá q_w=0; paridade e indução dão unicidade. Decodificação esquerda→direita v←2v+b preserva valor do prefixo.

00101110=32+8+4+2=46=0x2E. Zeros iniciais alteram largura, não valor. format(300,'08b') devolve nove bits 100101100: largura mínima não valida faixa. Rejeitar 300 em unsigned8 é diferente de wrap/máscara: 300 mod256=44;44,300,556 têm o mesmo resto, perdendo informação. Python int não é automaticamente limitado à palavra M8.

Para M mensagens de largura fixa, 2^w≥M. M=300 exige nove bits; isso não mede entropia/compressibilidade. 300 em 16 bits tem byte alto1 e baixo44, hex01 e2C. big=[01,2C],little=[2C,01]; ler [44,1] como big dá11265. Isso não inverte bits internos nem declara a ordem física do host. Mesmo padrão pode ter interpretação signed/texto/instrução, conforme outro contrato.

## Fontes

Sedgewick/Wayne, Computer Science: An Interdisciplinary Approach, §1.3 pp.67–68/PDF88–89, consulta textual parcial em 27/10/2026. Exemplar ©2017; nome/registro2016 não fixa impressão. Campo 6.1 é ligação temática anterior, sem leitura integral alegada. Não se distribui o PDF privado.

[Python Built-in Types](https://docs.python.org/3/builtins/stdtypes.html#int.to_bytes), documento exibido 3.15.2, consulta parcial em 27/10: operações bit a bit, bit_length, int.to_bytes/from_bytes, faixa e ordem. Nenhum runtime instalado/trocado. Código, provas, números, figura e exercícios próprios; sem reprodução dos exemplos das fontes.

## Código e verificações

`unsigned.py`: encode por divisões, decode por prefixos, wrap por resto explícito, pack16/unpack16 por divisão/base256. Inteiros exatos, bool/float rejeitados, w=1..16. Decode exige 1..16 caracteres ASCII0/1, sem prefixos/espaços. Pack/unpack recebem palavra sem sinal de16bits e exatamente dois bytes; ordem big/little. Não implementa float, texto Unicode, complemento de dois, protocolo de rede ou CPU real.

Da raiz: `python3 -m unittest discover -s labs/bits-largura -t .`. Cinco testes:2046 palavras de larguras1..10 contra format/int e soma ponderada; faixa/máscara/format; todos65536 valores de16bits nas duas ordens contra to_bytes e round-trip; extensão com zeros/capacidade; contratos. Escopo finito verificado não é universalidade de formato externo.

Preservados br1/br2, exemplos, Python, desafio bits8 e painel bitWord. Dez respostas novas:46;256;9;44;1;11265; formato não limita; máscara perde informação; little não inverte bits internos;11111111 sem sinal é255. Resoluções na aula.

Revisão proposta em duas sessões: conversão/invariante/faixa; depois rejeição/máscara e bytes. Pendentes: demais interpretações, formatos externos, precisão real/texto e revisão pessoal.

Conferência da entrega: cinco testes locais e14 do catálogo aprovados;769 fórmulas MathML conferidas. Em390px, br8 rejeitou300 e aceitou11265 pelo Enter; interpretação de perda modular aceita. Painel255 conferido nas interpretações já existentes; figura inspecionada, documento sem transbordamento horizontal e console sem erros. Revisão pessoal, leitor de tela e Windows real pendentes.
