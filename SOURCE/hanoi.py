from heapq import heappop, heappush
from collections import defaultdict
from search import *
from heuristics import *

# Initial State: All three disks on left most peg in ascending order.
# Goal State: All three disks on right most peg in ascending order.

if __name__ == "__main__":
    while True:
        current_state = INITIAL_STATE
        print(INITIAL_STATE)

        cmd = input("Command: \nBFS \nA* \nRecursion \nSettings \nExit \nPlease enter a command: ")
        if cmd.lower() == "bfs":
            run_bfs(3)
        elif cmd.lower() == "a*":
            pass
        elif cmd.lower() == "recursion":
            run_recursion(3, "A", "B", "C")
        elif cmd.lower() == "settings":
            pass
        elif cmd.lower() == "exit":
            break
        else:
            print("Command does not exist, please enter a valid command.")
            continue
        input("Press enter to continue to the menu.")