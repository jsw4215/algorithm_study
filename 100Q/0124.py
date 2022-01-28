#1. --------------------------------------------------------------------
nums = [100, 200, 300, 400, 500]

nums = nums[:3]

print(nums) # [100, 200, 300]


# Question :
# FeedBack :
# #2. ------------------------------------------------------------------------
l = [200, 100, 300]

l.insert(2,1000)

print(l) # [200, 100, 1000, 300]


# Question : l = [200, 100, 1000, 2000, 300]
# FeedBack :
#3. ---------------------------------------------------------------------------
l = [100, 200, 300]
print(l+l)
print(type(l)) # answer list

# Question : How to print class str, class int, class list, class tuple
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

# Question : 파이썬의 자료형?
# FeedBack :

#5.----------------------------------------------------------------------------------

a = 10
b = 2
for i in range(0, 11, 10):
    a += i
#11 // 14 // 19
print(a + b) # answer 16

# Question :
# FeedBack :

#6.-----------------------------------------------------------------------------------


falseList = [None, 1, "", 0, bool(0)]

Falsy = [] # bool(a) = False를 출력하는 모든 a값의 모음을 Falsy라고 합니다. :)

answer = falseList[1] # n = ?

print(answer not in Falsy) # == False


# Question : Falsy의 구성원을 얘기해주세요
# FeedBack : None "" 0 bool(0)

#7.---------------------------------------------------------------------------------------

# 변수명이 사용 불가능한 이유를 말씀해주세요.
# 1)age
# 2)a
# 3)as
# 4)_age
# 5)1age

# Question : 변수명 조건을 서술하세요
# FeedBack : 3,5
# 5 - 숫자로 시작할 수 없다
# 3 - 예약어이므로 사용할 수 없다

#8. -----------------------------------------------------------------------------------

d = {
    'height':100,
    'weight':78,
    'weight':84,
    'emparture':36,
    'eyesight':1
}

print(d['weight'])

# Question :
# FeedBack : 84

#9. ---------------------------------------------------------------------------------------
year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'

print(year[2:], month, day, sep="/", end=" " )
print(hour, minute, second, sep=":")

# Question :
# FeedBack :
# 2019 04 26
# 11 34 27


#10.------------------------------------------------------------------------------------------
# 크리스마스 트리를 출력해주세요


#    *
#   ***
#  *****
# *******
#*********

for i in range(5):
    print(" "*(4-i) + "*"*(2*i+1))

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *



# Question : 다른 모양 찍어보기
# FeedBack :

#11.-----------------------------------------------------------------------------------------------
s = 0

for s in range(2,101,2):
    s+=s

print(s)

# Question : 2부터 100까지 짝수만 더하기,
# FeedBack :

#12. ---------------------------------------------------------------------------------------------

class Wizard:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def attack(self, mana):
        while mana:
            print('파이어볼')
            mana-=10

x = Wizard(health = 545, mana = 210, armor = 10)
print(x.health, x.mana, x.armor)
x.attack(x.mana)


# Question : 마나 10마다 파이어볼 갯수를 하나 씩 추가해주세요
# FeedBack :


#13.----------------------------------------------------------------------------------------------
num = int(input()) # 1

planets = ["수성","금성","지구","화성","목성","토성","천왕성","해왕성","명왕성"]

answer = planets[num-1]

print(answer) #수성

# Question :
# FeedBack :

#14.----------------------------------------------------------------------------------------
num = int(input()) # 3, 2, 10, 9, 0, 15

if num%3==0 and num!=0:
    answer = "짝"
else :
    answer = num

print(answer) # 짝, 2, 10, 짝, 0, 짝

# Question :
# FeedBack :

#15.----------------------------------------------------------------------------------------
name = input() # 김다정, 김재만

answer = f'안녕하세요 저는 {name}입니다.'

print(answer) # 안녕하세요 저는 김다정입니다. , 안녕하세요 저는 김재만입니다.

# Question :
# FeedBack :