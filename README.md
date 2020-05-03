# Maze-Solver

This project uses `wall-follower` and `A*` algorithms to solve the maze problem implemented by python, and compares the efficiency of two algorithms.
This is a final project for CS 572 Heuristic Problem.

![image](https://github.com/Ronaldzzzzz/Maze-Solver/blob/main/image/image.jpg)

## Technologies

* Python 3.8
* [PrettyTable](https://github.com/jazzband/prettytable) - a Python library print a pretty table.

## Description

This project is more focusing on the algorithm part, which means some of the implements may be simplified, especially the maze building part.

### Points (location)

At first, you need to specify points in the maze and edit the `mapName.txt` file.

```shell
0   0   X
1   0   Y
2   0   
3   0   C
4   0   
5   0   
6   0   
...
```

For example, point `X` is located on `(0, 0)` in the maze, which is the left top corner.

### Wall

In the `maze.py`, which is the main file, there is a maze array for build the maze.
The martix uses binary to indicate the wall for each node.

![node](https://github.com/Ronaldzzzzz/Maze-Solver/blob/main/image/node.jpg)

For example, the node has two walls, top and left.
Starting from the top, and clockwise to left, each wall represents a bit for binary.
That means, top will be the first(2^0) bit and the left will be the forth(2^4) bit for a binary number, which is 9(1001).
Follow this rule, complete the whole maze by a decimal number.

### Identify States

This project uses the following states to indicate the state of the mouse at the current node.

* Initial state:
The initial state will be point A. Check it using the points table.

* Goal state:
The goal state will be any given point. The default point will be point G. Also can be checked using the points table.

* Goal test
Use the value of the x-axis and y-axis to access the point table then we can get the point which the mouse is at.

* Solution cost
Use a global variable to count the girds the agent traversed.

![states](https://github.com/Ronaldzzzzz/Maze-Solver/blob/main/image/states.jpg)

## Conclusion

![result](https://github.com/Ronaldzzzzz/Maze-Solver/blob/main/image/result.jpg)
