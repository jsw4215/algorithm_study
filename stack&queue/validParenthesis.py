def solution(input):
    result = True

    stack =[]
    table = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    for char in input:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False

    return len(stack) == 0


if __name__ == '__main__':

    input = '()[]{}'

    result = solution(input)

    print('result : ' + str(result))