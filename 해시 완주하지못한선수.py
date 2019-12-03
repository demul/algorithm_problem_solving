def solution(participant, completion):
    participant.sort()
    print(participant)
    completion.sort()
    print(completion)
    result = []

    for i in range(0, len(completion)):
        if completion[-1] == participant[-1]:
            participant.pop()
            print(participant)
            completion.pop()
            print(completion)
        else:
            result.append(participant[-1])
            print(result)
            return result

    answer = participant[0]
    return answer

list_p = ["mislav", "stanko", "mislav", "ana"]
list_c = ["stanko", "ana", "mislav"]

solution(list_p, list_c)
print("aas")