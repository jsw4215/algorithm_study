def longest_palindrome(target):
    #palindrome 문자열을 저장할 리스트
    palinList = []
    #start 1씩 증가
    for start in range(len(target)):
        #end 포인터 -> 문자열 맨 끝으로 위치
        end = len(target)
        #start ~ end 까지 문자열 길이가 1보다 작으면 더이상 palindrome이 될 수 없으므로 끝냄
        if end-start<=1:
            break

        #start지점은 고정되어있고, end 지점을 1칸씩 앞으로 이동시키며 문자열 case 비교
        while (True):
            isPalin = True
            print('[시작!]')
            print('start : ' + str(start) + ', end : ' + str(end))
            n=target[start:end]
            print('slice : ' + n)

            #문자열 짝수, 홀수 구분 로직
            odd_even_check = end-start
            print('length : ' + str(odd_even_check))
            if(odd_even_check%2==0):
                #짝수
                print('짝수')
                odd_even_check = False
            else:
                #홀수
                print('홀수')
                odd_even_check = True

            i=0
            j=len(n)-1

            # Target 문자열 내, 맨앞(i)과 맨끝(j)에서부터 한칸식 줄면서 palindrome 비교
            while(True):

                print('i : ' + str(i) + ", j : " + str(j))

                if n[i]!=n[j]:
                    isPalin=False
                    break

                i+=1
                j-=1

                if odd_even_check:
                    print('홀수 진입, odd_even_check : ' + str(odd_even_check))
                    # 홀수라면,
                    if i == j:
                        print('if 진입 : i : ' + str(i) + ', j : ' + str(j))
                        break
                else:
                    if i == j+1:
                        break

            #Palindrome인 경우, 리스트에 해당 문자열을 추가
            if(isPalin):
                print('isPalin : ' + str(isPalin))
                palinList.append(n)

            #end 1씩 감소
            end-=1
            if end-start<=1:
                break


    return palinList


if __name__ == '__main__':

    n = "oihuyftrdrhrotatorjkuytrerfgh"

    palinList = longest_palindrome(n)

    maximum_length=max(palinList, key=len)

    print('List : ' + str(maximum_length))