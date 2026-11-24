# RC com condição inicial e energia — rascunho

Aula `f3-rc` ampliada a14seções/12exercícios/4MathML. Exemplo τ6s,dois IDs e desafio de energia final preservados. Identificador rcCharging e quatro controles antigos preservados;V₀ e vista são adicionais com defaults compatíveis. Helper antigo ElectromagneticModels.rc permanece para compatibilidade;somente entrada visual antiga substituída.

## Fontes e autoria

Consulta direta pública parcial em22/10/2026:OpenStax University PhysicsII [10.5](https://openstax.org/books/university-physics-volume-2/pages/10-5-rc-circuits),carga/descarga e convenção de corrente;[8.3](https://openstax.org/books/university-physics-volume-2/pages/8-3-energy-stored-in-a-capacitor),energia e integral do trabalho. Balanço geral com condição inicial e fonte absorvendo é desenvolvimento próprio dessas equações. Não se declara leitura integral,nem consulta nova de PDF privado. Bibliografia privada anteriormente localizada permanece com seus estados de disponibilidade/edição;nenhum arquivo reproduzido.

## Contrato e derivação

R,C>0;V,V₀,u≥0 e finitos. τ=RC,t=uτ,Δ=V−V₀. V_C=V₀+Δ(1−e^(−u));I=Δe^(−u)/R;I=dq/dt,q=CV_C. E_f=CV(V_C−V₀) com sinal fornecido ao circuito. U_C=CV_C²/2;ΔU_C=(C/2)(V_C−V₀)(V_C+V₀);Q_R=CΔ²(1−e^(−2u))/2. E_f=ΔU_C+Q_R e VI=V_CI+RI². Fonte ideal tem de poder absorver energia se V₀>V>0. V=0 representa fechamento por fio ideal na descarga. Não garante comportamento de bateria/fonte comercial.

R=0 não pertence ao modelo;reduzir R altera correntes,potências e tempo,não as energias finais ideais. Indutância,radiação,perdas adicionais e aquecimento precisam de outros modelos. V₀ é preparação,não fonte adicional conectada. Expm1 evita cancelamento em tempo pequeno;as energias não são obtidas como resíduo forçado do balanço.

## Visual e verificação

Tese visual:mesmo painel,duas vistas com unidades distintas e uma tabela de energia atual/inicial/variação. Sem sobrepor corrente ao eixo em volts. Energia fornecida negativa representa absorção explícita. Escala com zero e margem para rótulos;controles em coluna no celular. Sem animação automática ou dados experimentais.

Quatro testes:144referências Decimal70dígitos por forma alternativa da exponencial;derivada da solução/lei da malha/potências e quadratura Simpson2048 de fontes/dissipação;descarga,retorno,início,escala e tempo pequeno;contratos.144estados Python/JS nas duas vistas e comparação com o helper antigo em V₀0. Testes e gráficos não substituem revisão conceitual ou validação física.

Próxima revisão pessoal:resolver V2,V₀4,R2,C3,u=ln2 e explicar−6=−10,5+4,5J. Redes gerais,fontes variáveis,RLC,medidas e demais tópicos continuam pendentes.
