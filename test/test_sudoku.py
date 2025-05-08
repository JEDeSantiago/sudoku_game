import pytest
from utils.utilities import sudokuGame

def test_generate_matrix_size():
    game = sudokuGame(n=3)
    matrix = game.generate_square_matrix()
    assert len(matrix) == 3
    assert all(len(row) == 3 for row in matrix)

def test_unique_elements_in_matrix():
    game = sudokuGame(n=3)
    game.generate_square_matrix()
    assert game.check_unique_elements() == True

def test_large_matrix_raises_error():
    with pytest.raises(ValueError, match="The matrix is to[o]* big"):
        game = sudokuGame(n=2000)  # 2000^2 = 4,000,000 > 1,000,000
        game.generate_square_matrix()
