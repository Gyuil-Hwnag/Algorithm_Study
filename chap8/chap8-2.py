# 네트워크 선 자르기(Top-Down : 재귀, 메모이제이션)

# 현수는 네트워크선을 1m, 2m의 길이를 갖는 선으로 자르려고 한다.
# 예를 들어 4m의 네트워크선이 주어진다면
# 1) 1m+1m+1m+1m
# 2) 2m+1m+1m
# 3) 1m+2m+1m
# 4) 1m+1m+2m
# 5) 2m+2m
# 등의 5가지 방법을 생각할 수 있다. 2 와 3 과 4의 경우 
# 왼쪽을 기준으로 자르는 위치가 다르면 다른 경우로 생각한다.
# 그렇다면, 네트워크 선의 길이가 Nm 이라면 몇 가지의 자르는 방법을 생각할 수 있는지

# 입력설명
# 첫째줄에 네트워크선의 총 길이인 자연수 N이 주어진다.
# 21

# 내풀이
n = int(input())

def DFS(L):
    if L<0:
        return 0
    elif L==0:
        return 1
    else:
        return DFS(L-1)+DFS(L-2)

res = DFS(n)
print(res)

# 해설
# dy 로 기록해주기 (메모리제이션) <- 안한다면 그냥 재귀 (속도차이 엄청남)
def DFS(len):
    # 이부분 꼭 해주기, 안하면 속도 엄청 느려짐
    if dy[len]>0:
        return dy[len]
    if len==1 or len==2:
        return len
    else:
        dy[len]=DFS(len-1)+DFS(len-2)
        return dy[len]

if __name__ == "__main__":
    n=int(input())
    dy=[0]*(n+1)
    print(DFS(n))