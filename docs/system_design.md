# System Design

## Problem statement

A user needs to find a route between a start cell and a goal cell in a grid containing blocked cells. The system should determine whether a route exists, visualize the route, and explain the result in plain language.

## Representation

- **State:** the current grid coordinate `(row, column)`.
- **Initial state:** the start coordinate, shown as `S`.
- **Goal state:** the destination coordinate, shown as `G`.
- **Actions:** move one cell up, right, down, or left.
- **Constraints:** remain inside the grid and do not enter a wall.
- **Step cost:** one for each move. Therefore, BFS finds a minimum-step path when one exists.

## Search algorithms

### Breadth-First Search (BFS)

BFS uses a FIFO queue and expands the shallowest discovered states first. It is complete on this finite grid and returns a minimum-step route because each move has equal cost.

### Depth-First Search (DFS)

DFS uses a LIFO stack and follows one branch deeper before backtracking. It can find a route, but does not guarantee a minimum-step route.

## Rule-based expert system

The current rules are deliberately simple and transparent:

1. IF start equals goal, THEN report that the goal is already reached.
2. IF no route is found, THEN report that the goal is unreachable in the current grid and advise the user to inspect walls that may disconnect the route.
3. IF BFS finds a route, THEN explain that it is a minimum-step route in this unweighted grid.
4. IF DFS finds a route, THEN explain that it is valid but may not be the shortest route.

## Evaluation plan

- Test a clear grid with a known minimum path length.
- Test a blocked start/goal separation where no route exists.
- Test BFS and DFS on the same maze.
- Check that the path begins at the start, ends at the goal, and never crosses a wall.
- Record path length, explored node count, and runtime. Runtime is informational because it depends on the computer and grid.
