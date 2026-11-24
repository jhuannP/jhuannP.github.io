# Associação ideal 2A⇌B: balanço, volume e intervalo

29/10/2026. Material original em rascunho para revisão de Jhuann.

B contém duas unidades A; nA=a0−2ξ, nB=b0+ξ. Conserva-se nA+2nB, não a soma de espécies. Quantidades em mol, v=V c° também em mol, K e Q adimensionais. Modelo ideal formal, sem dados de substância real ou previsão cinética. Não confundir com o simulador1:1 existente.

Q=v nB/nA². F=v(b0+ξ)−K(a0−2ξ)² tem sinais opostos em −b0 e a0/2 e derivada positiva no intervalo. Raiz única interior. Bisseção racional fornece lo≤ξ≤hi; o ponto médio tem erro≤(hi−lo)/2. Valores A/B retornados são aproximações se lo≠hi. Parâmetro steps0..200 controla divisões, não precisão experimental.

Referência original: a0=3,b0=0,K1; v1 dá A1 B1 ξ1; v8 dá A2 B1/2 ξ1/2, em mol. Diluição instantânea de v1 para8 multiplica Q por8 antes da reação, mantendo K. Extensão adicional −1/2 em relação ao primeiro equilíbrio. Comparação de estados finais, não trajetória.

Fontes: [OpenStax Chemistry2e§13.4](https://openstax.org/books/chemistry-2e/pages/13-4-equilibrium-calculations), consulta textual parcial de tabelas estequiométricas e raízes físicas em29/10/2026; não foram copiados exemplos/figuras. [Júpiter CCM0114](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0114), ativação15/07/2024 posterior à turma2023/2, versão ministrada não recuperada. Atkins disponível no mapa, sem nova consulta neste bloco.

Execução da raiz do protótipo:

```sh
python3 labs/equilibrio-21/association.py
python3 -B -m unittest discover -s labs/equilibrio-21 -t .
```

Testes constroem estados finais positivos antes de deduzir K, em27 combinações e três composições iniciais; conferem raiz contida, balanço e erro. Outros casos: referências/diluição, raiz não racional por sinais/intervalos aninhados, escala extensiva/extensão inversa e contratos. Não são validação experimental ou pedagógica.
