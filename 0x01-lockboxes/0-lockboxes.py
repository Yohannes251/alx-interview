#!/usr/bin/python3
"""
    Contains a function that implements lockboxes algorithm
"""

def canUnlockAll(boxes):
    """Returns True if all boxes can be opened False otherwise"""
    opened = [0]
    box = boxes[0]
    while True:
        for j in range(len(box)):
            if not box[j] in opened:
                opened.append(box[j])
                opened_new = 1
        if j == len(box) - 1:
            new_box = []
            for idx in opened:
                new_box += boxes[idx]
            box = new_box
        if opened_new == 0:
            break
        opened_new = 0
    return True if len(opened) == len(boxes) else False
