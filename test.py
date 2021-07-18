
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
def first_person(n):
    answer = []

    for i in range(n):
        if (i + 1) % 5 == 1:
            answer.append(1)
        elif (i + 1) % 5 == 2:
            answer.append(2)
        elif (i + 1) % 5 == 3:
            answer.append(3)

        elif (i + 1) % 5 == 4:
            answer.append(4)
        elif (i + 1) % 5 == 0:
            answer.append(5)

    return answer

def second_person(n):
    answers = [2 for _ in range(10000)]
    for i in range(1,10000,8):
        answers[i]=1

    for i in range(3,10000,8):
        answers[i]=3

    for i in range(5,10000,8):
        answers[i]=4

    for i in range(7,10000,8):
        answers[i]=5

    return answers[:n]

def third_person(n):
    answers = [0 for _ in range(10000)]

    for i in range(0,10000,10):
        answers[i] = 3
        answers[i+1] =3

    for i in range(2,10000,10):
        answers[i] =1
        answers[i+1]=1

    for i in range(4,10000,10):
        answers[i]=2
        answers[i+1]=2

    for i in range(6,10000,10):
        answers[i]=4
        answers[i+1]=4

    for i in range(8,10000,10):
        answers[i]=5
        answers[i+1]=5


    return answers[:n]





def solution(answers):
    answer = []
    n = len(answers)
    first_answer = first_person(n)
    second_answer = second_person(n)
    third_answer = third_person(n)

    count_1 = 0
    count_2 = 0
    count_3 = 0

    for val,ans in zip(first_answer,answers):
        if val==ans:
            count_1+=1

    for val,ans in zip(second_answer,answers):
        if val==ans:
            count_2+=1

    for val,ans in zip(third_answer,answers):
        if val==ans:
            count_3+=1


    answer_temp = [count_1,count_2,count_3]

    for person, score in enumerate(answer_temp):
        if score == max(answer_temp):
            answer.append(person+1)

    return answer
