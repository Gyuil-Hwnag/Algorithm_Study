# 정다면체
# 두개의 정 N면체와 정 M 면체의 두 개의 주사위를 던져서 나올수 있는 눈의 가장 확률이 높은 숫자를 출력
# n, m 은 4,6,8,12,20

# 나의 풀이
def numbers(n, m):
    a = [0]*(n+m+3)

    for i in range(1, n+1):
        for j in range(1, m+1):
            a[i+j] = a[i+j]+1

    result = list()
    for i in range(0, len(a)):
        if a[i] == max(a):
            result.append(i)
            print(i, end=' ')
    
    print()
    print(result)

numbers(4,6)

# 해설
# cnt = [0]*(n+m+3)
# max = 0
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         cnt[i+j] += 1

# for i in range(n+m+1):
#     if cnt[i] > max:
#         max = cnt[i]

# for i in range(n+m+1):
#     if cnt[i] == max:
#         print(i ,end=' ')
