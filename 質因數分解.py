#質因數分解
ans = ''
n = 0
num = int(input('請輸入數字'))
num_= num

for i in range(2,num +1):
    if num % i == 0:
        ans = ans + str(i)
        while num > 1 and num % i == 0:
            num = num // i
            n += 1
        if n > 1:
            ans = ans + '^' + str(n)
        n = 0
        ans = ans + '*'

print(ans[:-1:])
