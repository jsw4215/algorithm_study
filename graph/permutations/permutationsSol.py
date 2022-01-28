def solution(nums):
    results = []
    prev_elements = []

    def dfs(elements):
        print('=======================================================')
        if len(elements) == 0:
            results.append(prev_elements[:])
            print(f'results : {results} dfs 종료')

        for e in elements:
            next_elements = elements[:]
            print(f'next_elements : {next_elements}, e : {e}')
            next_elements.remove(e)
            print(f'next_elements.remove(e) : {next_elements}')

            prev_elements.append(e)
            print(f'elements : {elements}, prev_elements : {prev_elements}, next_elements : {next_elements}, dfs 호출')
            dfs(next_elements)
            print(f'before prev_elements.pop() : {prev_elements}')
            prev_elements.pop()
            print(f'after prev_elements.pop() : {prev_elements}')

        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++ end for : result : ' + str(results))

    dfs(nums)
    return results


if __name__ == '__main__':

    inputNum = [1,2,3]

    result = solution(inputNum)

    print('result : ' + str(result))