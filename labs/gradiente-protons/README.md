# Respiração, prótons e energia livre

Material didático original preparado com apoio de IA em 28/10/2026. Revisão pessoal pendente. Conecta compartimentos, reações redox e termodinâmica; não é experimento, modelo cinético ou resultado de IC.

## Da cadeia à membrana

No recorte mitocondrial, NADH da matriz doa elétrons ao complexo I; ubiquinona/Q liga essa entrada ao complexo III, citocromo c conecta III a IV e IV transfere elétrons ao O₂, formando água. Complexo II fornece outra entrada em Q, por exemplo a partir de succinato, sem bombear prótons. Não existe uma sequência obrigatória I→II→III→IV. I, III e IV contribuem para translocar H⁺ da matriz N ao espaço intermembrana P.

O retorno de H⁺ por ATP-sintase pode ser acoplado à síntese de ATP a partir de ADP e fosfato. Elétrons, prótons e ATP não são uma mesma espécie que muda de nome. Há prótons consumidos quimicamente na formação de água e prótons translocados; não confundir esses inventários. O₂ é o aceptor terminal neste recorte, sem ser reagente direto de cada etapa de Krebs.

## Convenção de sinais

Defina Δψ=ψ_N−ψ_P e ΔpH=pH_N−pH_P. Para transferir **um mol de H⁺ de P para N**, com mesma temperatura e estado padrão aquoso compatível, a mudança de potencial eletroquímico é

Δμ = RT ln(a_N/a_P)+F(ψ_N−ψ_P) = −RT ln(10) ΔpH+FΔψ.

a representa atividade adimensional de H⁺; pH=−log₁₀a. Em solução ideal diluída pode-se aproximar atividade por concentração normalizada, mas o cálculo usa diretamente os pHs dados. A carga do próton é positiva. R em J/(mol K), T em K, F em C/mol e ψ em V dão J/mol de H⁺. Um Δμ negativo favorece a direção P→N; o bombeamento reverso custa −Δμ nas mesmas condições. Isso não fornece uma vazão ou taxa.

## Exemplo sintético e acoplamento hipotético

Fixe pH_P=7, pH_N=8, ψ_P=0 V, ψ_N=−0,15 V e T=300 K. R=8,314 e F=96485 são constantes arredondadas para este exemplo. A contribuição química é aproximadamente −5,743 kJ/mol H⁺; a elétrica, −14,473; o total, −20,216 kJ/mol H⁺. Os números são escolhidos para o exercício, sem inferir valores de uma célula medida.

Suponha **apenas para um ciclo didático** que m prótons retornem por ATP formado e que ΔG de síntese seja +50 kJ/mol ATP nas condições escolhidas. Então ΔG_ciclo=50+mΔμ (em kJ/mol ATP). Para m=2, o resultado é positivo; para m=3, negativo. Essa comparação não mede a estequiometria da ATP-sintase, não soma custos de transporte de ADP/fosfato e não prevê ATP por NADH. É uma condição energética necessária sob o acoplamento imposto, não uma garantia de catálise, conversão completa ou velocidade. Vazamentos e outros fluxos podem dissipar energia; membrana com gradiente e ATP-sintase não implicam síntese irrestrita.

## Executar e verificar

```sh
python3 energy.py
python3 -m unittest test_energy.py
```

Python padrão. `transfer` retorna parcelas química/elétrica/total em J/mol H⁺, sem exponenciar os pHs. `coupled` trata apenas o ciclo hipotético com m inteiro positivo e energia de síntese positiva. Valores não finitos, bool, texto e temperatura não positiva são rejeitados. Não há simulação de cadeia, montagem molecular, transporte, taxa ou integração temporal.

Quatro testes: 243 casos comparados à expressão independente pela razão de atividades; reversão, aditividade e deslocamento comum de potencial em 27 trios de estados; contribuições e ciclos; contratos. Deslocar ψ_N e ψ_P pela mesma constante não muda o trabalho, pois só a diferença entra. Somar potenciais ou omitir o sinal da carga produziria resultado incorreto.

## Fontes e alcance

Nelson/Cox, *Princípios de Bioquímica de Lehninger*, 6ª ed., Artmed 2014 (original 2013), exemplar autorizado. Consulta textual parcial e inspeção visual em 28/10/2026: §19.1 p.744/PDF774, fluxo entre complexos e componentes da força próton-motriz; §19.2 p.748/PDF778, acoplamento quimiosmótico. P.747/PDF777 e p.743/PDF773 consultadas textualmente para localização/contexto. Não houve leitura integral das seções; figuras/tabelas do livro não foram copiadas nem o PDF distribuído. A convenção de origem/destino foi definida explicitamente nestas notas; não se transplanta o sinal de Δψ sem comparar definições.

O programa CCM0111 anteriormente registrado tem ativação em 2024; versão ministrada e tentativa de 2023 não comprovadas. Não foi reaberto neste bloco. O item respiração/fosforilação passa a parcial por este recorte; mecanismos dos complexos, rotação/estequiometria da ATP-sintase, regulação e rendimento global permanecem pendentes. Não se atribui ao livro o ciclo sintético m=2/3, ΔG=50.

## Revisão pessoal de 20 minutos

Desenhe os lados P/N e o caminho I→Q→III→cit c→IV; adicione a entrada II→Q. Depois derive o sinal do termo químico a partir do pH e some as duas parcelas, com unidades. Inverta a direção e explique por que o sinal muda. Registre dúvidas e ajuda utilizada; explicação de Jhuann não foi preenchida pelo agente.
