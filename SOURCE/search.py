from collections import deque

INITIAL_STATE = ((1, 2, 3), (), ())
GOAL_STATE = ((), (), (1, 2, 3))

# Defines legal moves and stores them in a list.
def legal_moves(state):
    moves = []

    for src in range(3):
        if not state[src]:
            continue

        disk = state[src][0]
        rest = state[src][1:]

        for dst in range(3):
            if src == dst:
                continue

            if not state[dst] or disk < state[dst][0]:
                new_state = list(state)
                new_state[src] = rest
                new_state[dst] = (disk,) + state[dst]
                moves.append((tuple(new_state), (src, dst)))

    return moves

def make_initial_state(n):
    disks = tuple(range(1, n + 1))
    return (disks, (), ())

def make_goal_state(n):
    disks = tuple(range(1, n + 1))
    return ((), (), disks)

def run_a_star(grid, heuristic):
    pass

# BFS solution.
def run_bfs(n):
    start = make_initial_state(n)
    goal = make_goal_state(n)

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

def print_bfs_solution(n):
    state = make_initial_state(n)
    path = run_bfs(3)
    peg_names = ("A", "B", "C")

    print("Initial State:", state)

    for src, dst in path or []:
        disk = state[src][0]
        updated_state = list(state)
        updated_state[src] = state[src][1:]
        updated_state[dst] = (disk,) + state[dst]
        state = tuple(updated_state)

        print(
            "Move disk",
            disk,
            "from rod",
            peg_names[src],
            "to rod",
            peg_names[dst],
        )

    print("End State:", state)

# Recursive solution.
def run_recursion(n, source, target, aux, total_moves=None):
    if total_moves is None:
        total_moves = []

    if n == 0:
        return len(total_moves)

    run_recursion(n - 1, source, aux, target, total_moves)
    move = (n, source, target)
    total_moves.append(move)
    print("Move disk", n, "from rod", source, "to rod", target)
    run_recursion(n - 1, aux, target, source, total_moves)

if __name__ == "__main__":
    run_recursion(3, "A", "B", "C")
    print_bfs_solution(3)


