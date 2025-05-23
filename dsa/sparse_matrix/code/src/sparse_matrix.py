import sys
import os

class SparseMatrix:
    def __init__(self, num_rows, num_cols):
        self.rows = num_rows
        self.cols = num_cols
        self.data = {}  # Using nested dictionaries instead of Map

    @staticmethod
    def from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

            rows = int(lines[0][5:])
            cols = int(lines[1][5:])

            matrix = SparseMatrix(rows, cols)

            for line in lines[2:]:
                line = line.strip()
                if not line:
                    continue

                # Parse (row, col, value) format
                values = [int(x.strip()) for x in line[1:-1].split(',')]
                matrix.set_element(values[0], values[1], values[2])

            return matrix
        except Exception as error:
            raise Exception(f"Failed to read matrix file: {file_path}\nError details: {str(error)}")

    def get_element(self, row, col):
        return self.data.get(row, {}).get(col, 0)

    def set_element(self, row, col, value):
        if value == 0:
            if row in self.data:
                if col in self.data[row]:
                    del self.data[row][col]
                if not self.data[row]:  # If row is empty
                    del self.data[row]
        else:
            if row not in self.data:
                self.data[row] = {}
            self.data[row][col] = value

    def get_dimension_string(self):
        return f"{self.rows}x{self.cols}"

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(f"Matrix dimensions must match for addition. Matrix 1 is {self.rows}x{self.cols}, Matrix 2 is {other.rows}x{other.cols}")

        result = SparseMatrix(self.rows, self.cols)

        # Add elements from first matrix
        for row in self.data:
            for col, value in self.data[row].items():
                result.set_element(row, col, value)

        # Add elements from second matrix
        for row in other.data:
            for col, value in other.data[row].items():
                sum_value = result.get_element(row, col) + value
                result.set_element(row, col, sum_value)

        return result

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(f"Matrix dimensions must match for subtraction. Matrix 1 is {self.rows}x{self.cols}, Matrix 2 is {other.rows}x{other.cols}")

        result = SparseMatrix(self.rows, self.cols)

        # Add elements from first matrix
        for row in self.data:
            for col, value in self.data[row].items():
                result.set_element(row, col, value)

        # Subtract elements from second matrix
        for row in other.data:
            for col, value in other.data[row].items():
                diff = result.get_element(row, col) - value
                result.set_element(row, col, diff)

        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError(f"Invalid dimensions for multiplication. Matrix 1 is {self.rows}x{self.cols}, Matrix 2 is {other.rows}x{other.cols}. "
                           f"The number of columns in first matrix ({self.cols}) must equal the number of rows in second matrix ({other.rows})")

        result = SparseMatrix(self.rows, other.cols)

        # Only iterate over non-zero elements
        for row1 in self.data:
            for col1, val1 in self.data[row1].items():
                if col1 in other.data:
                    for col2, val2 in other.data[col1].items():
                        current = result.get_element(row1, col2)
                        result.set_element(row1, col2, current + val1 * val2)

        return result

    def __str__(self):
        result = [f"rows={self.rows}", f"cols={self.cols}"]
        for row in sorted(self.data.keys()):
            for col in sorted(self.data[row].keys()):
                result.append(f"({row}, {col}, {self.data[row][col]})")
        return '\n'.join(result)

def main():
    if len(sys.argv) < 5:
        print("Usage: python sparse-matrix.py <operation> <matrix1_file> <matrix2_file> <output_file>")
        print("Operations available: add, subtract, multiply")
        print("Example: python sparse-matrix.py add matrix1.txt matrix2.txt result.txt")
        sys.exit(1)

    try:
        operation = sys.argv[1]
        matrix1 = SparseMatrix.from_file(sys.argv[2])
        matrix2 = SparseMatrix.from_file(sys.argv[3])
        output_file = sys.argv[4]

        # Display the operation with matrix dimensions
        dim1 = matrix1.get_dimension_string()
        dim2 = matrix2.get_dimension_string()
        print(f"Performing operation: {dim1} {operation} {dim2}")

        if operation == "add":
            result = matrix1.add(matrix2)
        elif operation == "subtract":
            result = matrix1.subtract(matrix2)
        elif operation == "multiply":
            result = matrix1.multiply(matrix2)
        else:
            raise ValueError(f'Invalid operation "{operation}". Valid operations are: add, subtract, or multiply')

        # Write result to output file
        with open(output_file, 'w') as file:
            file.write(str(result))
        print(f'Operation "{operation}" completed successfully. Result written to: {output_file}')

    except Exception as error:
        print("Error:", str(error))
        sys.exit(1)

if __name__ == "__main__":
    main()