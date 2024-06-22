# Making Change

## Description
This project involves solving the classic coin change problem using dynamic programming. The objective is to determine the fewest number of coins needed to make up a given total amount using a list of coin denominations.

## Requirements
- All code will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the PEP 8 style (version 1.7.x).
- All your files must be executable.

## Concepts Covered
- **Greedy Algorithms**: Understanding the basics and limitations.
- **Dynamic Programming**: Solving optimization problems with overlapping subproblems and optimal substructure.
- **Algorithmic Complexity**: Analyzing time and space complexity for efficiency.
- **Problem-Solving Strategies**: Breaking down problems into manageable subproblems and iterative vs. recursive approaches.
- **Python Programming**: Manipulating lists, using list comprehensions, and implementing efficient functions.

## Resources
### Python Official Documentation
- [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (for loops, if statements)

### GeeksforGeeks Articles
- [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
- [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)

### YouTube Tutorials
- [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=Y0ZqKpToTic) for a visual and step-by-step explanation of the dynamic programming approach.

By thoroughly understanding these concepts and utilizing the provided resources, you will be well-prepared to tackle the coin change problem. You will need to decide whether a greedy algorithm suffices for your particular set of coin denominations or if a more comprehensive dynamic programming approach is necessary to ensure correctness and efficiency. This project not only tests algorithmic skills but also reinforces the importance of choosing the right strategy based on problem constraints.

### Additional Resources
- [Mock Technical Interview] (https://youtu.be/9BSSIsJ-fWg)

## Usage
To use the `makeChange` function, follow the instructions below:

### Function Prototype
```python
def makeChange(coins, total):
```

### Parameters
- `coins`: A list of integers representing the values of the coins in your possession.
- `total`: An integer representing the total amount to be made with the coins.

### Return
- The function returns the fewest number of coins needed to meet the total.
- If the total is 0 or less, it returns 0.
- If the total cannot be met by any number of coins you have, it returns -1.

### Example
```python
makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Expected output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
```

## Files
- `0-making_change.py`: Contains the implementation of the `makeChange` function.
- `0-main.py`: Contains test cases to test the `makeChange` function.

## How to Run
1. Make sure your files are executable:
   ```bash
   chmod +x 0-making_change.py
   chmod +x 0-main.py
   ```
2. Run the main file to see the results of the test cases:
   ```bash
   ./0-main.py
   ```

## Author
- **Muna* - Initial work

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This `README.md` now includes the necessary resources and additional content, providing a comprehensive overview of the project, including concepts covered, usage instructions, and resources for further understanding.
