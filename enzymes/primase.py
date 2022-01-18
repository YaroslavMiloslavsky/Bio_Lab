class Primase:

    def __init__(self, strand, primar_length, direction) :
        self.length = primar_length
        self.strand = strand
        self.direction = direction
        self.sequence = []

    def connect(self):
        from molecules.dna import DNA
        if self.direction == (5,3):
            print('5 --> 3')
            for i in range(len(self.strand)):
                second_base=DNA.complete_base_pair(self.strand[i])
                if i < self.length:
                    self.sequence.append([self.strand[i], second_base])
                else:
                    self.sequence.append([self.strand[i]])
            return self.sequence

        elif self.direction == (3,5):
            print('3 <-- 5')
            for i in range(len(self.strand)):
                if i%self.length==3 or i==len(self.strand)-1: # TODO dynamic with random
                   # Stick a primar TODO for now it is sized 1 primar
                    second_base=DNA.complete_base_pair(self.strand[i])
                    self.sequence.append([self.strand[i], second_base])
                    
                else:
                    self.sequence.append([self.strand[i]])
            return self.sequence


    def __str__(self):
        dna_sequence = ''
        for i in self.sequence:
            dna_sequence += f'{i[0]} - {i[1]}\n'
        return (dna_sequence)