from collections import deque
from itertools import count
import heapq

# Helper functions.
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

# Heuristics
def admissable_heuristic(state, n):

    # Moving disk k requires first moving the k - 1 smaller disks,
    # which takes at least 2^(k - 1) - 1 moves.
    goal_peg = state[2]
    largest_misplaced = 0

    for disk in range(n):
        if disk not in goal_peg:
            largest_misplaced = disk

    if largest_misplaced == 0:
        return 0
    
    return 2 ** (largest_misplaced - 1) - 1


def inadmissable_heuristic(state, n):

    # This is not admissible because it can overestimate the remaining moves.
    goal_peg = state[2]
    misplaced = sum(1 for disk in range(1, n + 1) if disk not in goal_peg)
    return misplaced

# A* solution
def run_a_star(n, heuristic): # TODO

    start = make_initial_state(3)
    goal = make_goal_state(3)

    counter = count()
    h0 = admissable_heuristic(start, n)
    h1 = inadmissable_heuristic(start, n)
    open_heap = [(h0, next(counter), 0, start, [])]
    best = {start: 0}

    while open_heap:
        f, _, g, state, path = heapq.heappop(open_heap)

        if state == goal:
            return path

        if g > best.get(state, float("inf")):
            continue

        for next_state, move in legal_moves(state):
            next_g = g + 1

            if next_g >= best.get(next_state, float("inf")):
                continue

            best[next_state] = next_g
            h = heuristic(next_state, n)
            next_path = path + [move]

            heapq.heappush(
                open_heap,
                (next_g + h, next(counter), next_g, next_state, next_path)
            )
    return None

def print_a_star_solution(n): # TODO
    state = make_initial_state(n)
    path = run_a_star(n, admissable_heuristic)
    peg_names = ("A", "B", "C")

    print("Initial State:", state)

    for src, dst in path or []:
        disk = state[src][0]
        updated_state = list(state)
        updated_state[src] = state[src][1:]
        updated_state[dst] = (disk,) + state[dst]
        state = tuple(updated_state)

        print("Move disk", disk, "from rod", peg_names[src], "to_rod", peg_names[dst])

    print("End State: ", state)

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


