def solution(words, queries):

    result = []

    def bin_search(words, quer):
        quer_len = len(quer)
        left = 0
        start = left
        right = len(quer) - 1
        end = right
        #left/right구분
        checker = None
        cnt = 0
        temp = -1

        while left <= right:
            mid = (left + right) // 2

            #left가 ?일 경우
            if quer[start] == "?":
                checker = True
                if quer[mid]=="?":
                    left = mid + 1
                else:
                    right = mid - 1
                    temp = mid

            #right가 ?일 경우
            elif quer[end] == "?":
                checker = False
                if quer[mid] == "?":
                    right = mid - 1
                else:
                    left = mid + 1
                    temp = mid

        for word in words:
            if len(word) == quer_len:
                if checker:
                    if word[temp:] == quer[temp:]:
                        cnt+=1
                elif not checker:
                    if word[:temp+1] == quer[:temp+1]:
                        cnt+=1

        return cnt

    for quer in queries:
        result.append(bin_search(words, quer))

    return result


if __name__ == '__main__':

    words = ["frodo","front","frost","frozen","frame","kakao"]
    queries = ["fro??","????o","fr???","fro???","pro?"]


    result = solution(words, queries)

    print('result : ' + str(result))