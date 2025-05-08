# 🧩 Sudoku Matrix Generator

This project provides a simple Python script that generates a square matrix of size `n x n` with random unique numbers, simulating a basic Sudoku-like setup.

---

## 📁 Project Structure
.
+-- sudoku.py
+-- _utils
|   +-- utilities.py
+-- _test
|   +-- test_sudoku.py

---

## 🚀 How to Run

### 🔧 Prerequisites
- Python 3.6+
- No external dependencies required or pytest if you want to run pytest contained inside requirements.txt file

### ▶️ Usage

Run the script from the terminal:

```bash
python3 sudoku.py

You'll be prompted to enter a matrix dimension (n). The maximum allowed value is 10 (i.e., a 10x10 matrix).

Define a square matrix dimmension
It does not have to be greater than 10
5

The matrix that we got is [[3, 12, 5, ...], [...], ...]

✅ All elements are unique elements across the sudoku

