def bsearchF(arr, h) :
    start = 0
    end = h

    while(start<end) :
        h = (start + end + 1) // 2 # mid
        if (h<= arr[h-1]):
            start = h
        else:
            end = h -1

    return start

def solution(citations):
    n_max = len(citations)
    citations.sort(reverse = True)
    print(citations)
    answer = bsearchF(citations, n_max)

    return answer
