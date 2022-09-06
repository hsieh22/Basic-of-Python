def cul(x):
    n = len(str(x))
    a = 0
    y = 0
    while a < n:
        y = y + int(str(x)[a:a+1]) ** n
        a = a + 1
    return y


range,x = map(int,input('What is the upper and lower bound ? ').split())
ans = []
while x <= range:
    if x == cul(x):
        ans.insert(len(ans),x)
        x = x + 1
    else:
        x = x + 1

for answer in ans:
    print(answer, end=' ')