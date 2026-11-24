"""Previsões e limites de erro assumidos; dados sintéticos, sem inferência estatística."""
def model(accel=2, bias_cm=0, bound_cm=4):
    if any(type(x) is not int for x in (accel,bias_cm,bound_cm)) or not 0<=accel<=4 or not -20<=bias_cm<=20 or not 0<=bound_cm<=20:
        raise ValueError('a inteiro0..4m/s²; desvio−20..20cm; limite0..20cm')
    perturbations=(0,4,-4,4,-4)  # unidades internas de1/200m, não sorteios
    rows=[]
    for i,e in enumerate(perturbations):
        # t=i/2s; x0=0,5m; v0=0,5m/s; gerador com a=2m/s².
        observed=100+50*i+50*i*i+e+2*bias_cm
        predicted=100+50*i+25*accel*i*i
        residual=observed-predicted
        rows.append({'time':i/2,'observed':observed/200,'predicted':predicted/200,
                     'residual':residual/200,'within':abs(residual)<=2*bound_cm})
    return {'accel':accel,'bias_cm':bias_cm,'bound_cm':bound_cm,'rows':rows,
            'inside':sum(r['within'] for r in rows),'max_abs':max(abs(r['residual']) for r in rows)}

if __name__ == '__main__':
    m=model(); assert m['inside']==5 and m['max_abs']==.02
    print('a=2:',m)
    print('a=0, mesma posição e velocidade iniciais:',model(0)['inside'],'de5 dentro do limite')
