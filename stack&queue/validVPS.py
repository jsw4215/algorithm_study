def solution(input):

    stack =[]
    table = {
        ')':'('
    }

    for char in input:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False

    return len(stack) == 0


if __name__ == '__main__':

    numberOfInput = int(input())
    inputStr=[]
    for i in range(numberOfInput):
        temp = input()
        inputStr.append(temp)

    for i in inputStr:
        result = solution(i)
        if result:
            print("YES")
        else:
            print("NO")