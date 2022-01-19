from biolab import BioLab
from molecules.dna import DNA
from termcolor import colored
import os

'''This is a prototype of a CLI to come'''

def choice_bio_lab():
    print(colored('Coming soon', 'red'))

def choice_dna_test_tube():
    print(colored('Select an option below','green'))
    print(colored('1 - DNA replication', 'blue'))
    print(colored('2 - Soon ...', 'red'))
    choice = int(input('Selected Option: '))
    
    try:
        dna_test_tube_choices(choice=choice)
    except KeyError:
        print('Please select a valid choice')

def dna_test_replicate():
    size = int(input('Choose the size of the dna: '))
    dna = DNA(size)
    dna.replicate()

def dna_test_soon():
    print('Coming soon')

def choice_selection(choice):
    return {
        1: lambda: choice_bio_lab(),
        2: lambda: choice_dna_test_tube(),
    }[choice]()

def dna_test_tube_choices(choice):
    return{
        1: lambda: dna_test_replicate(),
        2: lambda: dna_test_soon(),
    }[choice]()

def main():
    os.system('clear')
    os.system('cls')
    print(colored('Welcome to the BioLab v0.1.1','green'))
    print(colored('Choose the functionality:', 'green'))

    while True:
        print(colored('1 - BioLab (Soon)','red'))
        print(colored('2 - DNA functions test','blue'))

        print()
        choice = int(input(colored('Selected Option: ', 'green')))
        try:
            choice_selection(choice=choice)
        except KeyError:
            print('Please select a valid choice')
        


if __name__ == '__main__':
    main()
    # dna = DNA(20)
    # dna.replicate()
