
class Dna_Test_Tube:
    """
    This is a class for the DNA test tube which will undergo different lab functions.
      
    Attributes:
        dna_array: The array of DNAs in the tube
    """

    def __init__(self, dna_array):
        self._dna_array = dna_array

    def __str__(self) -> str:
        dna_molecules = ''
        for dna in self._dna_array:
            print(dna)

        return dna_molecules

    def length_sort(self):
        """
        The function to mimics the Gel Electrophoresis process.
        """
        self._dna_array =  sorted(
            self._dna_array,
            key = lambda x: x.length,
            reverse=True
        )

    def dna_in_tube(self):
        return self._dna_array

    def amplify(self, sequence):
        """
        The function to mimics the PCR process.

        Attributes:
        sequence: The sequence we want to amplify
        """
        pass


