import unittest,itertools,math,cmath
from .spin import BASES,state,inner,amplitudes,probabilities,project,nonselective_probability

class SpinBasisTests(unittest.TestCase):
    def test_reference_and_complex_relative_phase(self):
        self.assertAlmostEqual(probabilities(BASES['x'][0],'z')[0],.5)
        psi=(math.sqrt(3)/2,.5j)
        self.assertAlmostEqual(probabilities(psi,'z')[0],.75)
        self.assertAlmostEqual(probabilities(psi,'x')[0],.5)
        self.assertAlmostEqual(probabilities(psi,'y')[0],(2+math.sqrt(3))/4)
        # Identical z populations with a different relative phase need not give same x.
        other=(math.sqrt(3)/2,.5)
        self.assertAlmostEqual(probabilities(other,'z')[0],.75)
        self.assertAlmostEqual(probabilities(other,'x')[0],(2+math.sqrt(3))/4)
    def test_bases_and_change_of_coordinates_roundtrip(self):
        for axis,vectors in BASES.items():
            for i,j in itertools.product((0,1),repeat=2):self.assertAlmostEqual(abs(inner(vectors[i],vectors[j])-(1 if i==j else 0)),0,places=14)
        for theta,phase in itertools.product([.2,.7,1.4],[0,.3,1.1]):
            psi=(math.cos(theta),cmath.exp(1j*phase)*math.sin(theta))
            for axis in 'xyz':
                amps=amplitudes(psi,axis);base=BASES[axis]
                recovered=tuple(sum(amps[k]*base[k][j] for k in (0,1)) for j in (0,1))
                self.assertTrue(all(abs(a-b)<1e-14 for a,b in zip(psi,recovered)))
                self.assertAlmostEqual(sum(probabilities(psi,axis)),1,places=14)
    def test_expectations_against_independent_pauli_matrices(self):
        matrices={'x':((0,1),(1,0)),'y':((0,-1j),(1j,0)),'z':((1,0),(0,-1))}
        for theta,phase in itertools.product([.2,.7,1.4],[0,.3,1.1]):
            psi=(math.cos(theta),cmath.exp(1j*phase)*math.sin(theta))
            for axis,matrix in matrices.items():
                vector=tuple(sum(matrix[i][j]*psi[j] for j in (0,1)) for i in (0,1))
                expected=inner(psi,vector);p,q=probabilities(psi,axis)
                self.assertAlmostEqual(expected.real,p-q,places=14);self.assertAlmostEqual(expected.imag,0,places=14)
                phased=tuple(cmath.exp(.6j)*a for a in psi)
                self.assertAlmostEqual(probabilities(phased,axis)[0],p,places=14)
    def test_selective_nonselective_and_coherent_recombination(self):
        psi=(1,0);p,post=project(psi,'x',0)
        self.assertAlmostEqual(p,.5)
        conditional=probabilities(post,'z')[0]
        self.assertAlmostEqual(conditional,.5);self.assertAlmostEqual(p*conditional,.25)
        self.assertAlmostEqual(nonselective_probability(psi,'x','z')[0],.5)
        self.assertAlmostEqual(probabilities(psi,'z')[0],1)
        # A coherent sum with specified phase is a different preparation than measurement.
        plus,minus=BASES['x'];coherent=tuple((a+b)/math.sqrt(2) for a,b in zip(plus,minus))
        self.assertAlmostEqual(probabilities(coherent,'z')[0],1)
        p,post=project((1,0),'z',1);self.assertEqual(p,0);self.assertIsNone(post)
        for axis in 'xyz':
            for outcome in (0,1):
                p,post=project((math.sqrt(3)/2,.5j),axis,outcome)
                self.assertGreater(p,0);self.assertAlmostEqual(probabilities(post,axis)[outcome],1)
    def test_normalization_and_contracts(self):
        for psi in [(0,0),(1,1),(True,0),(float('nan'),0),(float('inf'),0),(1e308,0),(1,)]:
            with self.assertRaises(ValueError):state(psi)
        with self.assertRaises(ValueError):probabilities((1,0),'a')
        with self.assertRaises(ValueError):project((1,0),'z',True)
