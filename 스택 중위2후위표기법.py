import collections
import sys


def pop_til_bracket(stack_, answer) :
    while not(not(stack_)):
        i = stack_.popleft()
        if i == '(':
            return stack_, answer
        else:
            answer += i
    return stack_, answer


def solution(string_) :
    stack_ = collections.deque()
    answer = ''

    for i in string_ :
        if 'A' <= i <= 'Z':
            answer += i
        elif i == '(':
            stack_.appendleft(i)
        elif i == ')':
            stack_, answer = pop_til_bracket(stack_, answer)

        elif i == '+' or i == '-':
            while not(not(stack_)):
                top_ = stack_[0]
                if top_ == '+' or top_ == '-':
                    answer += stack_.popleft()
                    break
                elif top_ == '(':
                    break
                else:
                    answer += stack_.popleft()
            stack_.appendleft(i)

        elif i == '*' or i == '/':
            while not(not(stack_)):
                top_ = stack_[0]
                if top_ == '+' or top_ == '-' or top_ == '(':
                    break
                else:
                    answer += stack_.popleft()
            stack_.appendleft(i)
        else:
            break

    if not(not(stack_)):
        _, answer = pop_til_bracket(stack_, answer)
    return answer


s = sys.stdin.readline()
print(solution(s))

#A+B-C*D/E
#AB+CD*E/-
#(A+(B-C))*(D/E)
#ABC-+DE/*
#A*(B+C)
#ABC+*
#A/(B/C)/D
#ABC//D/