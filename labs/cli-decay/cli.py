"""Small deterministic CLI: stdout JSON, argparse errors on stderr; no files/network."""
import argparse
import json
import math

def solve(steps=10,duration=1.0,rate=1.0,initial=1.0,method='euler'):
    if isinstance(steps,bool) or not isinstance(steps,int) or not 1<=steps<=100000:
        raise ValueError('steps must be an integer in 1..100000')
    values=[]
    for x in (duration,rate,initial):
        if isinstance(x,bool) or not isinstance(x,(int,float)):
            raise ValueError('finite real values required')
        try:y=float(x)
        except OverflowError:raise ValueError('finite real values required') from None
        if not math.isfinite(y):raise ValueError('finite real values required')
        values.append(y)
    duration,rate,initial=values
    if duration<=0 or rate<0 or initial<0:raise ValueError('duration>0, rate>=0, initial>=0 required')
    if method not in ('euler','exact'):raise ValueError('method must be euler or exact')
    product=rate*duration
    if not math.isfinite(product):raise ValueError('rate*duration must be finite')
    reference=initial*math.exp(-product)
    endpoint=reference
    if method=='euler':
        ratio=product/steps
        if ratio>1:raise ValueError('monotone Euler profile requires rate*duration/steps <= 1')
        endpoint=initial
        for _ in range(steps):endpoint*=1-ratio
    return dict(model='linear-decay-v1',method=method,steps=steps,duration=duration,rate=rate,initial=initial,endpoint=endpoint,reference=reference,absolute_error=abs(endpoint-reference))

def parser():
    p=argparse.ArgumentParser(description='Linear decay: Euler endpoint or analytic reference. No file writes.',allow_abbrev=False)
    p.add_argument('--steps',type=int,default=10,help='Euler steps, 1..100000; metadata only for exact')
    p.add_argument('--duration',type=float,default=1.0,help='positive final time in seconds')
    p.add_argument('--rate',type=float,default=1.0,help='nonnegative rate in inverse seconds')
    p.add_argument('--initial',type=float,default=1.0,help='nonnegative initial value in arbitrary U')
    p.add_argument('--method',choices=('euler','exact'),default='euler')
    return p

def main(argv=None):
    p=parser();args=p.parse_args(argv)
    try:result=solve(**vars(args))
    except ValueError as error:p.error(str(error))
    print(json.dumps(result,sort_keys=True,allow_nan=False))
    return 0

if __name__=='__main__':raise SystemExit(main())
