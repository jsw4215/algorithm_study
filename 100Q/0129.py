# 2, 4, 6, 7, 9, 10, 11, 12, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28
# 20문제
#2. ------------------------------------------------------------------------
l = [200, 100, 300]

l.insert(2, 1000)

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


# Question : [] {} () None "" 0 False
# FeedBack :

#7.---------------------------------------------------------------------------------------

# 변수명이 사용 불가능한 이유를 말씀해주세요.
# 1)age
# 2)a
# 3)as
# 4)_age
# 5)1age


# Question : 변수명 조건을 서술하세요
# FeedBack :  숫자로 시작할 수 없고,예약어는 사용할 수 없다.

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
    temp=""
    for _ in range(4-i):
        temp+=" "

    for _ in range(2*i+1):
        temp+="*"

    print(temp)

#    *
#   ***
#  *****
# *******
#*********

# Question : 다중 반복문으로 풀어봅시다!
# FeedBack :

#11.-----------------------------------------------------------------------------------------------
s = 0

for i in range(100):
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
        self.mana-=100
        if self.mana<0:
            print('마나가 부족합니다.')
        else:
            print('파이어볼')

x = Wizard(health = 545, mana = 210, armor = 10)
print(x.health, x.mana, x.armor)
x.attack()

# Question :
# FeedBack :


# 16.----------------------------------------------------------------
strs = input() # 거꾸로, 김재만

strs = strs[::-1]

print(strs) # 로꾸거, 만재김

# Question :
# FeedBack :

# 18.----------------------------------------------------
# 20 30 40 / 30 40 60
nums = list(map(int, input().split()))

avg = sum(nums)/len(nums)

print(avg) # 30 / 43

# Question :
# FeedBack :

# 19.----------------------------------------------
# 3 2/ 2 3/ 10 2
nums = list(map(int, input().split()))

squared = nums[0]**nums[1]

print(squared)# 9 / 8 / 100

# Question :
# FeedBack :

# 20. ---------------------------------------------------------
# 10 2 / 8 3 / 13 4
nums = list(map(int, input().split()))

share = nums[0]//nums[1]
remainder = nums[0]%nums[1]

print(share, remainder) # 5 0 / 2 2 / 3 1

# Question :
# FeedBack :

# 21.--------------------------------------------------------
#다음 중 set을 만드는 방법이 아닌 것은?
# 1) x = {1,2,3,4,5,6,7} # choose O
# 2) x = {} # choose  X
# 3) x = set('python') # choose O
# 4) x = set(range(5)) # choose O
# 5) x = set()  # choose O

# Question :
# FeedBack :

# 22.----------------------------------------------------------
#다음 중 변수 i가 6의 배수인지 확인하는 방법으로 올바른 것은?
# 1) i/6 == 0      # 무슨 연산인가요? 나눗셈
# 2) i%6 == 0      # 무슨 연산인가요? 나머지 나눗셈
# 3) i&6 == 0      # 무슨 연산인가요? 비트 and 연산
# 4) i|6 == 0      # 무슨 연산인가요? 비트 or 연산
# 5) i//6 == 0     # 무슨 연산인가요? 몫 나눗셈

# Question :
# FeedBack :

# 23.-------------------------------------------------------
print(10/2) # answer : 5.0

# Question :
# FeedBack :

# 24.----------------------------------------------------------
name = input() # mary, jaeman

name = name.upper()

print(name) # MARY, JAEMAN

# Question :
# FeedBack :

# 25.--------------------------------------------------------------
# 반지름 x 반지름 x 3.14인 원의 넓이를 구하는 함수를 작성하여 넓이를 출력하세요.
num = int(input()) # 7

def circleSqu(num):
    return (num**2)*3.14
answer = circleSqu(num)

print(answer) # 153.86

# Question :
# FeedBack :

# 26.-----------------------------------------------------------
planet = input() # 수성, 금성, 지구, 화성, 목성, 토성, 천왕성, 해왕성, 천왕성

dics = {'수성':'Mercury',
        '금성':'Venus',
        '지구':'Earth',
        '화성':'Mars',
        '목성':'Jupiter',
        '토성':'Saturn',
        '천왕성':'Uranus',
        '해왕성':'Neptune'}

answer = dics[planet]

print(answer) # Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune

# 27. ------------------------------------------------------------------
names = list(input().split()) # Yujin Hyewon
scores = list(map(int, input().split())) # 70 100
math_score = {}
for i in range(len(names)):
    math_score[names[i]] = scores[i]

print(str(math_score)) # {'Yujin': 70, 'Hyewon':100}

# 28.------------------------------------------------------------------------
strs = input() # Python

for i in range(len(strs)-1):
    print(strs[i]+strs[i+1])

#Py
#yt
#th
#ho
#on