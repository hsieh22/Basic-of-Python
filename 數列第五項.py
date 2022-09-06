a,b,c,d = map(int,input().split())
if d - c == c -b == b - a :
    e = d + (d - c)
else:
    e = d * (d / c)
for x in a,b,c,d,e:
    print(x, end =' ')