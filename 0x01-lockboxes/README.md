# 0x01-lockboxes

## Author

Tadala N. Kapengule

## Prerequisites

1. Lists and List Manipulation

- Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically.
- [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)

2. Graph theory basics

- Although not explicitly required, knowledge of graph theory (especially concepts related to traversal algorithms like Depth-First Search or Breadth-First Search) can be very helpful in solving this problem, as the boxes and keys can be thought of as nodes and edges in a graph.
- [Graph Theory (Khan Academy)](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs)

3. Algorithmic complexity

- Understanding the time and space complexity of your solution is important, as it can help in writing more efficient algorithms.
- [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/asymptotic-notation-and-analysis-based-on-input-size-of-algorithms/)

4. Recursion

- Some solutions might require a recursive approach to traverse through the boxes and keys.
- [Recursion in Python (Real Python)](https://realpython.com/python-recursion/)

5. Queue and Stack

- Knowing how to use queues and stacks is crucial if implementing a breadth-first search (BFS) or depth-first search (DFS) algorithm to traverse through the keys and boxes.
- [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/queue-in-python/)

6. Sets and operations

- Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process.
- [Python Sets (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html#sets)

7. Mock Interview

- [Mock interview](https://www.youtube.com/watch?v=V8DGdPkBBxg)

## Tasks

### 0. Lockboxes

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- Prototype: `def canUnlockAll(boxes)`
- `boxes` is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- - There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return `True` if all boxes can be opened, else return `False`

__File__
`0-lockboxes.py`
