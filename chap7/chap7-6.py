# 알파코드(DFS)

# 철수와 영희는 서로의 비밀편지를 암호화해서 서로 주고받기로 했다. 그래서 서로 어떻게 암호화를 할 것인지를 의논했다.
# 영희 : 알파벳 A에는 1로, B에는 2로 이렇게 해서 Z에는 26을 할당하여 번호로 보내기로 하자.
# 철수 : BEAN으로 보내면 24114 여서 복호화 하면 BEAAD, YADD, YAN, YKD, BEKD로 BEAN 말고도 5가지나 더 존재.
# 당신은 위와 같은 영희의 방법으로 암호화된 코드가 주어지면 그것을 알파벳으로 복원하는데 얼마나 많은 방법이 있는지 구하여라.

# 입력설명
# 첫번째 줄에 숫자로 암호화된 코드가 입력된다. (코드는 0부터 시작하지는 않는다. 코드의 길이는 최대 50이다.) 
# 0이 입력되면 입력종료를 의미한다.
# 25114

# 출력설명
# 입력된 코드를 알파벳으로 복원하는데 몇가지의 방법이 있는지 각 경우를 출력. 그 가지수도 출력한다.
# 단어의 출력은 사전순으로 출력한다.
# BEAAD
# BEAN
# BEKD 
# YAAD
# YAN 
# YKD
# 6

# 내설명


# 풀이
char = input()
numlist = list()
for i in char:
    if int(i) == 0:
        break
    numlist.append(int(i))
print(numlist)

count = 0
charlist = list()
def DFS(L, Before):
    global count
    if L == len(numlist):
        count+=1
        for i in charlist:
            print(chr(i+64), end='')
        print()
    elif L == len(numlist)-1:
        if Before != 0:
            num = Before*10+numlist[L]
            charlist.append(num)
            DFS(L+1, 0)
        else:
            charlist.append(numlist[L])
            DFS(L+1, 0)
    else:
        if Before != 0:
            num = Before*10+numlist[L]
            if num <= 26:
                charlist.append(num)
                DFS(L+1, 0)
            else:
                return
        else:
            charlist.append(numlist[L])
            DFS(L+1, 0)
            charlist.pop()
            charlist.pop()
            DFS(L+1, numlist[L])

DFS(0, 0)
print(count)

# 해설
# def DFS(L, P):
#     global cnt
#     if L==n:
#         cnt+=1
#         for j in range(P):
#             print(chr(res[j]+64),end='')
#         print()
#     else:
#         for i in range(1, 27):
#             if code[L] == i:
#                 res[P]=i
#                 DFS(L+1, P+1)
#             elif i>=10 and code[L]==i//10 and code[L+1]==i%10:
#                 res[P] = i
#                 DFS(L+2, P+1)

# if __name__ == "__main__":
#     code = list(map(int, input()))
#     n = len(code)
#     code.insert(n, -1)
#     res = [0]*(n+3)
#     cnt = 0
#     DFS(0,0)
#     print(cnt)