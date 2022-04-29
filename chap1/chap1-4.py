# 반복문 (for, while)

# a = range(1, 11)
# print(list(a))

# for i in range(10):
#     print(i)

# for i in range(10, 0, -2):
#     print(i)

# i = 1
# while i<=10:
#     print(i)
#     i = i+1

# i = 10
# while i>0:
#     print(i)
#     i = i-1

# i = 1
# while True:
#     print(i)
#     i = i+1
#     if(i > 10):
#         break

# for i in range(1, 11):
#     if i%2 == 0:
#         continue
#     print(i)

for i in range(1, 11):
    print(i)
    if i == 11:
        break
else:
    print("not break")