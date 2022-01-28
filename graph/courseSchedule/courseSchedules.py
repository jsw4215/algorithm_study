import collections


def solution(courses):

    graph = collections.defaultdict(list)

    global checker
    checker = True

    for x,y in courses:
        graph[x].append(y)

    courseList = graph.keys()

    stack = []

    def func(route):

        for dep in route:

            if dep not in stack:
                if len(stack)==num:
                    return True

                stack.append(dep)
            else:
                return False

            if graph[dep]!=[]:
                arr = graph[dep]
                func(arr)
            else :
                del graph[dep]
                return True

    checker = func(courseList)

    if checker is None:
        checker = True

    return checker


if __name__ == '__main__':

    courses = [[2,1],[1,0]]
    num = 3

    result = solution(courses)

    print(f'result : {result}')