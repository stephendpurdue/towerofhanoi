from hanoi import INITIAL_STATE, GOAL_STATE, legal_moves
from collections import deque

def A_Star(grid, heuristic):
    pass
    




# BFS solution.
def BFS(n):
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
def recursion(n, source, target, aux):
    if n == 0:
        return
    recursion(n -1, source, aux, target)
    print("Move disk", n, "from rod", source, "to rod", target)
    recursion(n - 1, aux, target, source)

recursion(3, "A", "B", "C")



