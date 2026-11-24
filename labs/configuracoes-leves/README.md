# Configurações eletrônicas leves

27/10/2026. Material original com apoio de IA em rascunho; revisão pessoal pendente. Preparação editorial não comprova domínio de Jhuann.

## Modelo e exemplo

N=Z−q, q em unidades da carga elementar positiva. Subníveis 1s,2s,2p,3s,3p para o recorte leve. s tem um orbital/capacidade 2, p três/capacidade 6. Cada orbital admite no máximo ↑↓; ↑↑ no mesmo orbital viola Pauli. Hund favorece maior spin nos orbitais degenerados do recorte, ocupando-os individualmente com spins paralelos antes de pares. O desenho não deriva toda a teoria de correlação/termos espectroscópicos.

O neutro: Z=8,N=8; 1s²2s²2p⁴, [He]2s²2p⁴. Diagrama p [↑↓][↑][↑], dois desemparelhados. [↑↓][↑↓][ ] respeita Pauli mas não o padrão de Hund; [↑↑][↑][↓] viola Pauli, embora ambas as somas sejam quatro. Caixa emparelhada à esquerda é convenção, não orientação única ou função de onda exata.

C 2p²:2 desemparelhados; N 2p³:3; O 2p⁴:2; Ne 2p⁶:0. Na neutro [Ne]3s¹, Mg [Ne]3s², Ar [Ne]3s²3p⁶. Na⁺,Mg²⁺,F⁻,O²⁻ e Ne compartilham 10 elétrons/configuração, mas não núcleo, carga, energia ou raio. Remover 3s neste caso não é regra para íons de transição.

Setas representam estados de spin, não giro clássico. Dois desemparelhados paralelos representam projeção máxima S_z=1 em unidades ℏ nesse esquema; não demonstram magnetização permanente da amostra. Sem energias, raios, estabilidade, resposta térmica ou configurações de átomos pesados. Periodicidade continua uma lacuna própria.

## Fonte

Atkins/Jones/Laverman, Princípios de Química, 7ª ed., Bookman 2018, Tópico 1E §§1E.1–1E.2 pp.42–46/PDF174–178, consulta parcial em 27/10/2026; p.45/PDF177 inspecionada visualmente para Pauli/Hund. Edição diferente da 3ª citada pelo Júpiter; não transportar paginação entre elas. Exemplos, diagramas, figura e exercícios próprios; sem reprodução de problemas, leitura integral ou distribuição do PDF. Programa curricular não reaberto neste bloco.

## Código e verificações

`electrons.py`: Z inteiro de 1 a 18, q inteiro e N=Z−q de 0 a 18; bool/float rejeitados. Retorna ocupações representantes e auxiliares de contagem/desemparelhados. Aceitar uma carga formal na aritmética não demonstra existência ou estabilidade de um íon isolado. Não resolve Hamiltoniano ou atribui energias. Caixas internas têm ordem convencional e não impõem eixos físicos únicos.

Da raiz: `python3 -m unittest discover -s labs/configuracoes-leves -t .`. Cinco testes: oito configurações de referência; 342 contagens formais com conservação/capacidades; enumeração independente dos 64 padrões binários dos seis spin-orbitais p e máximo de projeção de spin por N; espécies isoeletrônicas; contratos. Estados binários já codificam Pauli, não verificam energia real de átomos. Configurações de referência e padrões leves são exemplos, não catálogo universal.

Respostas dos 12 exercícios:8;10;10;6;4;2;3;18; ↑↑ viola Pauli; dois pares respeitam Pauli mas não Hund fundamental; isoeletrônico não significa mesma espécie; código não calcula estabilidade. Resoluções completas na aula.

Revisão proposta em duas sessões: O e diagramas permitidos/preferidos; depois íons e limites. Pendentes: periodicidade, energias, transição 3d/4s, configurações pesadas, termos espectroscópicos e revisão pessoal.

Conferência da entrega: cinco testes locais e 14 do catálogo aprovados; 762 fórmulas MathML conferidas. Em 390 px, desemparelhados rejeitou 0 e aceitou 2 pelo Enter; diferença Pauli/Hund aceita. Figura inspecionada, sem transbordamento horizontal ou erros de console. Revisão pessoal, leitor de tela e Windows real pendentes.
