#!/usr/bin/python3

"""0-Lockboxes"""

def canUnlockAll(boxes):
    """_Determines if all the boxes can be opened._

    `boxes` is a list of lists
    - A key with the same number as a box opens that box
    - You can assume all keys will be positive integers
        - There can be keys that do not have boxes
    - The first box `boxes[0]` is unlocked
    - Return `True` if all boxes can be opened, else return `False`

    Args:
        boxes (_list_): _a list of lists_
    """

    canUnlockAll = False
    count_b = len(boxes)
    keys = {0: True}

    while(True):
        count_k = len(keys)
        for b in range(count_b):
            if boxes[b] and keys.get(b, False):
                for el in boxes[b]:
                    if el < count_b:
                        keys[el] = True
                    boxes[b] = None
        if not len(keys) > count_k:
            break
    if count_k == count_b:
        canUnlockAll = True
    return canUnlockAll
