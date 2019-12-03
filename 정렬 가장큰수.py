import queue
import functools


def cmp_method(str1, str2):
    if (str1 + str2 >= str2 + str1):
        return 1
    else:
        return -1

#
# def merge_sort(str, len):
#     if (len == 1):
#         return str
#     front_Q = queue.Queue()
#     rear_Q = queue.Queue()
#     sum = queue.Queue()
#
#     for i in range(len // 2):
#         front_Q.put(str.get())
#
#     for i in range(len - len // 2):
#         rear_Q.put(str.get())
#
#     sorted_1 = merge_sort(front_Q, len//2)
#     sorted_2 = merge_sort(rear_Q, len - len//2)
#
#     e1 = sorted_1.get()
#     e2 = sorted_2.get()
#     # 크거나 같을때 앞에꺼 넣기로 하면, stable하게 정렬가능
#     while (True):
#         flag_cmp = cmp_method(e1, e2)
#         if (flag_cmp == 1):
#             sum.put(e1)
#             if (sorted_1.empty()):
#                 while (True):
#                     sum.put(e2)
#                     if (sorted_2.empty()):
#                         break
#                     else:
#                         e2 = sorted_2.get()
#             else:
#                 e1 = sorted_1.get()
#                 continue
#         else:
#             sum.put(e2)
#             if (sorted_2.empty()):
#                 while (True):
#                     sum.put(e1)
#                     if (sorted_1.empty()):
#                         break
#                     else:
#                         e1 = sorted_1.get()
#             else:
#                 e2 = sorted_2.get()
#                 continue
#         if sorted_1.empty() and sorted_2.empty() :
#             break
#
#
#     return sum


def solution(numbers):
    answer = ""
    numbers_stred = list(map(str, numbers))

    # numQ = queue.Queue()
    #
    # for i in numbers_stred:
    #     numQ.put(i)
    #
    # answer_Q = merge_sort(numQ, len(numbers))
    #
    # for i in range(len(numbers)):
    #     answer+=answer_Q.get()

    numbers_sorted = sorted(numbers_stred, key=functools.cmp_to_key(cmp_method))

    for i in numbers_sorted:
        answer += i

    return str(int(answer))

print(solution([3, 30, 34, 5, 9]))