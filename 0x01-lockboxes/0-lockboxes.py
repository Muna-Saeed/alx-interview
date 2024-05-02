#!/usr/bin/python3
'''
using a breadth-first search (BFS) algorithm to solve this task.
'''


def canUnlockAll(boxes):
    # Initialize a set to keep track of visited boxes
    visited = set()

    # Initialize a queue with the first box (index 0)
    queue = [0]

    # Mark the first box as visited
    visited.add(0)

    # While there are boxes in the queue
    while queue:
        # Pop the box from the queue
        current_box = queue.pop(0)

        # Iterate through keys in the current box
        for key in boxes[current_box]:
            # If the key opens a new box and that box hasn't been visited yet
            if key < len(boxes) and key not in visited:
                # Mark the box as visited
                visited.add(key)
                # Add the new box to the queue
                queue.append(key)

    # If all boxes have been visited, return True
    return len(visited) == len(boxes)
