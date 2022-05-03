# 두 리스트 합치기
# 오름차순으로 정렬이 된 두 리스트가 주어지면 
# 두 리스트를 오름차순으로 합쳐 출력하는 프로그램

# 내 풀이
x = list(map(int, input().split()))
y = list(map(int, input().split()))
z = list()

p1, p2 = 0, 0
while True:
    if p1+1 > len(x):
        z = z+y[p2::]
        break
    if p2+1 > len(y):
        z = z+x[p1::]
        break
    if x[p1]<=y[p2]:
        z.append(x[p1])
        print(z)
        p1 += 1
    else:
        z.append(y[p2])
        print(z)
        p2 += 1
print(z)

# 해설
# sort() 를 사용하지 말고 <- 속도 차이 때문에
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1=p2=0
c=[]
while p1<n and p2<m:
    if a[p1]<=b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2]

for x in c:
    print(x, end=' ')