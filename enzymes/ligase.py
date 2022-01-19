from enzymes.base.enzyme import Enzyme

class Ligase(Enzyme):
    '''This class represents a ligase enzyme to repair breaks in DNA strands '''
    def __init__(self):
        super().__init__()

    
    @classmethod
    def repair_strand(cls, dna, first_index, last_index):
        '''Repairs the strand int positions [first_index, last_index] included
            The direction of the primars is important'''
        from molecules.dna import DNA
        # removes the pair that is in DNA['second_strand'] evaluates and puts it back corrected
        for i in range(first_index, last_index):
            first_strand_base = dna.sequence[i][0]
            second_strand_base = dna.sequence[i][1] # We check if it is correct
            correct_second_strand = DNA.complete_base_pair(first_strand_base)

            if second_strand_base != correct_second_strand:
                print(f'current pair is ({first_strand_base},{second_strand_base}) but should be ({first_strand_base},{correct_second_strand})')
                dna.sequence[i][1] = correct_second_strand
            # dna.sequence[i][1] = 'Test'