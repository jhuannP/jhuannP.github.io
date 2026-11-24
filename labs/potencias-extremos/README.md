# Séries de potências — extremos e cota de erro

S_N(x)=∑ de n=1 a N de xⁿ/n. Raio1, convergência absoluta no interior, condicional em−1 e divergência em1. Identidade finita−ln(1−x)=S_N(x)+∫₀ˣtᴺ/(1−t)dt para−1≤x<1. Cota uniforme em|x|≤r<1: rᴺ⁺¹/[(N+1)(1−r)]. O resto em−1 é alternado e limitado entre1/[2(N+1)] e1/(N+1) em módulo. Provas na aula; testes finitos não as substituem.

## Fontes

Apostol, *Calculus*, VolumeI, 2ª edição,1967. §11.6 pp.428–429/PDF448–449 e§11.8 pp.431–432/PDF451–452, consulta textual parcial em27/10/2026. Cabeçalhos e correspondência impressa/PDF reconferidos na extração; sem nova inspeção visual. Trechos do topo de p.431 são exercícios anteriores e não foram usados/reproduzidos. A série∑xⁿ/n aparece em11.6, Exemplo3; não a apresentamos como escolha inédita. Deduções específicas do resto, escolhas de tolerância, figura, laboratório e exercícios próprios. Sem leitura integral, reprodução de figuras ou distribuição dos PDFs privados.

## Contratos

`partial` e `derivative_partial` calculam polinômios finitos, inclusive fora do intervalo, sem chamar isso de convergência. `uniform_bound` exige0≤r<1; busca compara a cota com uma tolerância positiva, com escolha explícita de desigualdade estrita ou não. A API aceita int/Fraction e rejeita bool/float. N entre0 e512. `first_sufficient` retorna None se não encontrou até512; não é declaração de divergência.

## Verificação

Na raiz: `python3 -m unittest discover -s labs/potencias-extremos -t .`.

Casos racionais de referência, identidade geométrica finita, diferenças sucessivas, comparação com log1p independente, quadratura de Simpson do resto, limites do extremo e alternância das derivadas. Precisão finita explicitada nas comparações com funções transcendentes/quadratura. Sem conclusão geral a partir dos casos testados.

Próxima revisão de20min: separar raio e extremos e obter a cota; depois reconstruir o certificado N=7 e explicar por que a série derivada falha em−1. Teoremas gerais, outros centros, revisão pessoal, leitor de tela e Windows real pendentes.

Conferência em27/10/2026: cinco testes locais e14 do catálogo aprovados;810 estruturas MathML globais. Em390px, certificado N rejeitou6 e aceitou7 pelo Enter; distinção de uniformidade aceita. Figura inspecionada, largura390px e console sem erros; captura na raiz `potencias-extremos-mobile.jpg`.
