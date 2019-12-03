import sys
day_for_mon = [0, 31, 30, 31, 30, 31, 31, 30, 31, 30]
sum_day_for_mon = []
i = 0
for j in day_for_mon:
    i += j
    sum_day_for_mon.append(i)


def date_to_day(mon, day):
    if mon < 3:
        return 0
    return sum_day_for_mon[mon-3] + day


def string_to_day(str_):
    day_list = str_.split(" ")
    start_ = date_to_day(int(day_list[0]), int(day_list[1]))
    end_ = date_to_day(int(day_list[2]), int(day_list[3]))
    return start_, end_


def get_input2list():
    n = int(input())
    output_list = []
    for i in range(n):
        output_list.append(string_to_day(sys.stdin.readline()))

    return output_list

def solution(input_list) :
    input_list.sort(key=lambda x: x[0])
    len_ = len(input_list)
    last_day = 1
    new_last_day =1
    MAX_DAY = date_to_day(11, 30)
    idx = 0
    cnt = 0

    while(idx < len_):
        while(idx < len_) :
            i = input_list[idx]
            if i[0] <= last_day:
                new_last_day = max(i[1], new_last_day)
                idx += 1
            else:
                break
        if new_last_day == last_day:
            return 0
        last_day = new_last_day
        cnt += 1
        if last_day > MAX_DAY :
            return cnt
    return 0

input_list = get_input2list()
print(solution(input_list))