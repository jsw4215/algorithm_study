def is_ok(visited):

    if len(visited) == pwLength:
        return True

    return False

def solution():
    result = []
    visited = []

    def dfs_stack(level, index, path):

        for i in range(index, len(charList)):
            visited.append(charList[i])
            if is_ok(visited):
                result.append(visited[:])
            else:
                dfs_stack(level+1, i+1, visited)
            visited.pop()

        pass

    dfs_stack(0,0,[])

    print(str(result))

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
