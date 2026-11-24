# Paralelo e rede mista — notas de aula

Rascunho original assistido por IA; revisão pessoal e uso com aluno pendentes. Python opcional; sem montagem física ou dado real.

## Modelo

Fonte ideal Vs≥0, fio ideal, resistor série R0≥0 e banco de ramos Ri>0. Regime DC estacionário. Mesmos dois nós implicam tensão comum Vb; conservação da carga dá I=ΣIi. Como Ii=Vb/Ri, 1/Rp=Σ1/Ri. Rede:Req=R0+Rp, I=Vs/Req, Vb=I Rp. Potência:R0 I²+ΣVb Ii=Vs I. Não é solver geral de nós, ponte, fonte real ou transitório. Retirar um ramo significa removê-lo da lista; resistor zero no banco não é permitido.

## Exemplos e respostas

Banco6||3 Ω direto a12 V:Rp2 Ω, ramos2e4 A, total6 A, potências24e48 W, total72 W. Adicionar R0=2 Ω:Req4 Ω,I3 A,Vb6 V,ramos1e2 A,potências18 W emR0 e6/12 W nos ramos,total36 W. Fonte tem potência absorvida negativa pela convenção passiva.

Ramo6 Ω sozinho direto:2 A. Adicionar ramo3 Ω direto mantém2 A no antigo. Com R0=2 Ω, antes I6=12/8=1,5 A eVb9 V; depois I6=1 A eVb6 V. A corrente da fonte sobe enquanto a do ramo antigo cai. Isso distingue tensão terminal da fonte e tensão do banco.

Respostas1–8:2 Ω;2 A;4 A;6 A;72 W;6 V;1 A;36 W. 9:mesmos dois nós.10:sim,condutâncias positivas se somam.11:menor R sob mesma V.12:não,queda série altera tensão comum.

## Verificação

```sh
python3 -m unittest discover -s labs/circuito-paralelo -t .
```

Executar na raiz. Quatro testes:exemplos;81 configurações contra equação independente (Vs−Vb)/R0=ΣVb/Ri, com conservação de corrente,tensão e potência;mudanças de ramo e fonte zero;contratos e entradas imutadas. Int/Fraction sem bool/float. Banco não vazio,semR zero/negativo. Código apenas calcula o modelo; testes não validam uma montagem ou competência pessoal.

## Fonte e limites

OpenStax, CollegePhysics2e§21.1: https://openstax.org/books/college-physics-2e/pages/21-1-resistors-in-series-and-parallel , consulta parcial27/10/2026 de conexões,derivação da condutância, potência e associação mista. Não representa leitura integral ou currículo escolar brasileiro completo. Notas,figura,contas e rede escolhida originais; exercícios e figuras não reproduzidos.

Percurso escolar próprio, sem código acadêmico universitário ou equivalência de ementa. Nenhum livro privado copiado ou publicado. Ainda faltam instrumentos,fontes reais,redes não redutíveis por série/paralelo,capacitores e transitórios. Painel da aula anterior continua resolvendo só série; esta aula usa tabela e laboratório opcional, sem novo painel interativo.

## Revisão pessoal

Data: ____ · previsão antes de calcular: ____ · dúvida: ____
