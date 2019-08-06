from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
from typing_extensions import Protocol
from heapq import heappush, heappop

T = TypeVar('T')


def linear_search(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True

    return False


C = TypeVar('C', bound='Comparable')


class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        ...

    def __lt__(self: C, other: C) -> bool:
        ...

    def __gt__(self: C, other: C) -> bool:
        return (not self < other) and self != other

    def __le__(self: C, other: C) -> bool:
        return self < other or self == other

    def __ge__(self: C, other: C) -> bool:
        return not self < other


def binary_search(sequence: Sequence[C], key: C) -> bool:
    low: int = 0
    high: int = len(sequence) - 1

    while low <= high:
        mid: int = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1  # key is not in lower part, readjust `low`
        elif sequence[mid] > key:
            high = mid - 1  # key is not in higher part, readjust `high`
        else:
            return True

    return False


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container  # true for empty containers

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()  # LIFO

    def __repr__(self) -> str:
        return repr(self._container)


class Queue(Generic[T]):
    def __init__(self) -> None:
        self._container: Deque[T] = Deque()

    @property
    def empty(self) -> bool:
        return not self._container  # true for empty containers

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.popleft()  # FIFO

    def __repr__(self) -> str:
        return repr(self._container)


class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[T], cost: float = 0.0, heuristic: float = 0.0) -> None:
        self.state: T = state
        self.parent: Optional[T] = parent
        self.cost: float = cost
        self.heuristic: float = heuristic

    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def dfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    # frontier is where we've yet to go
    frontier: Stack[T] = Stack()
    frontier.push(Node(initial, None))

    # explored is where we have been
    explored: Set[T] = {initial}

    # keep going while there is more to explore
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state

        # if we found the goal, we're done
        if goal_test(current_state):
            return current_node

        # check where we can go next and haven't explored
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))

    return None

# The queue is a list of nodes each node has a parent. Basically building a tree in memory.


def bfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    # frontier is where we've yet to go
    frontier: Queue[T] = Queue()
    frontier.push(Node(initial, None))

    # explored is where we have been
    explored: Set[T] = {initial}

    # keep going while there is more to explore
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state

        # if we found the goal, we're done
        if goal_test(current_state):
            return current_node

        # check where we can go next and haven't explored
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))

            print([(a.row, a.column) for a in node_to_path(current_node)])

    return None


def node_to_path(node: Node[T]) -> List[T]:
    path: List[T] = [node.state]

    # work backwards from end to front
    while node.parent is not None:
        node = node.parent
        path.append(node.state)

    path.reverse()
    return path


# if __name__ == "__main__":
#     print(linear_search([1, 5, 15, 20], 5))
#     print(binary_search(['a', 'd', 'e', 'f', 'z'], 'f'))
#     print(binary_search(['john', 'mark', 'ronald', 'sarah'], 'sheila'))
