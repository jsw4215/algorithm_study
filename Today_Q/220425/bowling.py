def solution(n, m, data):

    # 1부터 10까지의 무게를 담을 수 있는 리스트
    weights = [0] * 11

    for x in data:
        # 각 무게에 해당하는 볼링공의 개수 카운트
        weights[x] += 1

    count = 0
    # 1부터 m까지의 각 무게에 대하여 처리
    for i in range(1, m + 1):
        n -= weights[i]  # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
        count += weights[i] * n  # B가 선택하는 경우의 수와 곱하기

    print(count)
    return count

if __name__ == '__main__':

    # 볼링공 개수, 공의 최대 무게
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    res = solution(n, m, data)

    print("res", res)