"""Concatenate supplied transcript intervals; does not predict splicing."""
PRECURSOR = "AUGGUAGGAAGUAGUAG"
ISOFORM_A = ((0,3),(7,10),(14,17))
ISOFORM_B = ((0,3),(14,17))

def splice(rna, intervals):
    """Return (sequence, source_positions), with zero-based half-open intervals."""
    if not isinstance(rna,str):
        raise TypeError("RNA must be a string")
    if not rna or set(rna)-set("ACGU"):
        raise ValueError("RNA must be nonempty uppercase ACGU")
    if not isinstance(intervals,(list,tuple)):
        raise TypeError("intervals must be list or tuple")
    if not intervals:
        raise ValueError("at least one interval is required")
    positions=[]
    previous_end=0
    for pair in intervals:
        if not isinstance(pair,(tuple,list)) or len(pair)!=2:
            raise ValueError("each interval must contain start,end")
        start,end=pair
        if type(start) is not int or type(end) is not int:
            raise TypeError("coordinates must be integers, excluding bool")
        if not 0<=start<end<=len(rna) or start<previous_end:
            raise ValueError("intervals must be in order, nonoverlapping and within RNA")
        positions.extend(range(start,end))
        previous_end=end
    return ''.join(rna[i] for i in positions),tuple(positions)

if __name__ == "__main__":
    for name,intervals in (("A",ISOFORM_A),("B",ISOFORM_B)):
        print(name,splice(PRECURSOR,intervals))
