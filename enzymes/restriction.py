from enzymes.base.enzyme import Enzyme

from molecules.dna import DNA

class Restriction(Enzyme):

    def __init__(self):
        super().__init__()

    @classmethod
    def blunt(cls, dna, index):
        '''
        This method is a general simulation of generic blunt restriction enzyme
        It seeks no special sequence like a real enzyme does
        '''
        return dna.sequence[:index],dna.sequence[index+1:]
    
    @classmethod
    def sticky_ends(cls, dna, first_index, last_index):
        '''
        This method is a general simulation of sticky ends restriction enzyme
        '''
        upper_sequence = []
        lower_sequence = []

        for i in range(0, first_index):
            lower_sequence.append(dna.sequence[i])
        lower_sequence.append(dna.sequence[first_index])
        for i in range(first_index+1, last_index):
            lower_sequence.append([dna.sequence[i][0], ' '])
        
        for i in range(first_index+1, last_index):
            upper_sequence.append([' ',dna.sequence[i][1]])
        upper_sequence.append(dna.sequence[last_index])

        for i in range(last_index+1, int(dna.length/2)):
            upper_sequence.append(dna.sequence[i])

        
        DNA.print_strand(strand=lower_sequence)
        print()
        DNA.print_strand(strand=upper_sequence)

        return lower_sequence, upper_sequence

                 