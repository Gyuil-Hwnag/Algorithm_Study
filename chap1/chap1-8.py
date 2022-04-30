# 리스트, 내장함수(1)
import random as r

a = []
print(a)

b = list()
print(b)

a = [1,2,3,4,5]
print(a)
a.append(6)
print(a)
print(a[0])

b = list(range(1, 11))
print(b)

# append
a.append("+")
c = a+b
print(c)

a.insert(3, 7)
print(a)

# remove
a.remove('+')
print(a)

a.pop()
print(a)

a.pop(3)
print(a)

# index 번호 출력
print(a.index(5))

a.append("123")
print(a.index("123"))

# min, max
a = list(range(1, 11))
print(a)
print(sum(a))
print(max(a))

print(min(a))
print(min(7, 5))
print(min('A', 'Z'))

# shuffle, sort, reverse
r.shuffle(a)
print(a)

# 오름차순
a.sort()
print(a)

# 내림차순
a.sort(reverse=True)
print(a)

a.reverse()
print(a)

a.clear()
print(a)