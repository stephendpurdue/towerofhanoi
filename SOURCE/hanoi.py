from heapq import heappop, heappush
from collections import defaultdict
from search import *
from heuristics import *

# Initial State: All three disks on left most peg in ascending order.
# Goal State: All three disks on right most peg in ascending order.

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




