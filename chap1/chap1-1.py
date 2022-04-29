# 변수명
a=1
A=2
A2=3
print(a, A, A2)
a,b,c = 3,2,1
print(a,b,c)

# 값 교환
a,b = 10,20
print(a,b)
a,b = b,a
print(a,b)

# 변수 타입
a = 12345
print(a)
print(type(a))

a = 12.3456789012345678901234567 # float 는 8byte
print(a)
print(type(a))

a = 'student'
print(a)
print(type(a))
a = "student"
print(a)
print(type(a))
a = 's'
print(a)
print(type(a))

# 출력 방식
a,b,c = 1,2,3
print(a,b,c)
print("number : ",a,b,c)

print(a,b,c, sep='')
print(a,b,c, sep=',')
print(a,b,c, sep='\n')
print(a, end=' ')
print(b, end='')
print(c, end=',')
