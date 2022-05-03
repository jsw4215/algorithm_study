def solution(s):

    strs = list(s)


    for i in range(len(strs)-1):
        for idx in range(len(strs)-1):

            if strs[idx]=='c':
                if strs[idx+1]=='b':
                    strs[idx], strs[idx+1] = strs[idx+1], strs[idx]

    
            if strs[idx]=='b':
                if strs[idx+1]=='a':
                    strs[idx], strs[idx+1] = strs[idx+1], strs[idx]


    print("result", strs)

    return "".join(strs)

if __name__ == '__main__':

    s = "ababbaab"

    result = solution(s)

    print(str(result))