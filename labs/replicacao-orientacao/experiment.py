"""Sequências sintéticas, cópia ideal e orientação de uma forquilha; sem cinética."""


def complement(sequence):
    if type(sequence) is not str or not sequence or any(b not in 'ACGT' for b in sequence):
        raise ValueError('Use uma sequência não vazia, maiúscula, apenas ACGT')
    return sequence.translate(str.maketrans('ACGT','TGCA'))


def reverse_complement(sequence):
    """Recebe e devolve sequência escrita 5 para 3."""
    return complement(sequence)[::-1]


def fork(direction=1):
    if type(direction) is not int or direction not in (-1,1):
        raise ValueError('Sentido -1 (esquerda) ou +1 (direita)')
    return dict(leading='inferior' if direction==1 else 'superior',
                lagging='superior' if direction==1 else 'inferior',
                leading_growth=direction,lagging_growth=-direction)


def replicate(sequence):
    """Entrada: molde superior 5→3. Saída: dois duplexes alinhados da esquerda para direita."""
    bottom=complement(sequence)
    return ((dict(bases=sequence,orientation='5→3',origin='parental'),
             dict(bases=bottom,orientation='3→5',origin='nova')),
            (dict(bases=sequence,orientation='5→3',origin='nova'),
             dict(bases=bottom,orientation='3→5',origin='parental')))


if __name__=='__main__':
    assert complement('ACGTAACC')=='TGCATTGG'
    assert reverse_complement('ACGTAACC')=='GGTTACGT'
    assert fork(1)['leading']=='inferior'
    print(replicate('ACGTAACC'))
