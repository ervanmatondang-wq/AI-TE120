"""Graph-search algorithms for a grid maze.

Coordinates use (row, column). Walls are coordinates that cannot be visited.
The maze is unweighted, so BFS finds a shortest path in number of moves.
"""

from collections import deque
from dataclasses import dataclass
from time import perf_counter
from typing import Iterable

Coordinate = tuple[int, int]


@dataclass
class SearchResult:
    path: list[Coordinate]
    explored: list[Coordinate]
    elapsed_ms: float

    @property
    def found(self) -> bool:
        return bool(self.path)

    @property
    def steps(self) -> int:
        return max(0, len(self.path) - 1)

    @property
    def visited_count(self) -> int:
        return len(self.explored)


def _neighbors(cell: Coordinate, rows: int, cols: int, walls: set[Coordinate]) -> Iterable[Coordinate]:
    row, col = cell
    # Fixed order makes the demo repeatable: up, right, down, left.
    for nxt in ((row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)):
        r, c = nxt
        if 0 <= r < rows and 0 <= c < cols and nxt not in walls:
            yield nxt


def _reconstruct_path(parent: dict[Coordinate, Coordinate | None], goal: Coordinate) -> list[Coordinate]:
    if goal not in parent:
        return []
    path: list[Coordinate] = []
    current: Coordinate | None = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path


def breadth_first_search(
    rows: int,
    cols: int,
    walls: set[Coordinate],
    start: Coordinate,
    goal: Coordinate,
) -> SearchResult:
    """Find a shortest path using Breadth-First Search (BFS)."""
    started = perf_counter()
    if start in walls or goal in walls:
        return SearchResult([], [], (perf_counter() - started) * 1000)
    queue = deque([start])
    parent: dict[Coordinate, Coordinate | None] = {start: None}
    explored: list[Coordinate] = []

    while queue:
        current = queue.popleft()
        explored.append(current)
        if current == goal:
            break
        for nxt in _neighbors(current, rows, cols, walls):
            if nxt not in parent:
                parent[nxt] = current
                queue.append(nxt)

    path = _reconstruct_path(parent, goal)
    return SearchResult(path, explored, (perf_counter() - started) * 1000)


def depth_first_search(
    rows: int,
    cols: int,
    walls: set[Coordinate],
    start: Coordinate,
    goal: Coordinate,
) -> SearchResult:
    """Find a path using Depth-First Search (DFS); it may not be shortest."""
    started = perf_counter()
    if start in walls or goal in walls:
        return SearchResult([], [], (perf_counter() - started) * 1000)
    stack = [start]
    parent: dict[Coordinate, Coordinate | None] = {start: None}
    explored: list[Coordinate] = []

    while stack:
        current = stack.pop()
        explored.append(current)
        if current == goal:
            break
        # Reverse insertion order so the visual traversal follows the same
        # up/right/down/left preference as BFS when possible.
        next_cells = list(_neighbors(current, rows, cols, walls))
        for nxt in reversed(next_cells):
            if nxt not in parent:
                parent[nxt] = current
                stack.append(nxt)

    path = _reconstruct_path(parent, goal)
    return SearchResult(path, explored, (perf_counter() - started) * 1000)
