def solution(phone_number):
    l = len(phone_number)
    star = "*"*(l-4)
    return star+phone_number[-4:]