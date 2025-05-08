import random

class sudokuGame:

    def __init__(self, n):

        """
        Initialize the class with the size of the matrix.
        
        Parameters
        ----------
        n : int
            The size (rows and columns) of the square matrix.
        """
        self.n = n
        self.matrix = []

    def generate_square_matrix(self):
        """
        Generates a square matrix based on n value
        Parameters
        ----------
        n : int
            value of square matrix
        Returns
        --------
        matrix: list
            A matrix with different random values on it
        """
        if self.n**2 > 10**6:

            raise ValueError("The matrix is to big for generating unique numbers")
    
        numbers = list(range(1, self.n * self.n +1))
        random.shuffle(numbers)
        self.matrix = [numbers[i * self.n:(i + 1) * self.n] for i in range(self.n)]
    
        return self.matrix
    
    def check_unique_elements(self):
        """
        Validates if the square matrix has unique elements for getting a possible result of sudoku game
        Parameters
        ----------
        matrix: list
            Square matrix with random numbers
        
        Returns
        --------
        True/False: bool
            True boolean value if does not find a repeated element, False if yes
    """
        seen = set()
        for row in self.matrix:
            for value in row:
                if value in seen:
                    return False
                seen.add(value)
        return True