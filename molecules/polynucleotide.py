from molecules.base.molecule import Molecule


class Polynucleotide(Molecule):
    '''AKA strands of a DNA - The polynucleotide in made of nucleotides which define the weight of the gene
        Even though this class is pretty self explanatory, notice that this class uses encapsulation heavily, in order to simulate real life molecules'''
    def __init__(self) -> None:
        super().__init__(0)
        self._nucleotides = [] # This should be a separate class
        self.direction = (5,3) # A tuple 3-5 or 5-3 and read 5 --> 3

    def asses_length(self):
        self.length = len(self._nucleotides)
        return len(self._nucleotides)

    def add(self, base):
        '''As the class name, this class adds the new element into the the gene sequence'''
        self._nucleotides.append(base)

    def index(self, i):
        return self._nucleotides[i]

    def set_primes(self, first_prime, second_prime):
        self.direction = (first_prime, second_prime)

    def __str__(self) -> str:
        nucleotides = ''
        for i in self._nucleotides:
            nucleotides += i
        return f'length: {self.length}, {self.direction[0]} {nucleotides} {self.direction[1]}'