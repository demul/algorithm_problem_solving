def solution(clothes):
    d = dict()
    for i in clothes :
        try:
            d[i[1]] = d[i[1]] + 1
        except:
            d[i[1]] = 1

    answer = 1
    for i in d.values() :
        answer *= (i + 1)

    return answer-1
