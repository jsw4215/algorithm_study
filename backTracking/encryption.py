def solution(pwLength, numOfChar):
    result = []
    visited = []

    def dfs_stack(start):

       for node in range(start, numOfChar):

            visited.append(charList2[node])

            if len(visited) == pwLength:
                result.append(visited[:])
                visited.pop()
                continue

            else:
                dfs_stack(node+1)

            visited.pop()

       return

    dfs_stack(0)

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

    lists = input().split(" ")
    pwLength = int(lists[0])
    numOfChar = int(lists[1])
    charList2 = list(input().split())
    #charList = ['a','t','c','i','s','w']
    charList2.sort()
    solution(pwLength, numOfChar)

    # for i in result:
    #     temp = ''.join(i)
    #     print(temp)
