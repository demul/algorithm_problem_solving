import collections
import sys
import copy

class bfs_rev:
    def __init__(self, arr_):
        self.h = len(arr)
        self.w = len(arr[0])
        self.arr = arr_

        self.DQ = collections.deque()
        self.subDQ = collections.deque()
        self.sz = 0

    def pop_and_put(self, idx):
        y = idx[0]
        x = idx[1]


        #up
        if(0 <= y + 1 < self.h):
            if(self.arr[y + 1][ x] == 1):
                self.DQ.append((y + 1, x))
                self.arr[y+1][x] = 0
        #down
        if (0 <= y - 1 < self.h):
            if (self.arr[y - 1][ x] == 1):
                self.DQ.append((y - 1, x))
                self.arr[y-1][x] = 0
        #right
        if (0 <= x + 1 < self.w):
            if (self.arr[y][ x + 1] == 1):
                self.DQ.append((y, x + 1))
                self.arr[y][x+1] = 0
        #left
        if (0 <= x - 1 < self.w):
            if (self.arr[y][ x - 1] == 1):
                self.DQ.append((y, x - 1))
                self.arr[y][x-1] = 0



    def start_bfs(self):
        self.DQ.append((0, 0))
        self.arr[0][0] = 0
        while True:
            self.sz += 1
            self.subDQ = copy.deepcopy(self.DQ)
            self.DQ = collections.deque()
            while not(not(self.subDQ)):
                cursor = self.subDQ.popleft()
                if cursor == (self.h-1, self.w-1):
                    return self.sz
                self.pop_and_put(cursor)




h, w= list(map(eval, sys.stdin.readline().strip().split()))
arr = [[0] * w for i in range(h)]
for i in range(h):
    str_ = sys.stdin.readline().strip()
    for j, c in enumerate(str_):
        arr[i][j] = eval(c)

B = bfs_rev(arr)
print(B.start_bfs())
