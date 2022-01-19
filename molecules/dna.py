import random
from enzymes.polymerase import Polymerase
from molecules.molecule import Molecule
from molecules.polynucleotide import Polynucleotide
from enzymes.primase import Primase


class DNA(Molecule):
    ''' DNA has the connections A-T and C-G'''  
    bases = {'A','C','T','G'}
    _first_polynucleotide = None
    _second_polynucleotide = None
    sequence = [] # list of list pairs

    '''The constructor will generate random legal sequence'''
    def __init__(self, sequence_length=0, strand=None):
        if sequence_length>0:
            super().__init__(sequence_length)
            self._first_polynucleotide = Polynucleotide()
            self._second_polynucleotide = Polynucleotide()

            self._first_polynucleotide.set_primes(5,3) # Upper one is from left to right
            self._second_polynucleotide.set_primes(3,5) # Buttom one is from right to left

            for _ in range(self.length):
                first_base = random.sample(self.bases, 1)[0]
                second_base = self.complete_base_pair(first_base)

                self._first_polynucleotide.add(first_base)
                self._second_polynucleotide.add(second_base)

                self.sequence.append([first_base, second_base])
        
            self.length = self._first_polynucleotide.asses_length() + self._second_polynucleotide.asses_length()
        else:
            super().__init__(sequence_length)
            self.sequence = strand
            self.length = len(list(self.sequence))
            self._first_polynucleotide = Polynucleotide()
            self._second_polynucleotide = Polynucleotide()

            self._first_polynucleotide.set_primes(5,3) # Upper one is from left to right
            self._second_polynucleotide.set_primes(3,5) # Buttom one is from right to left
            for i in self.sequence:
                self._first_polynucleotide.add(i[0])
                self._second_polynucleotide.add(i[1])
            
            self.length = self._first_polynucleotide.asses_length() + self._second_polynucleotide.asses_length()

    
    @classmethod
    def complete_base_pair(cls, first_base):
        '''There is a better way of implementing this, however,
         there are only 4 bases so we will keep it that way for now'''
        if first_base == 'A':
            return 'T'
        elif first_base == 'T':
            return 'A'
        elif first_base == 'C':
            return 'G'
        elif first_base == 'G':
            return 'C'
        else:
            raise ValueError(f'{first_base} is not a common base')
    
    
    def replicate(self):
        '''The method simulates the netural process of DNA replication,
        in the end we will have a tuple with 2 exact copies of the DNA'''

        '''Unlike the natural process of replication, the helicase unzips the genes procedurally'''
        leading_strand = self.helicase(self.sequence, 0) # 5-3
        lagging_strand = self.helicase(self.sequence, 1) # 3-5
        # print(upper_strand,'AND' ,lagging_strand)

        '''In the nature all of these processes are parallel, alas,
            had I had the programming skill which I lack I would implement this with threads'''
        '''First we deal with the leading strand'''
        # The primer is being selected -> TODO dynamic
        primase = Primase(strand=leading_strand, primar_length=4, direction=self._first_polynucleotide.direction)
        # The primase synthesize few connections
        upper_strand_DNA = primase.connect()
        # Lets test the new sequence
        print('Leading strand after primase')
        for i in upper_strand_DNA:
            i = list(i)
            if len(i)>1:
                print(f'{i[0]} - {i[1]}')
            else:
                print(f'{i[0]} - ')
        # The Polymerase continues from here until the end
        print('\nLeading strand after polymerease')
        polymerase = Polymerase()
        replica_one_DNA = polymerase.fully_connect(strand=upper_strand_DNA, primes=self._first_polynucleotide.direction)
        # Lets test the new sequence
        print(replica_one_DNA)

        '''Now we deal with the lagging strand'''
        primase = Primase(strand=lagging_strand, primar_length=4, direction=self._second_polynucleotide.direction)
        lower_strand_DNA = primase.connect()
        # Lets test the new sequence
        print('Lagging strand after primase')
        for i in lower_strand_DNA:
            i = list(i)
            if len(i)>1:
                print(f'{i[0]} - {i[1]}')
            else:
                print(f'{i[0]} - ')
         # The Polymerase continues from here until the end
        print('\nLagging strand after polymerease')
        polymerase = Polymerase()
        replica_two_DNA = polymerase.fully_connect(strand=lower_strand_DNA, primes=self._second_polynucleotide.direction)
        '''After this fragment, the Exonuclease enzyme should remove the Okazaki fragments RNA leftovers
            and the gaps are being filled with a Polymaraease followed by the DNA Ligase which gives the DNA its form'''
        print(replica_two_DNA)

        return (replica_one_DNA, replica_two_DNA)

    
    @classmethod
    def helicase(cls, seq ,index):
        '''This is the enzyme that unzips the DNA into 2 strands AKA replication fork proccess'''
        strand = []
        for i in seq:
            i = list(i)
            strand.append(i[index])
        return strand

    def __str__(self):
        print('strands - ',self._first_polynucleotide, self._second_polynucleotide)
        dna_sequence = 'DNA Sequence:\n'
        for i in self.sequence:
            i = list(i)
            dna_sequence += f'{i[0]} - {i[1]}\n'
        return dna_sequence

