# 소수(에라토스테네스 체)
# 자연수 N 이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램
# 만약 20이 입려고디면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19 이렇게 총 8개 이다.

# 나의 풀이
# def eratos(x):
#     res = [0]*(x+1)
#     for i in range(2, x+1):
#         count = 1
#         while i*count < x+1:
#             res[i] = res[i]+1
#             count += 1

#     # 0,1 이 있으므로 -2
#     result = -2
#     for i in res:
#         if i == 1:
#             result += 1

#     print(result)

# eratos(20)

# 해설
n = int(input())
ch = [0]*(n+1)
cnt = 0
for i in range(2, n):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1

print(cnt)
