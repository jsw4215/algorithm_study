# 2, 4, 6, 7, 9, 10, 11, 12, 16, 18, 19, 20, 21, 22, 23, 24, 25
# 17문제
#2. ------------------------------------------------------------------------
l = [200, 100, 300]

l.insert(2,1000)

print(l) # [200, 100, 1000, 300]


# Question :
# FeedBack :

#4.-----------------------------------------------------------------------------


# 1)
a = 1
print(type(a)) # answer int

# 2)
b = 2.22
print(type(b)) # answer float

# 3)
c = 'p'
print(type(c)) # answer str

# 4)
d = [1, 2, 3]
print(type(d)) # answer list


# Question :
# FeedBack :

#6.-----------------------------------------------------------------------------------


falseList = [None, 1, "", 0, bool(0)]

Falsy = [] # bool(a) = False를 출력하는 모든 a값의 모음을 Falsy라고 합니다. :)

answer = falseList[1] # n = ?

print(answer not in Falsy) # == False


# Question :
# FeedBack :

#7.---------------------------------------------------------------------------------------

# 변수명이 사용 불가능한 이유를 말씀해주세요.
# 1)age
# 2)a
# 3)as
# 4)_age
# 5)1age


# Question : 변수명 조건을 서술하세요
# FeedBack : 숫자로 시작할수 없고, 예약어(ex) as)는 안된다.

#9. ---------------------------------------------------------------------------------------
year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'

print(year, month, day, sep="/", end=" ")
print(hour, minute, second, sep=":")


# Question :
# FeedBack :

#10.------------------------------------------------------------------------------------------
# 크리스마스 트리를 출력해주세요

for i in range(5):
    print(" "*(4-i) + "*"*(2*i+1))

for i in range(5):
    str=""
    for _ in range(i,4):
        str+=" "

    for _ in range(2*i+1):
        str+="*"
    print(str)

#    *
#   ***
#  *****
# *******
#*********

# Question : 다중 반복문으로 풀어봅시다!
# FeedBack :

#11.-----------------------------------------------------------------------------------------------
s = 0

for i in range(101):
    s+=i

print(s)

# Question :
# FeedBack :

#12. ---------------------------------------------------------------------------------------------

class Wizard:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def attack(self):
        print('파이어볼')


x = Wizard(health = 545, mana = 210, armor = 10)
print(x.health, x.mana, x.armor)
x.attack()

# Question :
# FeedBack :


# 16.----------------------------------------------------------------
str = input() # 거꾸로, 김재만

answer = str[::-1]

print(answer) # 로꾸거, 만재김

# Question :
# FeedBack :

# 18.----------------------------------------------------
 # 20 30 40 / 30 40 60

scores = list(map(int, input().split()))
avg = sum(scores)/len(scores)

print(avg) # 30 / 43

# Question :
# FeedBack :

# 19.----------------------------------------------
 # 3 2/ 2 3/ 10 2

squares = list(map(int, input().split()))

squared = squares[0]**squares[1]

print(squared)# 9 / 8 / 100

# Question :
# FeedBack :

# 20. ---------------------------------------------------------
nums = list(map(int, input().split())) # 10 2 / 8 3 / 13 4

share = nums[0]//nums[1]
remainder = nums[0]%nums[1]

print(share, remainder) # 5 0 / 2 2 / 3 1

# Question :
# FeedBack :

# 21.--------------------------------------------------------
#다음 중 set을 만드는 방법이 아닌 것은? 2번
# 1) x = {1,2,3,4,5,6,7} # choose O or X
# 2) x = {} # choose O or X
# 3) x = set('python') # choose O or X
# 4) x = set(range(5)) # choose O or X
# 5) x = set()  # choose O or X

# Question :
# FeedBack :

# 22.----------------------------------------------------------
#다음 중 변수 i가 6의 배수인지 확인하는 방법으로 올바른 것은?
# 1) i/6 == 0      # 무슨 연산인가요? 나눗셈
# 2) i%6 == 0      # 무슨 연산인가요? O 모드연산
# 3) i&6 == 0      # 무슨 연산인가요? 비트연산
# 4) i|6 == 0      # 무슨 연산인가요? 비트연산
# 5) i//6 ==0      # 무슨 연산인가요? 나눗셈 소수점 버림

# Question :
# FeedBack :

# 23.-------------------------------------------------------
print(10/2) # answer : 5.0

# Question :
# FeedBack :

# 24.----------------------------------------------------------
name = input() # mary, jaeman

answer = name.upper()

print(answer) # MARY, JAEMAN

# Question :
# FeedBack :

# 25.--------------------------------------------------------------
# 반지름 x 반지름 x 3.14인 원의 넓이를 구하는 함수를 작성하여 넓이를 출력하세요.
num = int(input()) # 7

def circledd(num):
    return (num**2)*3.14

answer = circledd(num)
print(answer) # 153.86

# Question :
# FeedBack :

#-----------------------------------------------------------
