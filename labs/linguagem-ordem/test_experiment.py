import unittest
import re
from itertools import product
from .experiment import trace, accepts, TRANSITIONS, ACCEPTING

class LanguageOrderTests(unittest.TestCase):
    def test_exhaustive_against_position_property_and_regex(self):
        for n in range(11):
            for letters in product("ab", repeat=n):
                word = "".join(letters)
                expected = not any(word[i] == "b" and word[j] == "a" for i in range(n) for j in range(i+1,n))
                self.assertEqual(accepts(word), expected)
                self.assertEqual(accepts(word), re.fullmatch(r"a*b*", word) is not None)

    def test_prefix_invariant_and_absorbing_rejection(self):
        for n in range(9):
            for letters in product("ab", repeat=n):
                word = "".join(letters)
                history = trace(word)
                self.assertEqual(len(history), n+1)
                for k,state in enumerate(history):
                    prefix = word[:k]
                    expected = "X" if "ba" in prefix else "B" if "b" in prefix else "A"
                    self.assertEqual(state, expected)
                if "X" in history:
                    self.assertTrue(all(s == "X" for s in history[history.index("X"):]))

    def test_counts_by_length_and_distinct_split_points(self):
        for n in range(13):
            accepted = {"".join(s) for s in product("ab", repeat=n) if accepts("".join(s))}
            constructed = {"a"*k+"b"*(n-k) for k in range(n+1)}
            self.assertEqual(accepted, constructed)
            self.assertEqual(len(accepted), n+1)

    def test_distinguishing_suffixes_and_reachability(self):
        self.assertEqual(trace("")[-1], "A")
        self.assertEqual(trace("b")[-1], "B")
        self.assertEqual(trace("ba")[-1], "X")
        for first,second,suffix in [("A","B","a"),("A","X",""),("B","X","")]:
            results=[]
            for state in (first,second):
                for c in suffix: state = TRANSITIONS[state][c]
                results.append(state in ACCEPTING)
            self.assertNotEqual(*results)

    def test_invalid_alphabet_and_contract(self):
        for word in ("c", "a bc", "a\nb", "á", "ε", "abbc"):
            self.assertFalse(accepts(word))
            with self.assertRaises(ValueError): trace(word)
        for word in (None, b"ab", 1, True):
            with self.assertRaises(ValueError): accepts(word)
        self.assertEqual(trace("aba"), ("A","A","B","X"))
        self.assertTrue(accepts(""))
        self.assertFalse(accepts("ba"))
