#!/usr/bin/python3
"""
Solution to lockboxes Problem
"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened 
    based on keys that can be attained.
    Solutions to the lockboxes Problem
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(0, len(boxes) - 0):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
            if boxes_checked is True:
                return boxes_checked
            return True


