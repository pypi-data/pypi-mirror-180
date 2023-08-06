# Maze Generation & Solving
Generate/Solve Maze of any dimension using DFS and search algorithms like, Dijkstra, etc.


## Features
- Create maze of different sizes.
- Solve maze using path finding algorithm like Dijkstra(adding more later).


## Usage
This module provides 2 functions, create(...) and search(...). Both of these functions require some parameter that needs to be given by the user. Let's start by importing module in your project,
```py
import maze_generator_and_solver as mgs
```

### Generate/Create a maze
There are 2 ways of using the create(...) function to generate a maze, both of them return same structure so you can use either of them as per the need.
```py
#definition:
create(width=3, height=3, cellSize=1) # width (default: 3), height (default: 3), cellsize (default: 1)
```
```py
#use:
maze = mgs.create(3, 3) # to create a maze of (5 x 5) grid
maze = mgs.create(3, 5) # to create a maze of (3 x 5) grid
maze = mgs.create(90, 90, 30) # to create a maze of (3 x 3) grid
maze = mgs.create(90, 150, 30) # to create a maze of (3 x 5) grid

# all these functions return the same structures, an array and a Graph objec
```
scroll down to get a better understanding with the help of an example

### Solve the maze
To search/solve the maze use the search(...) function,
```py
#definition:
search(graph, root, target, searchAlgoId=1)
# graph: the graph object returned by 'create(...) function', root: starting index,
# target: ending index, searchAlgoId: the id the search algorithm being used (default: 1[dijkstra])
```
```py
#use:
# 'maze' was defined above when create function was called
path = mgs.search(maze["mazeGraph"], 0, maze["mazeGraph"].v-1) # retuns a stack object that contains the solution/path
```
scroll down to get a better understanding with the help of an example

#### Search Algorithm IDs
<table>
  <tr>
    <th>Algorithm ID</th>
    <th>Search Algorithm</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Dijkstra</td>
  </tr>
</table>
More algorithms will be added soon ;p


## Example
Taking this (3x3)maze as an example. on the left(unsolved) and on the right, you can see it is solved.
<img alt="maze" src="https://github.com/0-harshit-0/maze/blob/b3db9ca4a223457e2abaa2037a0676aaf55486b8/assets/maze-npm.png?raw=true" />

- The create(...) function returns 2 structure, one is a simple 1D Array and the other one is a custom Graph structure.
  - The array contains maze/grid index in the order they should be visited (including bactracked indexes). This is useful if you want to create some kind of animation to create a maze.
  - The Graph, as the name suggest, will return an object that has a Map object(adjList). This Map object maps all the index connected to each other.
```py
[0,1,4,5,8,7,6,3,6,7,8,5,2,5,4,1,0] #mazeArr
{"v":9,"AdjList":{Map(9) 0: {0 => GNode}, ...},"length":9} #mazeGraph
# GNode: {d: Set(..), visited: true|false}
```
NOTE: create(...) use randomized DFS, so a (3x3) maze created on your system might return some different values.

- The search(...) function returns a custom Stack object, it contains the array(stackArray) that will provide the solution / path to take from root(0) to target(8).
```py
[0,1,4,5,8] #stackArr
```

That's it, you are ready to create and solve maze :smile:. You can play with a working maze generator/solver at https:#0-harshit-0.github.io/maze
