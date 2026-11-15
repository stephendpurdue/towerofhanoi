"""FUNCTION heuristic(state, goal):

    misplaced_disks ← 0

    FOR each peg IN state:
        FOR each disk IN peg:
            IF disk is not on its goal peg:
                misplaced_disks ← misplaced_disks + 1

    RETURN misplaced_disks"""
