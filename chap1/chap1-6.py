# 중첩 반복문 (2중 for문)

# for i in range(5):
#     print('i : ', i, sep='', end=' ')
#     for j in range(5):
#         print("Second", end=' ')
#     print()

# 별 찍기
for i in range(5):
    for j in range(5-i):
        print("*", end=' ')
    print()