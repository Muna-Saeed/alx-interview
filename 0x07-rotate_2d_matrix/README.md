# 0x07. Rotate 2D Matrix

## Description

For the “0. Rotate 2D Matrix” project, you are tasked with implementing an in-place algorithm to rotate an `n x n` 2D matrix by 90 degrees clockwise. This challenge requires a good understanding of matrix manipulation and in-place operations in Python. Below are the key concepts and resources that you need to grasp in order to successfully complete this project.

## Concepts Needed

### Matrix Representation in Python

- Understanding how 2D matrices are represented using lists of lists in Python.
- Accessing and modifying elements in a 2D matrix.

### In-place Operations

- Performing operations on data without creating a copy of the data structure.
- The importance of minimizing space complexity by modifying the matrix in place.

### Matrix Transposition

- Understanding the concept of transposing a matrix (swapping rows and columns).
- Implementing matrix transposition as a step in the rotation process.

### Reversing Rows in a Matrix

- Manipulating rows of a matrix by reversing their order as part of the rotation process.

### Nested Loops

- Using nested loops to iterate through 2D data structures like matrices.
- Modifying elements within nested loops to achieve the desired rotation.

## Learning Objectives

- Understand how 2D matrices are represented using lists of lists in Python.
- Perform operations on data without creating a copy of the data structure.
- Transpose a matrix (swap rows and columns).
- Reverse rows in a matrix.
- Utilize nested loops to iterate through 2D data structures.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.10)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should use the `pycodestyle` style (version 2.8.0)
- No imports allowed
- All modules and functions must be documented
- All files must be executable

## Task

### 0. Rotate 2D Matrix

Given an `n x n` 2D matrix, rotate it 90 degrees clockwise.

#### Prototype
```python
def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in place.
    
    :param matrix: List of lists representing the 2D matrix
    """
    pass
```

#### Example

```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)
```

#### Expected Output

```python
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Implementation

The function first transposes the matrix and then reverses each row to achieve the 90-degree clockwise rotation.

### Transpose the Matrix
Swap the element at position `(i, j)` with the element at position `(j, i)`.

### Reverse Each Row
After transposing, reverse each row to complete the rotation.

## Usage

To run the script, ensure it is executable and run it using Python:

```bash
chmod +x 0-rotate_2d_matrix.py
./0-rotate_2d_matrix.py
```

This will output the rotated matrix as expected.

## Resources

### Python Official Documentation

- [Data Structures (list comprehensions, nested list comprehension)](https://docs.python.org/3/tutorial/datastructures.html)
- [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### GeeksforGeeks Articles

- [Inplace rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- [Transpose a matrix in Single line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)

### TutorialsPoint

- [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm) for basics of list manipulation in Python.

By understanding these concepts and utilizing the provided resources, you will be able to approach the problem methodically, first transposing the matrix and then reversing each row to achieve a 90-degree clockwise rotation. This project not only tests your ability to manipulate 2D matrices but also challenges you to think about optimizing your solution to operate in-place, thus improving your problem-solving and algorithmic thinking skills in Python.

## Additional Resources

- [Mock Technical Interview](https://www.youtube.com/watch?v=yM9Xbi-MigE)

## Author

Muna Saeed - [GitHub Profile](https://github.com/Muna-Saeed)
This `README.md` includes all the necessary sections, detailing the concepts needed and resources to successfully complete the project.
