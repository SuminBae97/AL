numpad = {
        1: (1, 1), 2: (2, 1), 3: (3, 1),
        4: (1, 2), 5: (2, 2), 6: (3, 2),
        7: (1, 3), 8: (2, 3), 9: (3, 3),
        '*': (1, 4), 0: (2, 4), '#': (3, 4)
}


def solution(numbers, hand):

    answer=''
    left_part = [1,4,7]
    right_part = [3,6,9]

    #starting_point
    last_left = "*"
    last_right = "#"
    for val in numbers:

        if val in left_part:
            answer+='L'
            last_left = val

        elif val in right_part:
            answer +='R'
            last_right = val

        else:

            left_dis_f = abs(numpad[last_left][0]- numpad[val][0])
            left_dis_s = abs(numpad[last_left][1]- numpad[val][1])
            l_dis = left_dis_f + left_dis_s


            right_dis_f=abs(numpad[last_right][0]- numpad[val][0])
            right_dis_s = abs(numpad[last_right][1] - numpad[val][1])

            r_dis = right_dis_f + right_dis_s

            if l_dis > r_dis:
                answer+='R'
                last_right = val

            elif l_dis < r_dis:
                answer+='L'
                last_left = val

            elif l_dis ==r_dis:

                if hand == "right":
                    answer+="R"
                    last_right = val
                else:
                    answer+="L"
                    last_left = val

    return answer
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],'right'))












