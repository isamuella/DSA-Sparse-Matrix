# Sparse Matrix Operator

## Programming Assignment: Sparse Matrix Operations

A simple Python program to perform **addition**, **subtraction**, and **multiplication** on **sparse matrices** loaded from input files.

---

## Task Description

Using Python, this program:

- Loads **two sparse matrices** from input files.
- Performs:
  - ➕ Addition
  - ➖ Subtraction
  - ✖️ Multiplication (if dimensionally compatible)
- Allows the user to **save the result** to a file.

---

## Features

- Input: Text files with sparse matrix data.
- Matrix format:
  ```
  rows=<number_of_rows>
  cols=<number_of_columns>
  (row_index, col_index, value)
  (row_index, col_index, value)
  ...
  ```
- Handles:
  - Whitespace and formatting issues
  - Dimension mismatch for multiplication
- Outputs results in the same format to a file

---

## Requirements

- Python 3.x  
- Check with `python --version` or `python3 --version` depending on your system.

---

## Installation & Setup

1. **Clone the Repository**

```bash
git clone https://github.com/isamuella/DSA-Sparse-Matrix.git
cd DSA-Sparse-Matrix
```

2. **Navigate to the `src` Directory**

```bash
cd dsa/sparse_matrix/code/src/
```

3. **Ensure Input Files are in the Same Directory**

Place your input `.txt` matrix files in the `src` folder.

---

## How to Run

To run the program:

```bash
python3 -u sparse_matrix.py
```
---

## Example

### **Input File: easy_sample_02_1.txt**
```
rows=1
cols=2
(0, 1, 3)
(0, 2, 4)
```

### **Input File: easy_sample_02_2.txt**
```
rows=1
cols=2
(0, 1, 5)
(0, 2, 10)
```

### **Output**

**Addition**
```
rows=1
cols=2
(0, 1, 8)
(0, 2, 14)
```

**Subtraction**
```
rows=1
cols=2
(0, 1, -2)
(0, 2, -6)
```

**Multiplication**
```
❌ Multiplication not feasible: Column count of easy_sample_02_1.txt ≠ Row count of easy_sample_02_2.txt. Instesd you can use easy_sample_02_2.txt and easy_sample_02_3.txt
```

---

## Handling Input Issues

✅ Whitespace Handling  
- Lines with only whitespace are ignored.  
- Leading/trailing whitespace in values is removed.

✅ Empty Lines  
- Skipped automatically during matrix loading.

---

## Author

**Ineza Samuella**  
s.ineza@alustudent.com

---

## License

This project is for educational use and is open for contributions or enhancements.
