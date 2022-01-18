

class Polymerase:

    def __init__(self) -> None:
        pass
    
    def fully_connect(self, strand, primes):
        from molecules.dna import DNA
        if primes == (5,3):
            for i in range(len(strand)):
                if len(strand[i])>1:
                    continue
                else:
                    strand[i].append(DNA.complete_base_pair(list(strand[i])[0]))
            return DNA(strand=strand)
        else:  # This does exactly what a polymerase does to a strand 3->5 
            for i in range(len(strand)):
                if len(strand[i])<2:
                    j=i
                    while len(strand[j])<2 and j>=0:
                        strand[j].append(DNA.complete_base_pair(list(strand[j])[0]))
                        j -= 1
                else:
                    continue
            return DNA(strand=strand)

 