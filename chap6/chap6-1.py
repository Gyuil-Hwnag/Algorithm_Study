# 재귀함수를 이용한 이진수 출력
# 10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램. 
# 단 재귀함수를 이용해서 출력

# 입력설명
# 첫번쨰 줄에 10진수 N이 주어진다.
# 11

# 출력설명
# 첫번째 줄에 이진수를 출력
# 1011

# 내 풀이
n = int(input())

def num(x):
    if x!=0:
        num(x//2)
        print(x%2, end='')
    else:
        return
num(n)

# 해설
def DFS(x):
    if x==0:
        return
    else:
        DFS(x//2)
        print(x%2, end=' ')

if __name__ == "__main__":
    n = int(input())
    DFS(n)