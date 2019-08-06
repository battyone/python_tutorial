# %%
from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
import generic_search as gs


class Cell(str, Enum):
    EMPTY = ' '
    BLOCKED = 'X'
    START = 'S'
    GOAL = 'G'
    PATH = '*'


class MazeLocation(NamedTuple):
    row: int
    column: int


class Maze:
    def __init__(self, rows: int = 10, columns: int = 10, sparseness: float = 0.2, start: MazeLocation = MazeLocation(0, 0), goal: MazeLocation = MazeLocation(9, 9)) -> None:
        # initialize basic
        self._rows: int = rows
        self._columns: int = columns

        self._sparseness: float = sparseness

        self.start: MazeLocation = start
        self.goal: MazeLocation = goal

        # fill grid with empty cells
        self._grid: List[List[Cell]] = [
            [Cell.EMPTY for c in range(columns)] for r in range(rows)]

        # populate the grid with blocked cells
        self._randomly_fill_grid()
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_fill_grid(self):
        for r in range(self._rows):
            for c in range(self._columns):
                if random.uniform(0, 1.0) < self._sparseness:
                    self._grid[r][c] = Cell.BLOCKED

    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self.goal

    def successors(self, ml: MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []

        # right
        if (ml.row + 1) < self._rows and self._grid[ml.row+1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row+1, ml.column))

        # left
        if (ml.row - 1) >= 0 and self._grid[ml.row-1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row-1, ml.column))

        # down
        if (ml.column + 1) < self._columns and self._grid[ml.row][ml.column+1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column+1))

        # down
        if (ml.column - 1) >= 0 and self._grid[ml.row][ml.column-1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column-1))

        return locations

    def mark(self, path: List[MazeLocation]):
        for loc in path:
            self._grid[loc.row][loc.column] = Cell.PATH

        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path: List[MazeLocation]):
        for loc in path:
            self._grid[loc.row][loc.column] = Cell.EMPTY

        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def __str__(self) -> str:
        output: str = ''
        for row in self._grid:
            output += ''.join([c.value for c in row]) + '\n'

        return output


# %%
# maze: Maze = Maze(20, 20, 0.25, MazeLocation(0, 0), MazeLocation(19, 19))
# print(maze)

# ml: MazeLocation = MazeLocation(1, 1)
# su = maze.successors(ml)
# print(len(su))

# %%
if __name__ == "__main__":
    m: Maze = Maze(5, 5, 0.2, MazeLocation(0, 0), MazeLocation(4, 4))
    print(m)

    # solution1: Optional[gs.Node[MazeLocation]] = gs.dfs(m.start, m.goal_test,
    #                                                     m.successors)

    # if solution1 is None:
    #     print('No DFS solution found')
    # else:
    #     path1: List[MazeLocation] = gs.node_to_path(solution1)
    #     m.mark(path1)
    #     print(m)
    #     m.clear(path1)

    solution2: Optional[gs.Node[MazeLocation]] = gs.bfs(m.start, m.goal_test,
                                                        m.successors)

    if solution2 is None:
        print('No BFS solution found')
    else:
        path2: List[MazeLocation] = gs.node_to_path(solution2)
        m.mark(path2)
        print(m)
        m.clear(path2)
