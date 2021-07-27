import math
from collections import Counter


def solution(progress, speeds):
    left = []
    remainder = []
    full = [100 for _ in range(len(progress))]

    for a, b in zip(full, progress):
        left.append(a - b)

    for a, v in zip(left, speeds):
        remainder.append(math.ceil(a / v))

    for i in range(len(remainder)):
        try:
            if remainder[i] > remainder[i + 1]:
                remainder[i + 1] = remainder[i]

        except IndexError:
            break

    a = Counter(remainder)
    return list(a.values())
