# Quatro spins: média, distribuição e resposta

Laboratório original, sintético, de equilíbrio canônico. Spins independentes σ=±1, E=−hΣσ, kB=1. T>0 é energia; em kelvin substituir T por kB T_K. Sem dinâmica ou material real.

`distribution(n,r)` recebe **r=exp(2h/T)**, não h. Inteiros/Fraction, 1≤n≤100, r>0; permite probabilidades exatas sem arredondar exponenciais. Não é enumeração de 2^n sequências em produção. O teste faz enumeração independente até n=6.

N=4, r=1: massas 1,4,6,4,1 divididas por16 para M=−4,−2,0,2,4. Média0, variância4, P(M=0)=3/8. Em T=2, resposta em h=2.
N=4,r=3: p+=3/4, média2, variância3, resposta em h=3/2 para T=2. Neste caso h=ln3, não3.

`response(n,r,T,mu)` devolve ∂B⟨mu M⟩=mu² Var(M)/T para h=mu B. Mu positivo e constante; total, sem dividir pelo volume, sem convenção H/μ0. Para resposta dimensionless em h use mu=1. M não é momento em SI.

Da raiz: `python3 -B -m unittest discover -s labs/paramagneto-finito -t .` e `python3 labs/paramagneto-finito/spin.py`.

Fonte temática parcialmente consultada30/10/2026: [Tong, §1.3.2](https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S1.html), sistema de dois níveis e fatoração da partição. Sua origem0,ε corresponde a deslocar nossos níveis−h,+h por+h quando h>0, com ε=2h; os rótulos dos estados diferem. A figura, enumeração, exemplos e deduções finitas são locais. Sem cópia de figura/exercício. Revisão pessoal pendente.
