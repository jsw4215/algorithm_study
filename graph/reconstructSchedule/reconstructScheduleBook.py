import collections


def solution(schedules):

    arranged = collections.defaultdict(list)

    for a,b in sorted(schedules):
        arranged[a].append(b)

    curr_node = []
    next_node = []
    result = []

    def connection(dep):
        while arranged[dep]:
            connection(arranged[dep].pop(0))
        result.append(dep)

    connection('JFK')


    return result[::-1]


if __name__ == '__main__':

    schedules = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    #[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    #[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

    result = solution(schedules)

    print('result : ' + str(result))