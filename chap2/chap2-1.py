# K 번째 약수
# 어떤 자연수 p,q가 있을 때 만일 p를 q로 나누었을 떄
# 나어지가 0이면 q는 p의 약수이다.

def kPrime(n , k):
    # n, k = map(int, input().split())
    cnt = 0

    for i in range(1, n+1):
        if n%i == 0:
            cnt+=1
        if cnt == k:
            print(i)
            break
    else:
        print(-1)

kPrime(6, 3)