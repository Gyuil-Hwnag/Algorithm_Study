# 리스트와 내장함수(2)

from numpy import sometrue


a = [23, 12, 36, 53, 19]

print(a)
print(a[:3])
print(a[2:])
print(a[2:3])

print(len(a))
print()

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x ,end=' ')
print()

for x in a:
    if x%2==0:
        print(x ,end=' ')
print()

# 튜플 <- 변경 불가능
for x in enumerate(a):
    print(x)

b = (1,2,3,4,5)
print(b)
print(b[0])

for x in enumerate(b):
    print(x[0], x[1])
    print(x)

for index, value in enumerate(a):
    print(index, value)
print()

# 리스트 탐색 함수
if all(60>x for x in a):
    print("모두 60보다 작다")
else:
    print("X")

if all(30>x for x in a):
    print("모두 30보다 작다")
else:
    print("X")

if any(15>x for x in a):
    print("YES")
else:
    print("NO")