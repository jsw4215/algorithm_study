from collections import deque


def bfs_queue(courses, pairs) :
    # 인풋 처리 구간=========================
    courses = courses

    # 후에 순회를 위한 코스리스트
    course_list = []

    #그래프를 위한 딕셔너리
    graph = {}

    for num in range(courses):
        course_list.append(num)

        # courses 값을 활용해 graph의 키 값을 나열한다.
        graph[num] = []

        # 과목간의 관계를 순회하면서,
        for pair in pairs:
            # 해당하는 심화과목이 나왔는데 아직 선수과목이 반영되지 않았다면,
            if pair[0] == num and pair[1] not in graph[num]:
                # 그래프를 최신화한다.
                graph[num].append(pair[1])

    print(course_list)
    print(graph)

    # =========================================
    # can_graduate 기본값 선언
    can_graduate = True

    # 모든 코스를 시작점으로 순회를 실행하기 위한 반복문
    for i in course_list:
        visited = []
        q = deque([i])

        # 만약 q가 참이라면 == 만약 q가 []의 형태가 되지 않는다면
        # (파이썬에서는 빈 자료형도 Falsy값)
        while q :

            # 스택에서 값 꺼내서 노드로 저장
            node = q.popleft()

            # 노드의 선수과목리스트인 graph[node]를 반복
            # adj는 노드에 담긴 과목의 선수과목
            for adj in graph[node]:

                #만약 해당 선수과목이 이번 순회에서 이미 방문한 정점이라면,
                if adj in visited:
                    # 졸업 불가를 반환
                    can_graduate = False
                    return can_graduate

                # 아직 방문하지 않은 정점이라면, 스택
                else:
                    q.append(adj)
                    visited.append(adj)

    # 졸업 불가한 과정이 없으면 졸업 가능 반환
    return can_graduate

print(bfs_queue(3, [[1,0],[2,1], [0,2]]))