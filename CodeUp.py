# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Python 기초 100제

# +
# 6059 
# 비트 단위로 NOT 하여 출력하기

a = int(input())

print(~a)

# +
# 6060 
# 비트단위로 AND 하여 출력하기

a,b = input().split()
a = int(a)
b = int(b)
print(a & b)
print(a | b)
print(a ^ b)



# +
# 6061
# 비트단위로 OR 하여 출력하기

a, b = input().split()
print(int(a)|int(b))

# +
# 6062
# 비트단위로 XOR 하여 출력하기

a,b = input().split()
print(int(a)^int(b))

# +
# 6063
# 정수 2개 입력받아 큰 값 출력하기

# 3개의 요소로 이루어지는 3항 연산은
# "x if C else y" 의 형태로 작성이 된다.
# - C : True 또는 False 를 평가할 조건식(conditional expression) 또는 값
# - x : C의 평가 결과가 True 일 때 사용할 값
# - y : C의 평가 결과가 True 가 아닐 때 사용할 값
a,b = input().split()
a = int(a)
b = int(b)

print(a if a>b else b)

# +
# 6064
# 정수 3개 입력받아 가장 작은 값 출력하기

a,b,c = input().split()
a,b,c = int(a),int(b),int(c)
d = a if a<=b else b
e = d if d<=c else c
print(e)

###############################

a, b, c = map(int, input().split()) 
print(min(a,b,c))

# +
# 6065
# 정수 3개 입력받아 짝수만 출력하기
a,b,c = input().split()
a,b,c = int(a),int(b),int(c)
if a%2==0:
    print(a)

if b%2==0:
    print(b)
    
if c%2==0:
    print(c)

# +
# 6066
# 정수 3개 입력받아 짝/홀 출력하기
a,b,c = input().split()
a,b,c = int(a),int(b),int(c)
if a%2==0:
    print('even')
else:
    print('odd')

if b%2==0:
    print('even')
else:
    print('odd')
    
if c%2==0:
    print('even')
else:
    print('odd')

# +
# 6067
# 정수 1개 입력받아 분류하기

a = int(input())
if a%2==0: # 짝
    if a>0:
        print("C") #양수
    elif a<0:
        print("A") # 음수
else: # 홀
    if a>0:
        print("D") #양수
    elif a<0:
        print("B") # 음수

# +
# 6068
# 점수 입력받아 평가 출력하기
a = int(input())

if a>=90:
    print("A")
elif a>=70:
    print("B")
elif a>=40:
    print("C")
elif a>=0:
    print("D")
# -

# 6069
# 평가 입력받아 다르게 출력하기
a = input()
if a == "A":
    print("best!!!")
elif a == "B":
    print("good!!")
elif a == "C":
    print("run!")
elif a == "D":
    print("slowly~")
else:
    print("what?")

# +
# 6070
# 월 입력받아 계절 출력하기

a = int(input())
if a//3 ==1:
    print("spring")
elif a//3==2:
    print("summer")
elif a//3==3:
    print("fall")
else:
    print("winter")
# -

# 6071
# 0 입력될 때까지 무한 출력하기
a = 1
while a!=0:
    a = int(input())
    if a!=0:
        print(a)
    elif a==0:
        break

# 6072
# 정수 1개 입력받아 카운트다운 출력하기1
a = int(input())
while a!=0:
    print(a)
    a-=1

# +
# 6073
# 정수 1개 입력받아 카운트다운 출력하기2

a = int(input())
i = 1
while a!=0:
    b = a-i
    print(b)
    i+=1
    if b == 0:
        break
        
## 모범답안
# a=int(input()) 
# while a!=0: 
#    a=a-1 
#    print(a)



# +
#6074
# 문자 1개 입력받아 알파벳 출력하기

a = ord(input())
t = ord('a')
while t<=a:
    print(chr(t),end=' ')
    t+=1
# -

# 6075
# 정수 1개 입력받아 그 수까지 출력하기
a = int(input())
b = 0
while b<=a:
    print(b)
    b+=1

# +
# 6076
# 정수 1개 입력받아 그 수까지 출력하기2

a = int(input())
for i in range(a+1):
    print(i)

