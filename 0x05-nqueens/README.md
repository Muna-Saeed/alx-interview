# N Queens Problem

## Introduction

The “0x05. N queens” project is a classic problem in computer science and mathematics, known for its application of the backtracking algorithm to place N non-attacking queens on an N×N chessboard. To successfully complete this project, you will need to understand several key concepts and have access to resources that will help you grasp the necessary algorithms and techniques.

### Concepts Needed

#### Backtracking Algorithms:
Understanding how backtracking algorithms work to explore all potential solutions to a problem and backtrack when a solution cannot be completed.
- [Backtracking Introduction](https://www.geeksforgeeks.org/backtracking-algorithms/)

#### Recursion:
Using recursive functions to implement backtracking algorithms.
- [Recursion in Python](https://realpython.com/python-recursion/)

#### List Manipulations in Python:
Creating and manipulating lists, especially to store the positions of queens on the board.
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

#### Python Command Line Arguments:
Handling command-line arguments with the sys module.
- [Command Line Arguments in Python](https://docs.python.org/3/library/sys.html#sys.argv)

By studying these concepts and utilizing the resources provided, you will be equipped with the knowledge required to implement an efficient solution to the N queens problem using Python. This project not only tests programming and problem-solving skills but also offers an excellent opportunity to learn about algorithmic thinking and optimization techniques.

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.*)
- All your files must be executable

## Tasks

### 0. N queens (Mandatory)

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

#### Usage
```bash
./0-nqueens.py N
```

#### Example
```bash
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$
```
## Usage

To use this program, you need to run it from the command line. The program expects a single command-line argument, which is the size of the board (N).

```bash
./0-nqueens.py N
Requirements
The program should be executed with exactly one argument.
The argument must be an integer greater than or equal to 4.
If the argument is not valid, the program will print an error message and exit with a status code of 1.
Error Messages
If the user called the program with the wrong number of arguments, print:
```plaintext
Usage: nqueens N
```
followed by a new line, and exit with the status 1.

Where N must be an integer greater or equal to 4. If N is not an integer, print:
```plaintext
N must be a number
```
followed by a new line, and exit with the status 1. If N is smaller than 4, print:
```plaintext
N must be at least 4
```
followed by a new line, and exit with the status 1.

The program should print every possible solution to the problem. One solution per line. Format: see example. You don’t have to print the solutions in a specific order. You are only allowed to import the `sys` module.

## Implementation Details

### Backtracking Algorithm

The program uses a backtracking algorithm to find all possible solutions to the N Queens problem:

1. **is_safe**: This function checks if a queen can be placed at a given position without being attacked by any other queens.
2. **solve_nqueens**: This function initiates the backtracking process and prints all valid solutions.
3. **backtrack**: This recursive function attempts to place queens row by row and backtracks if a placement leads to a conflict.
4. **print_solution**: This function formats and prints each valid solution.

### Python Version

The code is written for Python 3 and should be executed in an environment where Python 3.4.3 or later is available.

### PEP 8

The code follows the PEP 8 style guide for Python code.

## Project Structure

- `0-nqueens.py`: The main executable Python script that solves the N Queens problem.
- `README.md`: This file, providing an overview and instructions for the project.

## License

This project is open source and available under the MIT License.

## Author

This project was created as part of the ALX Interview Preparation curriculum.

## Additional Resources
- Mock Interview

This `README.md` includes detailed project information, usage instructions, and links to additional resources for understanding the required concepts.
