# 2차원 리스트 생성및 접근
a = [0]*3
print(a)

# 1 
a = [[0]*3 for _ in range(3)]
print(a)

a[0][1] = 1
print(a)

for x in a:
    print(x)

# 2 
a = [[0]*3]*3
print(a)

a[0][1] = 1
print(a)

for x in a:
    print(x)

# 1,2 의 차이점 알아보기
# 2의 경우 [0,0,0]을 참조하는것 만듬

a = [[0]*3 for _ in range(3)]
print(a)
a[0][1] = 1

for x in a:
    for y in x:
        print(y, end=' ')
    print()