# +
# 6077
# 짝수 합 
a = int(input())
b = 0
for i in range(1, a+1):
    if i % 2 ==0 :
        b+=i
    
print(b)

# +
# 6078
# 원하는 문자가 입력될 때까지 반복 출력하기

while True:
    a = input()
    print(a)
    if a == 'q':
        break

# +
# 6079
# 언제까지 더해야 할까?
a = int(input())
s = 0
n = 0
while s < a:
    n = n + 1
    s = s + n
    
print(n)
    

# -

# 6080
# 주사위 2개 던지기
n, m = input().split()
n = int(n)
m = int(m)
for i in range(1, n+1):
    for j in range(1, m+1):
        print(i,j)

# 6081
# 16진수 구구단 출력하기
a = input()
a = int(a , 16)
for i in range(1, 16):
    print('%X'%a,'*%X'%i,'=%X'%(a*i),sep='')

# +
# 6082
# 3 6 9 게임의 왕이 되자
a = int(input())
for i in range(1,a+1):
    if i % 10 == 3:
        print('X')
    elif i % 10 == 6:
        print('X')
    elif i % 10 == 9:
        print('X')
    else:
        print(i)
# 모범답안
# n = int(input()) 
# for i in range(1, n+1) : 
#     if i%10==3 or i%10==6 or i%10==9 : 
#         print("X", end=' ') 
#     else : 
#         print(i, end=' ')


# -

# 6083
# 빛 섞어 색 만들기
r, g, b = input().split()
r, g, b = int(r),int(g),int(b)
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
print(r*g*b)

# 6084
# 소리 파일 저장용량 계산하기
h, b, c, s = input().split()
h, b, c, s = int(h), int(b), int(c), int(s)
result = format(h*b*c*s/8/1024/1024,'.1f')
print(result,'MB')

# 6085
# 그림 파일 저장용량 계산하기
w, h, b = input().split()
w, h, b = int(w), int(h), int(b)
result = format(w*h*b/8/1024/1024,'.2f')
print(result,'MB')

# +
# 6086
# 거기까지! 이제 그만~

a = int(input())
s = 0
c = 0
while True:
    s = s+1
    c = c+s
    if c>=a:
        break
print(c)
    

# +
# 6087
# 3의 배수는 통과

a = int(input())
for i in range(1,a+1):
    if i % 3 == 0:
        continue
    print(i,end=' ')

# +
# 6088
# 수 나열하기1
a, d, n = input().split()
a, d, n = int(a), int(d), int(n)
i = 1
while True:
    a+=d
    i+=1
    if i == n :
        print(a)
        break

# 모범 답안
# a,d,n=input().split() 
# a=int(a) d=int(d) n=int(n) 
# s=a 
# for i in range(2, n+1): 
#     s+=d 
#     print(s)



# +
# 6089
# 수 나열하기2
a, r, n = input().split()
a, r, n = int(a), int(r), int(n)
s = a

for i in range(2,n+1):
    s*=r

print(s)

# +
# 6090
# 수 나열하기 3
a, m, d, n = input().split()
a, m, d, n = int(a), int(m), int(d), int(n)
s = a

for i in range(2, n+1):
    print(i)
    s = s*m+d
print(s)
# -

# 6091
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
d = 1
while d % a != 0 or d % b != 0 or d % c != 0:
    d +=1
print(d)

# +
# 6092
# 이상한 출석 번호 부르기1
n = int(input()) # 번호를 부른 횟수
a = input().split() # 번호의 총 갯수 ( 1 ~ 23)

for i in range(n):
    a[i] = int(a[i])
    
d = []
for i in range(24):
    d.append(0)

for i in range(n):
    d[a[i]]+=1

for i in range(1,24):
    print(d[i], end=' ')

# +
# 6093
# 이상한 출석 번호 부르기2
n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
    
for i in range(n-1,-1,-1):
    print(a[i], end=' ')

# +
# 6094
# 이상한 출석 번호 부르기3

n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])

min = a[0]
for i in range(n):
    
    if a[i] < min : 
        min = a[i]
print(min)
# -

# 6095
# 바둑판에 흰 돌 놓기

