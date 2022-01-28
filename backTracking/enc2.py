def solution():
    result = []
    visited = []

    def dfs_stack(level, start, path):

       for node in range(start, numOfChar):

            visited.append(charList[node])

            if len(visited) == pwLength:
                result.append(visited[:])
                visited.pop()
                continue

            else:
                dfs_stack(level+1, node+1, visited)

            visited.pop()

       return

    dfs_stack(0,0,[])

    def pwCheck(lists):

        for i in lists:
            jaUm = 0
            moUm = 0
            for char in i:
                if char in 'aeiou':
                    moUm+=1
                else:
                    jaUm+=1
            if jaUm>=2 and moUm>=1:
                print(''.join(i))

    pwCheck(result)

    return


if __name__ == '__main__':


    pwLength = 4
    numOfChar = 6
    charList = ['a','t','c','i','s','w']
    charList.sort()
    solution()

    # for i in result:
    #     temp = ''.join(i)
    #     print(temp)
