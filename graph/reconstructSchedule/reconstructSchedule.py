import collections


def solution(schedules):

    arranged = collections.defaultdict(list)


    for a,b in sorted(schedules):
        arranged[a].append(b)

    print(f'arranged : {arranged}')

    curr_node = []
    next_node = []
    result = []

    def connection(dep):
        result.append(dep)
        if len(arranged[dep])!=0:
            arr = arranged[dep]
            temp = arr.pop(0)
            connection(temp)
        else:
                return


    connection('JFK')


    return result


if __name__ == '__main__':

    schedules = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    #[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    #[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    result = solution(schedules)

    print('result : ' + str(result))

# if len(arr)>0 and arranged[temp]==[]:
#     arr.append(temp)
#
#     temp = arr.pop(0)
#     arr.sort()
#
#     connection(temp)
# else: