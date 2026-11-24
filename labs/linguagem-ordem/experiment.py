"""Reconhecedor específico de a*b*, não compilador geral de regex."""
TRANSITIONS = {
    "A": {"a": "A", "b": "B"},
    "B": {"a": "X", "b": "B"},
    "X": {"a": "X", "b": "X"},
}
ACCEPTING = frozenset({"A", "B"})

def trace(word):
    if not isinstance(word, str) or any(c not in "ab" for c in word):
        raise ValueError("O rastro exige uma palavra de {a,b}*")
    states = ["A"]
    for symbol in word:
        states.append(TRANSITIONS[states[-1]][symbol])
    return tuple(states)

def accepts(word):
    if not isinstance(word, str):
        raise ValueError("A entrada deve ser uma string")
    state = "A"
    for symbol in word:
        if symbol not in "ab":
            return False
        state = TRANSITIONS[state][symbol]
    return state in ACCEPTING

if __name__ == "__main__":
    for word in ("", "aabb", "aba", "bbb"):
        print(repr(word), trace(word), accepts(word))
