# K번째 큰 수
# 현수는 1부터 100사이의 자연수가 적힌 N장의 카트를 가지고 있다. 같은 숫자의 카드가 여러장 있을 수 있다.
# 현수는 이중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려고 한다. 3장을 뽑을 수 있는 모든 경우를 기록한다.
# 기록한 값 중 K번째로 큰 수를 출력하는 프로그램
# 만약 큰수부터 만들어진 수가 25 25 23 23 22 20 19 ... 이고 K 값이 3이라면 K번 째 큰 값은 22 이다.

# 나의 풀이
a = [13, 15, 34, 23, 45, 65, 33, 11, 26, 42]
size = len(a)

def kstBigger(k):
    global size
    result = set()

    for i in range(0, size):
        for j in range(i+1, size):
            for m in range(j+1, size):
                result.add(a[i]+a[j]+a[m])

    result = list(result)
    result.sort()
    print(result[k-1])

kstBigger(3)

# 해설
n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set() # 중복 제거

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])

res = list(res)
res.sort(reverse=True)
print(res[k-1])
