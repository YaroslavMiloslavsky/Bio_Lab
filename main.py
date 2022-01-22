from biolab import Dna_Test_Tube
from molecules.dna import DNA
from termcolor import colored
import os

'''This is a prototype of a CLI to come'''

def choice_bio_lab():
    print(colored('Coming soon', 'red'))

def choice_dna_test_tube():
    print(colored('Select an option below','green'))
    print(colored('0 - Return', 'blue'))
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

def exit():
    os._exit(status=0)


def choice_selection(choice):
    return {
        0: lambda: exit(),
        1: lambda: choice_bio_lab(),
        2: lambda: choice_dna_test_tube(),
    }[choice]()

def dna_test_tube_choices(choice):
    return{
        0: lambda: main_loop(),
        1: lambda: dna_test_replicate(),
        2: lambda: dna_test_soon(),
    }[choice]()

def main_loop():
    os.system('clear')
    os.system('cls')
    while True:
        print(colored('0 - Exit', 'blue'))
        print(colored('1 - BioLab (Soon)','red'))
        print(colored('2 - DNA functions test','blue'))

        print()
        choice = int(input(colored('Selected Option: ', 'green')))
        try:
            choice_selection(choice=choice)
        except KeyError:
            print('Please select a valid choice')

def main():
    os.system('clear')
    os.system('cls')
    print(colored('Welcome to the BioLab v0.1.1','green'))
    print(colored('Choose the functionality:', 'green'))

    main_loop()

if __name__ == '__main__':
    # For production uncomment the function if you wish to use the CLI
    # main()

    # For testing purpose
    os.system('clear')
    os.system('cls')

    dna1 = DNA(sequence_length=10)
    print(dna1)
    a, b = dna1.replicate()
    print('replica 1:',a)
    print('replica 2:',b)


