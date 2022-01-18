from biolab import BioLab
from molecules.dna import DNA

def main():
    lab = BioLab()

'''TODO Implement statistics!!'''

if __name__ == '__main__':
    # main()
    dna = DNA(15)
    print(dna)
    dna.replicate()
