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

This heuristic counts how many disks are not currently on the goal peg. It
uses that count as a simple estimate of the remaining work, but does not
consider disk ordering, legal moves, or the additional moves needed to clear
smaller disks from underneath larger ones. It is therefore less detailed than
the first heuristic.

#### Requirements & File Structure:

- Python 3.8 or newer.gi
- No external packages; only Python's standard library is required.

```text
SOURCE/
├── hanoi.py          # Command-line menu
├── search.py         # BFS, A*, and Heuristics
├── tests/
│   └── tests.py      # Tests
└── README.md         # Documentation
```

#### Startup Guide:

Upon loading the folder, run the program with 'python hanoi.py'. This will open a menu in the command line, each algorithm can be executed with it's respective command (A* / BFS), the output will print to the command line.
In order to use either heuristic, simply change the heuristic in this line in the print_a_star_solution function.

```
path = run_a_star(n, admissable_heuristic)
```
