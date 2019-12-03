import itertools


def solution(baseball):
    cnt = 0
    brute_list = list(map(''.join, itertools.permutations([str(z) for z in range(1,10)], 3)))

    for i in brute_list:
        dir_ad_tab = [-1 for p in range(10)]
        for idx, val in enumerate(i):
            dir_ad_tab[int(val)] = idx
        for j in baseball:
            flag = False
            b_cnt = 0
            s_cnt = 0

            if(int(i) == 328):
                print()
            for idx, val in enumerate(str(j[0])):
                if (dir_ad_tab[int(val)] == -1):
                    continue
                else:
                    if (dir_ad_tab[int(val)] == idx):
                        s_cnt += 1
                    else:
                        b_cnt += 1
            if (s_cnt == j[1] and b_cnt == j[2]):
                flag = True
                continue
            else:
                break
        if flag:
            cnt += 1

    return cnt

print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))