# 동전교환(냅색 알고리즘: Knapsack Algorithm)

# 다음과 같이 여러 단위의 동전들이 주어져 있을 때, 거스름돈을 가장 적은 수의 동전으로 교환해주려면 어떻게 주면 되는지?
# 각 단위의 동전은 무한정 쓸 수 있다.

# 입력설명
# 첫번째 줄에 동전의 종류개수 N이 주어진다.
# 두번째 줄에는 N개의 동전의 종류가 주어지고, 그 다음줄에 거슬러 줄 금액 M이 주어진다.
# 각 동전의 종류는 100원을 넘지 않는다.
# 3
# 1 2 5
# 15

# 출력설명
# 첫번째 줄에 거슬러 줄 동전의 최소개수를 출력한다.
# 3

# 내풀이
n = int(input())
coin = list(map(int, input().split()))
coin.sort(reverse=True)
sum = int(input())

dy = [sum]*(sum+1)
for i in range(len(coin)):
    for j in range(coin[i], sum+1):
        dy[j] = min(dy[j], dy[j-coin[i]]-coin[i]+1)

print(min(dy))

# 해설
if __name__ == "__main__":
    n=int(input())
    coin=list(map(int, input().split()))
    m=int(input())
    dy=[1000]*(m+1)
    dy[0]=0
    for i in range(n):
        for j in range(coin[i], m+1):
            dy[j]=min(dy[j], dy[j-coin[i]]+1)
    print(dy[m])
