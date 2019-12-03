def solution(genres, plays):
    d = dict()
    for i in range(len(genres)) :
        try:
            d[genres[i]][0][i] = plays[i]
            #장르내 고유번호 해시에 +
            d[genres[i]][1] += plays[i]
            #장르 고유 재생수에 +
        except:
            d[genres[i]]=list()
            d[genres[i]].append(dict())
            d[genres[i]][0][i] = plays[i]
            d[genres[i]] .append(plays[i])
    d_sorted = sorted(d.items(), key = lambda x:x[1][1])
    answer = []
    return answer
