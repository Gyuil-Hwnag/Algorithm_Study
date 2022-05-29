# 양팔저울(DFS)

# 무게가 서로다른 K개의 추와 빈그릇이 있다. 모든 추의 무게는 정수이고, 그릇의 무게는 0으로 간주한다.
# 양팔저울을 한번만 이용하여 물의 무게를 그릇에 담고자 한다. 주어진 모든 추 무게의 합을 S라 하자.
# 예를 들어, 추가 3개이거, 각 추의 무게가 {1, 2, 6}이면, S=9이고, 양팔저울을 한번만 이용하여 1부터 S사이에 대응되는 
# 모든 무게의 물을 다음과 같이 그릇에 담을 수 있다. X는 그릇에 담는 물의 무게이고, P는 그릇을 나타낸다.
# 만약 추의 무게가 {1,5,7} 이면 S=13 이고, 그릇에 담을 수 있는 물의 무게는 {1,2,3,4,5,6,7,8,11,12,13} 이고,
# 1부터 S사이에서 무게에서 9와 10에 대응하는 무게의 물을 담을 수 없다.
# K개의 추 무게가 주어지면, 1부터 S사이의 정수중 측정이 불가능한 물의 무게는 몇가지가 있는지 출력

# 입력설명
# 첫번째 줄에 자연수 K가 주어진다.
# 두번째 줄에 K개의 각 추의 무게가 공백을 사이에 두고 주어진다.
# 3
# 1 5 7

# 출력설명
# 첫번째 측정이 불가능한 가지수를 출력
# 2


# 내풀이
n = int(input())
chu = list(map(int, input().split()))
max = sum(chu)
res = [0]*(max+1)
def DFS(L, sum):
    global res
    if L == n:
        if 0<sum<=max:
            res[sum]+=1
    else:
        DFS(L+1, sum+chu[L])
        DFS(L+1, sum-chu[L])
        DFS(L+1, sum)

DFS(0, 0)
for i in res:
    if i > 0:
        max-=1
print(max)


# 해설
def DFS(L, sum):
    global res
    if L==n:
        if 0<sum<=s:
            res.add(sum)
    
    else:
        DFS(L+1, sum+G[L])
        DFS(L+1, sum-G[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    n = int(input())
    G=list(map(int, input().split()))
    s=sum(G)
    res=set()
    DFS(0,0)
    print(s-len(res))