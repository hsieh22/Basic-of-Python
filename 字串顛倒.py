#coding=utf-8
#字串顛倒
a = input('請輸入字串')
b = a[::-1]
print(b)

a = input('請輸入字串')
b = list(a)
b.reverse()
b = ''.join(b)
print(b)

a = input('請輸入字串')
b = ''
for i in a:
    b = i + b
print(b)