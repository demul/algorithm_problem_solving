# 고칠점 :
# self.total_list를 처음부터 set으로 만들기(끝나고나서 set하기엔 요소가 너무 많아짐(메모리 낭비))

######################고치기 전 코드#####################
# import copy
# class PRIME_CAL:
#     def __init__(self) :
#         self.total_list = []
#
#     def rec_func(self, list_left, list_, len_=7):
#         self.total_list += list_
#         if (len_ == 0):
#             return
#
#
#         for i in range(len_):
#             tmp = copy.deepcopy(list_left)
#             new_list = []
#
#             if not list_:
#                 new_list.append(list_left[i])
#                 del (tmp[i])
#                 self.rec_func(tmp, new_list, len_ - 1)
#                 continue
#
#
#             for j in range(len(list_)):
#                 new_list.append(list_left[i] + list_[j])
#             del(tmp[i])
#             self.rec_func(tmp, new_list, len_ - 1)
#
#
#     def is_prime(self):
#         cnt = 0
#         self.total_list = list(set(map(int, self.total_list)))
#         for number_ in self.total_list :
#             if number_< 2:
#                 continue
#             max_eratos = number_ ** 0.5
#             for j in range(2, int(max_eratos) + 1):
#                 if (number_ % j == 0):
#                     cnt -= 1
#                     break
#             cnt += 1
#
#         return cnt
#
#
# def solution(numbers):
#     numbers = [i for i in numbers]
#     P = PRIME_CAL()
#     P.rec_func(numbers, [], len(numbers))
#
#     answer = P.is_prime()
#
#     return answer

######################고친 후 코드#####################
import copy
class PRIME_CAL:
    def __init__(self) :
        self.total_list = set()

    def rec_func(self, list_left, list_, len_=7):
        for listnum in list_ :
            self.total_list.add(listnum)
        if (len_ == 0):
            return


        for i in range(len_):
            tmp = copy.deepcopy(list_left)
            new_list = []

            if not list_:
                new_list.append(list_left[i])
                del (tmp[i])
                self.rec_func(tmp, new_list, len_ - 1)
                continue


            for j in range(len(list_)):
                new_list.append(list_left[i] + list_[j])
            del(tmp[i])
            self.rec_func(tmp, new_list, len_ - 1)


    def is_prime(self):
        cnt = 0
        self.total_list = list(set(map(int, self.total_list)))
        for number_ in self.total_list :
            if number_< 2:
                continue
            max_eratos = number_ ** 0.5
            for j in range(2, int(max_eratos) + 1):
                if (number_ % j == 0):
                    cnt -= 1
                    break
            cnt += 1

        return cnt


def solution(numbers):
    numbers = [i for i in numbers]
    P = PRIME_CAL()
    P.rec_func(numbers, [], len(numbers))

    answer = P.is_prime()

    return answer