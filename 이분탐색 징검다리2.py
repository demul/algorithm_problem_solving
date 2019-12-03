import copy


class Rock:
    def __init__(self, distance, rocks):
        self.dist_list = []

        rocks.append(distance)

        fidx = 0
        ridx = 0
        for i in range(0, len(rocks)):
            fidx = ridx
            ridx = rocks[i]

            self.dist_list.append(ridx - fidx)

        self.dist_list.insert(0, 100000000000)
        self.dist_list.append(100000000000)

    def find_min_idx(self):
        min_dist = 10000000000
        min_dist_s = 10000000000
        LR = 0
        min_idx = -1

        for i in range(1, len(self.dist_list) - 1):
            fval = self.dist_list[i - 1]
            cval = self.dist_list[i]
            rval = self.dist_list[i + 1]
            if (cval < min_dist):
                min_dist = cval
                min_idx = i
                if (fval < rval):
                    LR = -1
                    min_dist_s = fval
                else:
                    LR = 1
                    min_dist_s = rval
            elif (cval == min_dist):
                if (fval < rval):
                    LR_this = -1
                    min_dist_s_this = fval
                else:
                    LR_this = 1
                    min_dist_s_this = rval
                if (min_dist_s_this < min_dist_s):
                    min_idx = i
                    min_dist_s = min_dist_s_this
                    LR = LR_this

                # if(fval < rval) :
                #     min_dist_s_this = fval
                #     if min_dist_s_this < min_dist_s :
                #         min_dist = cval
                #         min_idx = i
                #         min_dist_s = min_dist_s_this
                #         LR = -1
                # else :
                #     min_dist_s_this = rval
                #     if min_dist_s_this < min_dist_s :
                #         min_dist = cval
                #         min_idx = i
                #         min_dist_s = min_dist_s_this
                #         LR = 1

        del (self.dist_list[min_idx])
        if (LR == -1):
            self.dist_list[min_idx - 1] += min_dist
        else:
            self.dist_list[min_idx] += min_dist


def solution(distance, rocks, n):
    # 일단 정렬
    rocks = sorted(rocks)
    rockNroll = Rock(distance, rocks)

    for i in range(n):
        rockNroll.find_min_idx()
        print()

    answer = min(rockNroll.dist_list)
    print(answer)

    return answer

solution(20,[3, 6, 9, 12, 15],3)
# solution(45, [4,7,14,23,32,36,39], 1)
# solution(45, [4,7,14,23,32,36,39], 2)
# solution(45, [4,7,14,23,32,36,39], 3)
# solution(45, [4,7,14,23,32,36,39], 4)
# solution(45, [4,7,14,23,32,36,39], 5)
# solution(45, [4,7,14,23,32,36,39], 6)
# solution(45, [4,7,14,23,32,36,39], 7)
