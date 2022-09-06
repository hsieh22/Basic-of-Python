#氣泡排序
import random
#利用random sample 不重複取樣
li = random.sample(range(0,100),10)
print(li)

def bubble_sorted(li):
    for i in range(len(li)):
        for j in range(len(li)-i-1):   
            if li[j] > li[j+1]:
                li[j],li[j+1] =li[j+1] , li[j]
    return li

print(bubble_sorted(li))