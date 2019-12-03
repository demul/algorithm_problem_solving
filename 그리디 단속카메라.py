def solution(routes):
    answer = 1  # 1개는 무조건 필요
    routes = sorted(routes, key=lambda x: x[0])
    min_idx = routes[0][1]
    for i in routes:
        cursor = i[0]
        if (min_idx < cursor):  # 걸쳐 있어도 만난 것으로 간주하므로 <
            min_idx = i[1]
            answer += 1
        min_idx = min(min_idx, i[1])

    # 탐욕증명
    # 1. 어떤 차량의 진입지점도 다른 차향의 진출지점보다 크지 않은 구간 하나 당, 카메라가 1개 필요하다.
    # 2. 진입지점을 기준으로 정렬했을 때, 어떤 차량의 진입지점이 다른 차량의 진출지점보다 큰 경우 새로운 구간이 하나 시작된다. 이러한 성질이 유지되므로 각 구간마다 설치한 카메라의 총 수가 최소의 카메라 갯수다.

    return answer