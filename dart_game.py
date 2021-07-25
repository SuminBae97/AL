def solution(dartResult):
    dartResult = dartResult.replace('10', 'k')
    point = ['10' if i == 'k' else i for i in dartResult]
    letter = ['S', 'D', 'T']
    score = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    bonus = ["*", "#"]
    stack = []

    for i in range(len(point)):
        if point[i] in score:
            stack.append(int(point[i]))
            continue

        if point[i] in letter:
            val = stack.pop()
            val = val ** (letter.index(point[i]) + 1)
            stack.append(val)

        if point[i] in bonus:
            if point[i] == "#":
                val = stack.pop()
                val = -val
                stack.append(val)

            elif point[i] == "*":
                val = stack.pop()
                val = 2 * val
                if len(stack):
                    stack[-1] *= 2
                stack.append(val)

    return sum(stack)