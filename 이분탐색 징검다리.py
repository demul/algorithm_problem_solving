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

    def find_min_idx(self):
        min_fidx = -1
        min_cidx = -1
        min_ridx = -1

        min_fdist = 1000000000
        min_cdist = 1000000000
        min_rdist = 1000000000

        for i in range(0, len(self.dist_list) - 2):
            fdist = self.dist_list[i]
            cdist = self.dist_list[i + 1]
            rdist = self.dist_list[i + 2]

            if (cdist < min_cdist):
                min_fdist = fdist
                min_fidx = i
                min_cdist = cdist
                min_cidx = i + 1
                min_rdist = rdist
                min_ridx = i + 2
            elif(cdist == min_cdist):
                fflag = 0
                rflag = 0


                if(fdist < min_fdist):
                    fflag = 1
                else:
                    fflag = -1

                if (rdist < min_rdist):
                    rflag = 1
                else:
                    rflag = -1

                if(fflag == 1 and rflag == 1) :
                    min_fdist = fdist
                    min_fidx = i
                    min_cdist = cdist
                    min_cidx = i + 1
                    min_rdist = rdist
                    min_ridx = i + 2
                elif(fflag == 1 and rflag == -1):
                    if(fdist < min_rdist):
                        min_fdist = fdist
                        min_fidx = i
                        min_cdist = cdist
                        min_cidx = i + 1
                        min_rdist = rdist
                        min_ridx = i + 2
                    else:
                        continue
                elif (fflag == -1 and rflag == 1):
                    if (rdist < min_fdist):
                        min_fdist = fdist
                        min_fidx = i
                        min_cdist = cdist
                        min_cidx = i + 1
                        min_rdist = rdist
                        min_ridx = i + 2
                    else:
                        continue
                else:
                    continue

        first = self.dist_list[0]
        last = self.dist_list[-1]
        min__ = min(first, min_cdist, last)

        if(min__ == first):
            del (self.dist_list[0])
            self.dist_list[0] += first
            # return first
        elif (min__ == last):
            del (self.dist_list[-1])
            self.dist_list[-1] += last
            # return last
        else:
            if(min_fdist < min_rdist):
                del (self.dist_list[min_cidx])
                self.dist_list[min_cidx-1] += min_cdist
                # return min_cdist
            else:
                del (self.dist_list[min_cidx])
                self.dist_list[min_cidx] += min_cdist
                # return min_cdist


def solution(distance, rocks, n):
    # 일단 정렬
    rocks = sorted(rocks)
    rockNroll = Rock(distance, rocks)

    for i in range(n):
        i = rockNroll.find_min_idx()
        # print(i)

    answer = min(rockNroll.dist_list)
    # print(answer)

    return answer

# solution(25, [2, 14, 11, 21, 17], 2)