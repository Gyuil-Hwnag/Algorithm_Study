# K 번째 수
# N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열에서 s번째부터 e번째 까지의 수를 
# 오름차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램

# 나의 풀이
a = [6, 2, 5, 3]
def kST(s, e, k):
    b = []
    b = a[s-1:e]
    b.sort()
    for i in b:
        if(i == k-1):
            print(b[i])

kST(1,4,2)

# 해설
T = a
def kST():
    for t in range(T):
        n, s ,e , k = map(int, input().split())
        a = list(map(int, input().split()))
        a = a[s-1:e]
        a.sort()
        print(a[k-1])

kST()