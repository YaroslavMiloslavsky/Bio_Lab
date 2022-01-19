from biolab import BioLab
from molecules.dna import DNA

def main():
    print('Welcome to the BioLab v0.1.1')
    print('Choose the functionality:')
    print('1 - BioLab (Soon)')
    print('2 - DNA functions test')

    choice = int(input('***Select and option: '))

    if choice == 1:
        print('Coming soon')
    if choice == 2:
        size = int(input('Choose the size of the dna: '))
        dna = DNA(size)
        print('Choose a function to test')
        print('1 - replicate')

        option = int(input('***Select and option: '))
        if option == 1:
            print(dna)
            dna.replicate()

'''TODO Implement statistics!!'''

if __name__ == '__main__':
    main()
    # dna = DNA(20)
    # dna.replicate()
