# Maxwell: componente, módulo e cauda

Modelo clássico 3D isotrópico em equilíbrio, sem velocidade média do gás; massa positiva,θ=kB T_K. Rascunho assistido porIA, revisão pessoal pendente. Sem dados medidos, dinâmica ou amostragem de trajetórias.

Na raiz:

```sh
python3 -B -m labs.maxwell-geometria.speed
python3 -B -m unittest discover -s labs/maxwell-geometria -t .
```

s=√(θ/m) é desvio padrão de uma componente, x=vx/s assinado e u=|v|/s≥0. φ(x)=exp(−x²/2)/√(2π);q(u)=√(2/π)u²exp(−u²/2). Densidade em velocidade física éq(v/s)/s; densidade vetorial tem unidadeinversa de velocidade³, densidade de rapidez inversa de velocidade. Valores de densidade não são probabilidades pontuais. Máximo do vetor na origem e modo radial não coincidem devido ao fator de casca4πv².

`scales(θ,m)`retorna modo,média,RMS e segundo momento. θ/m está em velocidade²;θ,m em1e−4..1e4 no sistema escolhido,domínio didático numérico,sem unidadeinferida pelo código. θ2,m1:dámodo2,média4/√π,RMS√6,segundo momento6. Campos devem usar unidades coerentes;não confundirθ em energia com kelvin semkB.

PDFs e caudas de u são avaliadas apenas no domínio0..32;componente em−32..32. Este é limite daAPI,não truncamento físico da distribuição. Entradas int/float finitos,sem bool/texto. `tails(u)`devolveP(U>u) eE[U²;U>u],segundo momento NÃO condicionado ao evento. Fórmulas por integração por partes usam erfc para evitar subtrair números próximos de1. Não se usa o quadrado da rapidez média como segundo momento.

Cinco testes:referências;normalizações/momentos porSimpson existente;quatro caudas por integral direta até12e fatorgeométrico;quatro cenários de escala/modo;snippet/desafio antigos/contratos. A contribuição após12é desprezível perante as tolerâncias desses testes,sem certificar erro de toda quadratura numérica. No desafio antigo,janela[0,8]na escala s1 omite massa≈8,21e−14 e segundo momento≈5,42e−12;malha também tem erro próprio. Sem repetir testestodos os labs.

Isotropia sozinha não implica independência de componentes:distribuição uniforme numa esfera de rapidez fixa é isotrópica mas não gaussiana/fatorada. O modelo canônico com energia cinética separável justifica a fatoração usada. Não adotamos como universal a generalização informal da fonte de que só rotação já fixa a distribuição. Interações/termostatos/relatividade eBose/Fermi fora do recorte.

Fonte primária:DavidTong,Statistical Physics§2.3,corpo parcial30/10/2026, https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S2.html . Mudança para velocidades/cascas,normalização e segundo momento;parágrafo do argumento deMaxwell lido para distinguir hipótese de fatoração. Figuras,exercícios e código locais;figura de gases nobres/história não reproduzidas. SemPDFprivado distribuído.
