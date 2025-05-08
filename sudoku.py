"""
sudoku puzzles are solved by filling a 9x9 grid with numbers 1-9, 
ensuring that no number repeats in any row, column, or 3x3 block. 
Each row, column, and 3x3 square must contain all the numbers from 1 to 9, without any repetitions
Thi is a possible represntation of the matrix:
sudoku_elements = [["5","3","4","6","7","8","9","1","2"],
                ["6","7","2","1","9","5","3","4","8"],
                ["1","9","8","3","4","2","5","6","7"],
                ["8","5","9","7","6","1","4","2","3"],
                ["4","2","6","8","5","3","7","9","1"],
                ["7","1","3","9","2","4","8","5","6"],
                ["9","6","1","5","3","7","2","8","4"],
                ["2","8","7","4","1","9","6","3","5"],
                ["3","4","5","2","8","6","1","7","9"]]
"""
import sys
from utils.utilities import sudokuGame


if __name__ == '__main__':

    print("Define a square matrix dimmension")
    print("It does not have to be greater than 10")
    
    n = int(input())
    if n > 10:
        print("You have exceeded the limit of square matrix which is 10")
        sys.exit(1)
    print("\n")
    matrix_gen = sudokuGame(n)
    matrix = matrix_gen.generate_square_matrix()
    print(f"""The matrix that we got is {matrix}""")
    print("\n")
    if matrix_gen.check_unique_elements():
        print("✅ All elements are unique elements accros the sudoku")
    else:
        print("❌ There are repeated elements in the sudoku.")