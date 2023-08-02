#!/usr/bin/python3
"""a module with a canUnlock function"""


def canUnlockAll(boxes):
    """determines wether all boxes can be unlocked"""
    # Special case: If there are no boxes or only one box, it is always True.
    if not boxes or len(boxes) == 1:
        return True

    n = len(boxes)
    visited = set()
    queue = [0]  # Start with the first box (index 0).
    visited.add(0)

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key not in visited and key < n:
                queue.append(key)
                visited.add(key)

    return len(visited) == n
