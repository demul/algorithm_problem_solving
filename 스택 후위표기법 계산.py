import sys
import collections


def cal_post_order(str_, tab_):
    stack_ = collections.deque()

    for c in str_:
        if 'A' <= c <= 'Z':
            stack_.appendleft(eval(tab_[c]))
        elif c == '+':
            opr2 = stack_.popleft()
            opr1 = stack_.popleft()
            stack_.appendleft(opr1 + opr2)
        elif c == '-':
            opr2 = stack_.popleft()
            opr1 = stack_.popleft()
            stack_.appendleft(opr1 - opr2)
        elif c == '*':
            opr2 = stack_.popleft()
            opr1 = stack_.popleft()
            stack_.appendleft(opr1 * opr2)
        elif c == '/':
            opr2 = stack_.popleft()
            opr1 = stack_.popleft()
            stack_.appendleft(opr1 / opr2)
        else:
            print('error')
            exit(-1)

    return stack_.pop()


iter_ = eval(sys.stdin.readline().strip()) #개행문자 제거
string_ = sys.stdin.readline().strip() #개행문자 제거
table_ = dict()

offset_ = ord('A')
for i in range(iter_):
    table_[chr(offset_+i)] = sys.stdin.readline().strip() #개행문자 제거

val = cal_post_order(string_, table_)

print("%.2f" % val)
