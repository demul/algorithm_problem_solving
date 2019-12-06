import collections
import sys


class bfs_pic:
    def __init__(self, arr_):
        self.h = len(arr)
        self.w = len(arr[0])
        self.check_arr = [[1] * self.w for i in range(self.h)]
        self.arr = arr_

        self.DQ = collections.deque()
        self.cnt = 0
        self.tmp_sz = 0
        self.max_sz = 0

    def pop_and_put(self, idx):
        y = idx[0]
        x = idx[1]

        #up
        if(0 <= y + 1 < self.h):
            if(self.check_arr[y + 1][ x] == 1 and self.arr[y + 1][ x] == 1):
                self.DQ.append((y + 1, x))
                self.check_arr[y + 1][ x] = 0
        #down
        if (0 <= y - 1 < self.h):
            if (self.check_arr[y - 1][ x] == 1 and self.arr[y - 1][ x] == 1):
                self.DQ.append((y - 1, x))
                self.check_arr[y - 1][ x] = 0
        #right
        if (0 <= x + 1 < self.w):
            if (self.check_arr[y][ x + 1] == 1 and self.arr[y][ x + 1] == 1):
                self.DQ.append((y, x + 1))
                self.check_arr[y][ x + 1] = 0
        #left
        if (0 <= x - 1 < self.w):
            if (self.check_arr[y][ x - 1] == 1 and self.arr[y][ x - 1] == 1):
                self.DQ.append((y, x - 1))
                self.check_arr[y][ x - 1] = 0



    def start_bfs(self, idx):
        self.DQ.append(idx)
        self.check_arr[idx[0]][ idx[1]] = 0
        while not(not(self.DQ)):
            self.pop_and_put(self.DQ.popleft())
            self.tmp_sz += 1
        self.max_sz = max(self.tmp_sz, self.max_sz)
        self.tmp_sz = 0


    def find_seed(self):
        for i in range(self.h):
            for j in range(self.w):
                if self.arr[i][ j] == 1 and self.check_arr[i][ j] == 1:
                    self.start_bfs((i, j))
                    self.cnt += 1

        return self.cnt, self.max_sz


h, w= list(map(eval, sys.stdin.readline().strip().split()))
arr = [[0] * w for i in range(h)]
for i in range(h):
    arr[i] = list(map(eval, sys.stdin.readline().strip().split()))

B = bfs_pic(arr)
cnt, sz = B.find_seed()

print("%d\n%d" % (cnt, sz))