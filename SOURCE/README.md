# Tower of Hanoi

This project solves the Tower of Hanoi problem by implementing both the A* and BFS algorithms.
Two Heuristics have been implemented in order to further compliment both algorithms.
Tests have also been created in order to ensure each algorithm works as expected.

#### Heuristics:

##### Admissable Heuristic:

```
def admissable_heuristic(state, n):
    goal_peg = state[2]
    largest_misplaced = 0

    for disk in range(n):
        if disk not in goal_peg:
            largest_misplaced = disk

    if largest_misplaced == 0:
        return 0
    
    return 2 ** (largest_misplaced - 1) - 1
```

##### Inadmissable Heuristic:
```
def inadmissable_heuristic(state, n):
    goal_peg = state[2]
    misplaced = sum(1 for disk in range(1, n + 1) if disk not in goal_peg)
    return misplaced
```

#### Requirements:

- Python 3.8 or newer.gi
- No external packages; only Python's standard library is required.
