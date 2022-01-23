from types import NoneType
from enzymes.ligase import Ligase
from molecules.dna import DNA
from enzymes.polymerase import Polymerase

class Dna_Test_Tube:
    """
    This is a class for the DNA test tube which will undergo different lab functions.
    The test can be performed on multiple DNA molecules or on a single one

    Attributes:
        dna_array: The array of DNAs in the tube
        single_dna: Single DNA molecule
        Notice: Only one can be chosen but not both
    """

    def __init__(self, dna_array=None, single_dna=None):
        self.dna_array = dna_array if dna_array else []
        self.single_dna = single_dna if single_dna else None

    def __str__(self) -> str:
        dna_molecules = ''
        for dna in self.dna_array:
            print(dna)

        return dna_molecules

    def length_sort(self):
        """
        The function to mimics the Gel Electrophoresis process.
        """
        self.dna_array =  sorted(
            self.dna_array,
            key = lambda x: x.length,
            reverse=True
        )

    def dna_in_tube(self):
        return self.dna_array

    def pcr(self, sequence, revolutions, tube):
        if revolutions < 1:
            return 

        a, b = self.amplify(sequence=sequence)
        if a :
            tube.append(a)
        if b :
            tube.append(b)

        Dna_Test_Tube(single_dna=a).pcr(sequence=sequence,revolutions=revolutions-1, tube=tube)
        Dna_Test_Tube(single_dna=b).pcr(sequence=sequence,revolutions=revolutions-1, tube=tube)


    def amplify(self, sequence):
        """
        The function to mimics the PCR process.

        Attributes:
        sequence: The sequence we want to amplify
        """
        sequence_length = len(sequence)
        #Step 1: Separate DNA strands aka denaturation
        upper_strand, lower_strand = self.single_dna.get_strands()
        
        # print(upper_strand) # 5,3
        # print(lower_strand) # 3,5
        # print()
        #Step 2: Annealing, we construct the given primars in the sequence that we were given
        # 5 --> 3 (the sequence will connect from the other side 3 --> 5)
        # We try and connect the sequence to the upper stand
        upper_new_sequence = []
        upper_strand_length = upper_strand.asses_length()

        for i in range(upper_strand_length-1,-1,-1):
            if i >= upper_strand_length-sequence_length:
                correct_second_base = DNA.complete_base_pair(upper_strand.index(i))
                if correct_second_base == sequence[upper_strand_length-i-1]:
                    upper_new_sequence.append([upper_strand.index(i),sequence[upper_strand_length-i-1]])
                else:
                    # print(f'{upper_strand.index(i)},{sequence[upper_strand_length-i-1]} is can\'t connect')
                    upper_new_sequence.append([upper_strand.index(i)])
            else:
                upper_new_sequence.append([upper_strand.index(i)])
        upper_new_sequence.reverse()

        primar_success_count = len(upper_new_sequence)
        for i in upper_new_sequence:
            if len(i)<2:
                primar_success_count -= 1
        if primar_success_count < sequence_length:
            upper_new_sequence = []

        # print('Upper Strand After Annealing')
        # DNA.print_strand(strand=upper_new_sequence)
        # print()

         # 3 --> 5 (the sequence will connect normally)
        # We try and connect the sequence to the lower strand
        lower_new_sequence =[]
        lower_strand_length = lower_strand.asses_length()
     
        for i in range(0, lower_strand_length):
            if i< sequence_length:
                # lower_new_sequence.append([lower_strand.index(i), sequence[i]])
                correct_second_base = DNA.complete_base_pair(lower_strand.index(i))
                if correct_second_base == sequence[i]:
                    lower_new_sequence.append([lower_strand.index(i),sequence[i]])
                else:
                    # print(f'{lower_strand.index(i)},{sequence[i]} is can\'t connect')
                    lower_new_sequence.append([lower_strand.index(i)])
            else:
                lower_new_sequence.append([lower_strand.index(i)])
        
        primar_success_count = len(lower_new_sequence)
        for i in lower_new_sequence:
            if len(i)<2:
                primar_success_count -= 1
        if primar_success_count < sequence_length:
            lower_new_sequence = []

        # print('\nLower Strand After Annealing')
        # DNA.print_strand(strand=lower_new_sequence)

        # Step 3: Extension with the polymerase
        # print('\nAfter Extension - Upper New')
        polymerase = Polymerase()
        try:
            polymerase.fully_connect(upper_new_sequence, upper_strand.direction)
        except:
            print('Couldn\'t complete')
        # DNA.print_strand(strand=upper_new_sequence)

        # print('\nAfter Extension - Lower New')
        polymerase = Polymerase()
        try:
            polymerase.fully_connect(lower_new_sequence, lower_strand.direction)
        except:
            print('Couldn\'t complete')

        # DNA.print_strand(strand=lower_new_sequence)
        
        # TODO check a false positive and erase them

        dna_upper = DNA(strand=upper_new_sequence)
        dna_lower = DNA(strand=lower_new_sequence)

        ligase = Ligase()
        ligase.repair_strand(dna=dna_upper, first_index=0,last_index=int(dna_upper.length/2))
        ligase.repair_strand(dna=dna_lower, first_index=0,last_index=int(dna_lower.length/2))

        return [dna_upper, dna_lower]
        

    def extract(self, sequence):
        extracted_tube = []
        for dna in self.dna_array:
            dna_upper, dna_lower = dna.get_strands()

            if sequence in dna_upper.get_sequence() or sequence in dna_lower.get_sequence():
                extracted_tube.append(dna)

        return extracted_tube


    def sequence_bases(self):
        """
        The function to mimics the Electric pulse that allows us to know which bases construct our DNA molecule.

        Reactions:
        A - returns 1 
        T - returns 2
        C - returns 3
        G - returns 4
        """
        if self.single_dna != None:
            return Dna_Test_Tube._single_molecule_sequence(self.single_dna)

        elif self.dna_array != None:
            bases = []
            for i in self.dna_array:
                bases.append(Dna_Test_Tube._single_molecule_sequence(i))
            return bases

    @classmethod
    def _electric_shock(cls, base):
        return{
            'A': lambda: 0b01,
            'T': lambda: 0b10,
            'C': lambda: 0b11,
            'G': lambda: 0b100
        }[base]()

    @classmethod
    def _single_molecule_sequence(cls, dna):
        bases = {}
        dna_upper, dna_lower = dna.get_strands()
        bases['upper_dna'] = [Dna_Test_Tube._electric_shock(i) for i in dna_upper.get_sequence()]
        bases['lower_dna'] = [Dna_Test_Tube._electric_shock(i) for i in dna_lower.get_sequence()]

        return bases