# Reservatório finito e aproximação canônica

Todo com L sítios binários distinguíveis e q excitações, energia qε, ε>0, distribuição uniforme nos C(L,q) estados acessíveis. Parte observada com m sítios fixos. Um padrão com k excitações tem probabilidade C(L−m,q−k)/C(L,q). Agrupar por energia exige degenerescência C(m,k). Não foi definida dinâmica.

Exemplo original preservado: L=11,q=3,m=1, pesos120 e45. Novo recorte no mesmo todo: m=2, complemento9, pesos84/36/36/9. Comparação canônica independente com p=3/11, marginais iguais e conjunta diferente: P_exato(11)=3/55 versus9/121, covariância−12/605, variação total24/605. Igualar marginais não atribui temperatura contínua exata ao complemento pequeno.

## Fonte e proveniência

[David Tong, Statistical Physics §1.3 e início1.3.1](https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S1.html#S1.SS3), até eqs.1.19–1.21, consulta pública parcial em27/10/2026. Fundamentos do peso por contagem, expansão e normalização. Não se reproduzem figuras, textos extensos ou exercícios. A curvatura em termos de C_R, a comparação finita e a prova por produtos finitos são deduções locais, com hipóteses próprias. Não se generalizam automaticamente equivalência de ensembles ou propriedades dinâmicas.

A expansão de entropia pressupõe banho macroscópico suave, controles fixos, T e C_R positivos, com termo quadrático e superiores desprezíveis na faixa relevante. Não diferenciamos diretamente a contagem discreta pequena. No limite combinatório, L cresce, m fica fixo e q/L→p em(0,1). Não foi demonstrado o regime de m proporcional a L.

## Código e verificação

Somente biblioteca padrão, probabilidades Fraction. 1≤L≤4096,0≤q≤L,1≤m≤min(L,8). Extremos q=0,L são permitidos como contagens, sem atribuir β finito. Comparação canônica recebe p e não ajusta uma temperatura. O código não simula banho térmico, trajetória, ergodicidade, correções em um material real ou dados da IC.

Na raiz: `python3 -m unittest discover -s labs/reservatorio-finito -t .`.

Verificações contra enumeração completa de sistemas pequenos, construção independente por sorteios sequenciais sem reposição, marginais, momentos, covariância/variação total e escala com fração global fixa. Não substituem as provas da aula ou a revisão conceitual pessoal.

Próxima revisão de20min: reconstruir as duas contagens sem trocar o todo, somar a degenerescência do nívelε e explicar por que marginais iguais não garantem independência. Depois demonstrar o limite com m fixo. Revisão pessoal, leitor de tela e Windows real pendentes.

Conferência em 27/10/2026: cinco testes locais e 14 de catálogo aprovados; 813 estruturas MathML globais. Interface em 390 px: conjunta rejeitou 9/121 e aceitou 3/55 pelo Enter, limite com m fixo aceito. Figura e texto inspecionados, largura 390 px e console sem erros; captura na raiz `reservatorio-finito-mobile.jpg`.
