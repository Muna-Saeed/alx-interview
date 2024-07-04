# Island Perimeter

## Project Overview

The "Island Perimeter" project involves calculating the perimeter of an island in a grid. The grid is represented by a 2D array of integers where `0` represents water and `1` represents land. The goal is to determine the perimeter of the island by analyzing the grid.

## Concepts Needed

### 2D Arrays (Matrices)

- **Accessing and Iterating**: Understanding how to access and iterate over elements in a 2D array.
- **Navigating Adjacent Cells**: Knowing how to navigate through adjacent cells (horizontally and vertically).

### Conditional Logic

- **Applying Conditions**: Determining whether a cell contributes to the perimeter of the island by applying specific conditions.

### Counting Techniques

- **Edge Counting**: Developing a method to count the edges that contribute to the island’s perimeter.

### Problem-Solving Strategies

- **Breaking Down the Problem**: Identifying land cells and calculating their contribution to the perimeter by breaking down the problem into smaller tasks.

### Python Programming

- **Nested Loops**: Using nested loops to iterate over grid cells.
- **Conditional Statements**: Using conditional statements to check the status of adjacent cells.

## Resources

### Python Official Documentation

- **Nested Lists**: Understanding how to work with lists within lists in Python.
  - [Python Documentation on Lists](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions)

### GeeksforGeeks Articles

- **Python Multi-dimensional Arrays**: A guide to working with 2D arrays in Python effectively.
  - [GeeksforGeeks on Multi-dimensional Arrays](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/)

### TutorialsPoint

- **Python Lists**: Explains how to create, access, and manipulate lists in Python, which is essential for working with a grid.
  - [TutorialsPoint on Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)

### YouTube Tutorials

- **Python 2D arrays and lists**
  - [YouTube Tutorial on Python 2D Arrays](https://www.youtube.com/results?search_query=python+2d+arrays+and+lists)

By understanding these concepts and utilizing the provided resources, you will be equipped to approach the problem methodically. You’ll need to iterate over the grid, apply logical operations to identify the perimeter of the island, and account for the specific conditions described in the task. This project not only tests your algorithmic thinking but also reinforces your ability to manipulate data structures and apply logical reasoning to solve problems.

## Additional Resources

- [Mock Technical Interviews](https://youtu.be/fFgEM6CMQc4)

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7)
- You are not allowed to import any module
- All modules and functions must be documented
- All your files must be executable

## Tasks

### 0. Island Perimeter

**Mandatory**

Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in the grid.

- `grid` is a list of list of integers:
  - `0` represents water
  - `1` represents land
  - Each cell is square, with a side length of 1
  - Cells are connected horizontally/vertically (not diagonally)
  - The grid is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing)
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island)

#### Example

```python
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Output should be 12
```

## Repository

- **GitHub Repository**: `alx-interview`
- **Directory**: `0x09-island_perimeter`
- **File**: `0-island_perimeter.py`
```

This `README.md` file outlines the necessary concepts, resources, and requirements for the Island Perimeter project, providing a clear guide for understanding and implementing the solution.
