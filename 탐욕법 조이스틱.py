def min_dist(ch):
    return min(ch, abs(ch - 26))


def solution(name):
    answer = 0

    for i in name:
        print(ord(i)-ord('A'))
        answer += min_dist(ord(i)-ord('A'))


    return answer

print(solution("JEROEN"))
