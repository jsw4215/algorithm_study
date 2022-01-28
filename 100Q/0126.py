#1. --------------------------------------------------------------------
nums = [100, 200, 300, 400, 500]

nums = nums[:3]

print(nums) # [100, 200, 300]


# Question : nums 값을 유지한 채로, [100,200,300] 출력하기, pop의 시간 복잡도는?
# FeedBack : O(1)

# #2. ------------------------------------------------------------------------
l = [200, 100, 300]

l.insert(2, 1000)
l.insert(1000, 300)
print(l) # [200, 100, 1000, 300]


# Question : l = [200, 100, 1000, 2000, 300], insert의 첫 인자 값이 엄청 크면 어떻게 될까??
# FeedBack : 맨뒤에 추가됨

#3. ---------------------------------------------------------------------------
l = [100, 200, 300]

print(type(l)) # answer list

# Question : How to print class str, class int, class list, class tuple, 어떻게 하면 데이터 타입을 set으로 출력할 수 있을까?
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

#숫자형(인트, 플롯) + 스트링 + 불 + 리스트 , 셋, 딕셔너리, 튜플, 바이트

# Question : 파이썬의 자료형?
# FeedBack :

#5.----------------------------------------------------------------------------------

a = 10
b = 2
for i in range(1, 5, 1):
    a += i

print(a + b) # answer 16

# Question : 결과값을 22으로 만들어 주세요.
# FeedBack :

#6.-----------------------------------------------------------------------------------


falseList = [None, 1, "", 0, bool(0)]

Falsy = [] # bool(a) = False를 출력하는 모든 a값의 모음을 Falsy라고 합니다. :)

answer = falseList[1] # n = ?

print(answer not in Falsy) # == False


# Question : Falsy의 구성원을 얘기해주세요
# FeedBack : None "" 0 False [] {} ()

#7.---------------------------------------------------------------------------------------

# 변수명이 사용 불가능한 이유를 말씀해주세요.
# 1)age
# 2)a
# 3)as
# 4)_age
# 5)1age

#* 문자 : 예약어 X
#* 숫자 : 맨 앞에 오면 안됨
#* 특수기호 : _

# Question : 변수명 조건을 서술하세요
# FeedBack :

#8. -----------------------------------------------------------------------------------

d = {
    'height':100,
    'weight':78,
    'weight':84,
    'emparture':36,
    'eyesight':1
}

print(d['weight'])

# Question : weight값이 왜 그렇게 출력 됐나요? d.pop(key값)을 하면 어떻게 될까요?
# FeedBack : 84
# 둘 다 빠짐

#9. ---------------------------------------------------------------------------------------
year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'

print(year, month, day, sep="/", end=" ")
print(hour, minute, second, sep=":")


# Question : sep에 여러가지 기호를 넣어보아요! ㅎㅎ
# FeedBack :

#10.------------------------------------------------------------------------------------------
# 크리스마스 트리를 출력해주세요

for i in range(5):
    print(" "*(4-i)+"*"*(2*i+1))

#    *
#   ***
#  *****
# *******
#*********

# Question : 다른 모양 찍어보기, 트리를 뒤집어봅시다!
# FeedBack :

#11.-----------------------------------------------------------------------------------------------
s = 0

for i in range(101):
    s+=i

print(s)

# Question : 2부터 100까지 짝수만 더하기,
# FeedBack :

#12. ---------------------------------------------------------------------------------------------

class Wizard:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def attack(self):
        print('파이어볼')
        self.mana-=100


x = Wizard(health = 545, mana = 210, armor = 10)
print(x.health, x.mana, x.armor)
x.attack()
x.attack()

# Question : 마나 100마다 파이어볼을 쓸 수 있습니다! 여러번 시전 해주세요
# FeedBack :


#13.----------------------------------------------------------------------------------------------
num = int(input()) # 1, 2, 3, 4, 5, 6, 7, 8

planets = ("수성", "금성", "지구", "화성", "목성", "토성", "천왕성", "해왕성")
dic = {
    1:"수성",
    2:"금성",
    3:"지구",
    4:"화성",
    5:"목성",
    6:"토성",
    7:"천왕성",
    8:"해왕성"
}

print(dic[num]) #수성, 금성, 지구, 화성, 목성, 토성, 천왕성, 해왕성

# Question : 리스트로 만드셨나요?? 그럼 딕셔너리로 한번 해보죠!
# FeedBack :

#14.----------------------------------------------------------------------------------------
num = int(input()) # 3, 2, 10, 9, 0, 15

if num%3==0 and num!=0:
    print('짝')
else :
    print(num)
# 짝, 2, 10, 짝, 0, 짝

# Question : 혹시 0일때도 짝 소리나는 3,6,9게임은 아니죠?!
# FeedBack :

#15.----------------------------------------------------------------------------------------
name = input() # 김다정, 김재만

answer = f'안녕하세요 저는 {name[::-1]}입니다.'

print(answer) # 안녕하세요 저는 김다정입니다. , 안녕하세요 저는 김재만입니다.

# Question : 이름은 거꾸로 말해요로 해볼까요?
# FeedBack :

# 16.----------------------------------------------------------------
str = input() # 거꾸로, 김재만

answer = str[::-1]

print(answer) # 로꾸거, 만재김
print(''.join(reversed(answer)))

# 17.---------------------------------------------------
height = int(input()) # 190, 132

if height>=150:
    print('Yes')
else:
    print('No')

# print > Yes, print > No

# 18.----------------------------------------------------
print('과목 점수 3개 띄워서 입력해주세요 : ')
nums =  list(map(int, input().split()))

avg = sum(nums)/len(nums)

print(avg) # 30 / 43

# 19.----------------------------------------------
print('숫자 승수 입력 : ')
nums = list(map(int, input().split()))

squared = nums[0]**nums[1]

print(squared)# 9 / 8 / 100

# 20. ---------------------------------------------------------
nums = list(map(int, input().split()))
# 10 2 / 8 3 / 13 4

share = nums[0]//nums[1]
remainder = nums[0]%nums[1]
print(share, remainder) # 5 0 / 2 2 / 3 1