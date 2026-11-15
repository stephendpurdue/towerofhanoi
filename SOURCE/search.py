from collections import deque

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

def run_a_star(n, heuristic): # TODO
    """ PSEUDOCODE

    start ← make_initial_state(n)
    goal  ← make_goal_state(n)

    open_set ← priority queue
    counter ← 0

    g_score ← dictionary with default value infinity
    g_score[start] ← 0

    parent ← empty dictionary
    move_used ← empty dictionary

    PUSH (priority = heuristic(start, goal),
          tie_breaker = counter,
          state = start)
          INTO open_set

    WHILE open_set is not empty:

        current ← POP state with lowest priority

        IF current = goal:
            path ← empty list

            WHILE current ≠ start:
                APPEND move_used[current] TO path
                current ← parent[current]

            REVERSE path
            RETURN path

        FOR each (next_state, move) IN legal_moves(current):

            tentative_g ← g_score[current] + 1

            IF tentative_g < g_score[next_state]:

                parent[next_state] ← current
                move_used[next_state] ← move
                g_score[next_state] ← tentative_g

                f_score ← tentative_g + heuristic(next_state, goal)

                counter ← counter + 1

                PUSH (priority = f_score,
                      tie_breaker = counter,
                      state = next_state)
                      INTO open_set

    RETURN None"""

def print_a_star_solution(n): # TODO
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


