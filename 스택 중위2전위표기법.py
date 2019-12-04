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
############################################
#####위 코드는 중위 -> 후위표기법 코드다.######
############################################

#수식을 뒤집은 뒤, 후위표기법으로 구하고, 다시 뒤집으면 전위표기법이 된다.

s = sys.stdin.readline()
print(solution(s[:,:,-1])[:,:,-1])
