# 후위식 연산
# 후위식 연산식이 주어지면 연산한 결과를 출력하는 프로그램
# 만약 3*(5+2)-9 을 후위연산식으로 표현하면 352+*9- 로 표현되며 결과는 21 이다.

# 입력설명
# 첫 줄에 후위연산식이 주어진다. 연산식의 길이는 50을 넘지 않는다. 식은 1~9 의 숫자와 +, -, *, /, (, ) 연산자로만 이루어진다.
# 352+*9-

# 출력설명
# 연산한 결과를 출력

# 내 풀이
str = input()
inputList = []
stack = []
for i in str:
    inputList.append(i)

res = 0
for i in inputList:
    if i.isdecimal():
        stack.append(int(i))
    else:
        if i == '+':
            res = stack.pop() + stack.pop()
        elif i == '-':
            se = stack.pop()
            fi = stack.pop()
            res = fi - se
        elif i == '*':
            res = stack.pop() * stack.pop()
        else:
            se = stack.pop()
            fi = stack.pop()
            res = fi / se
        stack.append(res)
print(stack[0])

# 해설
a=input()
stack=[]
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x=='+':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n1+n2)
        elif x=='-':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2-n1)
        elif x=='*':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n1*n2)
        elif x=='/':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2/n1)
print(stack[0])

