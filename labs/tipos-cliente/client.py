"""Cliente de tipos da biblioteca padrão; política explícita para rótulos."""
import unicodedata
import math


def label_key(text: str) -> str:
    if not isinstance(text,str):raise ValueError('Rótulo deve ser texto.')
    key=unicodedata.normalize('NFC',text.strip()).casefold()
    key=unicodedata.normalize('NFC',key)
    if not key:raise ValueError('Rótulo vazio não aceito neste cliente.')
    return key


def interference(z,w):
    values=[]
    for value in (z,w):
        if isinstance(value,bool) or not isinstance(value,(int,float,complex)):
            raise ValueError('Números complexos finitos,sem bool/texto.')
        try:value=complex(value)
        except (ValueError,OverflowError):raise ValueError('Número fora do domínio.') from None
        if not math.isfinite(value.real) or not math.isfinite(value.imag):
            raise ValueError('Componentes finitas necessárias.')
        values.append(value)
    z,w=values
    try:
        zz=z+w;cross=2*(z*w.conjugate()).real
        out=dict(z_abs=abs(z),w_abs=abs(w),sum_abs=abs(zz),
                 sum_square=zz.real**2+zz.imag**2,
                 component_squares=z.real**2+z.imag**2+w.real**2+w.imag**2,
                 cross=cross)
    except OverflowError:raise ValueError('Resultado fora do domínio numérico.') from None
    if not all(math.isfinite(v) for v in out.values()):
        raise ValueError('Resultado fora do domínio numérico.')
    return out


if __name__=='__main__':
    original=' FI\u0301SICA ';key=label_key(original)
    print('Original preservado:',repr(original),'chave:',key)
    a=[1];b=a;returned=b.append(2);c=a.copy();c.append(3)
    print('Alias:',a,b,'retornoappend:',returned,'cópia externa:',c)
    print('Complexos sem unidade:',interference(3+4j,-3+4j))
