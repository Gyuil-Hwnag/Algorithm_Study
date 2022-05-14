# 후위표기식 만들기
# 중위표기식이 입력되면 후위표기식으로 변환하는 프로그램
# 중위표기식은 흔히 쓰는 표현식 즉 3+5 같은 연산자가 피연산자 사이에 있는것. 
# 후위표기식은 35+ 와 같이 연산자가 피연산자 뒤에 있는 표기식
# 예를 들어 3+5*2 를 후위표기식으로 표현하면 352*+ 로 된다. (3+5)*2 이면 35+2*

# 입력 설명
# 첫 줄에 중위표기식이 주어진다. 길이는 100을 넘지 않는다.
# 식은 1~9 의 숫자와 +,-,*,/,(,) 연산자로만 이루어진다.
# 3+5*2/(7-2)

# 출력 설명
# 후위표기식을 출력한다.
# 352*72-/+

# 내 풀이
str = input()
stack = []
for i in str:
    if i.isdecimal():
        print(i, end='')
    else:
        if i == '+' or i=='-':
            while stack and stack[-1]!='(':
                print(stack.pop(), end='')
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                print(stack.pop(), end='')
            stack.append(i)
        elif i == ')':
            while stack and stack[-1]!='(':
                print(stack.pop(), end='')
            stack.pop()
        else:
            stack.append(i)
while stack:
    print(stack.pop(), end='')
print()

# 해설
a=input()
stack=[]
res=''
for x in a:
    if x.isdecimal():
        res+=x
    else:
        if x=='(':
            stack.append()
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop()

while stack:
    res+=stack.pop()
