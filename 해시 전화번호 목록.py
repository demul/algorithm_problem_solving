def solution(phone_book):
    d = dict()
    for i in phone_book :
        d[i] =1

    for i in phone_book :
        for j in range(len(i)) :
            try :
                d[i[:j]]
                return False
            except :
                continue
    return True
