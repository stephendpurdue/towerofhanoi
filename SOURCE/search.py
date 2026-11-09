from hanoi import INITIAL_STATE, GOAL_STATE, legal_moves
from collections import deque

def run_a_star(grid, heuristic):
    pass

# BFS solution.
def run_bfs(n):
    start = INITIAL_STATE
    goal = GOAL_STATE

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        for next_state, move in legal_moves(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [move]))

    return None

# Recursive solution.
def run_recursion(n, source, target, aux):
    if n == 0:
        return
    run_recursion(n -1, source, aux, target)
    print("Move disk", n, "from rod", source, "to rod", target)
    run_recursion(n - 1, aux, target, source)

run_recursion(3, "A", "B", "C")



