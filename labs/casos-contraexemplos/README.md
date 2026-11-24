# Casos conhecidos e contraexemplos

Laboratório original de ensino. Não modifica código do site nem usa ferramenta externa de mutação. Energia clássica K=mv²/2,m≥0 e v assinado;unidades kg,m/s,J. Entradas racionais int/Fraction para isolar erros lógicos sem arredondamento;floats e bool rejeitados neste laboratório. O snippet anterior da aula continua sendo exemplo simples de float e contrato de massa,não esta API racional.

Cinco casos com referências manuais:repouso(1,0)→0,geral(2,3)→9,zero massa(0,3)→0,velocidade negativa(2,−3)→9,massa inválida(−1,3)→ValueError. Cinco erros deliberados:omitir1/2,omitir quadrado,elevar massa ao quadrado,aceitar massa negativa,rejeitar massa zero. A versão equivalent_abs usa|v|²=v²:é equivalente no domínio, não erro que uma suíte deveria rejeitar.

Casos gerais e velocidade negativa detectam os mesmos três erros aritméticos. Zero massa encontra rejeição indevida e massa inválida encontra validação ausente. Repouso não detecta nenhum dos cinco. Entre os cinco casos e cinco erros fornecidos,menor conjunto tem três casos:geral OU velocidade negativa,mais zero massa e inválida. Isso não é otimização geral ou certificação de uma suíte real. Um mutante sobrevivente pode ser equivalente ou não ter sido distinguido pelos casos.

## Fonte consultada em29/10/2026

Documentação oficial Python3.14 unittest:TestCase,assertEqual,assertRaises e subTest;recortes textuais de comparação,exceção esperada e identificação de iterações. https://docs.python.org/3.14/library/unittest.html . Sem copiar tutorial/teste da documentação. Matriz de falhas,implementações deliberadas,figura e busca finita originais. Não houve consulta a livro privado ou oferta curricular. Biblioteca padrão;sem instalação. Testado neste Mac com Python3.14.5,não Windows físico.

## Executar

```sh
python3 -B -m unittest discover -s labs/casos-contraexemplos -t .
python3 labs/casos-contraexemplos/audit.py
```

Quatro métodos:cinco referências literais/exceção;matriz de cinco casos contra cinco erros;duas suítes mínimas entre esses candidatos;28 pares m/v na versão equivalente,mais contratos. As falhas deliberadas são observações do laboratório, não testes de regressão deixados quebrados. A suíte do laboratório passa ao confirmar que os erros são detectados conforme esperado. Não é prova de correção geral,desempenho,segurança,validade física ou habilidade pessoal.
