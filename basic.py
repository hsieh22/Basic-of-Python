# print 用法、字符串概念
#last_name = 'Hsieh'
#first_name = 'Yuan Lung'
#print('Hello '+ first_name + ' ' + last_name )

#print 其他功能
#print(first_name.upper())
#print(first_name.lower())
#print(first_name.capitalize())
#print(first_name.count('u'))

#print範例
#first_name = input('What is your first name ? ')
#last_name = input('What is your last name ? ')
#print('Hello ' + first_name.capitalize() + ' ' + last_name.capitalize())

#my_name = input('What is your Name: ')
#my_sirname = input('What is your Sirname: ')
#output = 'Hello, {0} {1}'.format(my_name, my_sirname)
#output =f'Hello, {my_name} {my_sirname}'
#output = 'Hello, ' + my_name + my_sirname
#print(output)

#數值資料
#days_in_feb = 28
#錯誤
#print(days_in_feb + 'days in February')
#正確 字串轉為數字 str
#print(str(days_in_feb) + ' days in February')
#數字轉字串 int 及 float
#first_num = input('Enter first number')
#second_num = input('Enter second number')
#print(first_num + second_num)
#print(int(first_num) + int(second_num))
#print(float(first_num) + float(second_num))

# 日期資料datetime 
#from datetime import datetime , timedelta

#today = datetime.now()
#print('Today is ' + str(today))
#print('Day: ' + str(today.day))
#print('Today is ' + str(today.year) + str(today.month) + str(today.day))
#利用timedelta加減日期
#減去兩天
#two_day = timedelta(days=2)
#the_day_before_yestoday = today - two_day
#print('The day before yesterday was ' + str(the_day_before_yestoday))

#字串轉日期資料格式
#birthday = input("Whar's your birthday (dd/mm/yyyy) ?")
#birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
#print('Birthday: ' + str(birthday_date))

#錯誤處理:語法錯誤 運行錯誤 邏輯錯誤

#語法錯誤(if 沒加冒號)
# x = 1
# y = 3
#if x < y
#    print('Sucess')

#運行錯誤(除以0)
# x = 2
# y = 0
#print(x / y)

#邏輯錯誤(x不大於y)
#x = 1
#y = 3
#if x > y:
#    print('Success')

#if 條件邏輯
#country = 'TAIWAN'
#if country.lower() == 'taiwan':
#  print('Yes')

#if else else or in 條件邏輯的介紹幾級應用
#A = 0
#if A == 3 or A== 2:
#  print('YA')
#elif A in(1,0,-1):
#  print('Umm')
#else:
#  print('No')

#複雜條件
#x = 5
#y = 4
#if x > 3:
#    if y > 3:
#        print('ya')

#if x > 3 and y > 3:
#    print('YA')

#if x > 3 and y > 3:
#    honour_roll = True
#else:
#    honour_roll = False
#隔了幾行程式碼
#if honour_roll:
#    print('ya')

#列表Array
#names = ['Tim' , 'Eastin' , 'Bill']
#取得列表內資料數
#print(len(names))
#在列表中插入資料
#names.insert(0,'Jhon')
#print(names)
#排列列表內的資料
#names.sort()
#print(names)
#列表
#presenters = names[1:3]
#print(presenters)

#Dictionary字典
# people = {'Apple':400,'Joey':600,'Bella':50,'2th King':10000}
# people[2002] = 2
# print(people)
# print(people.keys())
# print(people.values())
# people = sorted(people.items(), key=lambda x:x[1])    #排序，items會將dictionary轉為tuple
# print(people)

#for迴圈 記得冒號

#for name in ['Tim' , 'Jack' , 'Tom']:
#    print(name)

#people = ['Tim' , 'Jack' , 'Mike']
#for name in people:
#    print(name)

#for index in range(2, 5):
#    print(index)

#可以有條件的while迴圈

#name = ['Tim' , 'Jack' , 'Tom']
#index = 0
#while len(name) > index:
#    print(name[index])
#    index = index + 1

#自訂函數function

#from datetime import datetime
#print the current and task name
#def print_time(task_name):
#  print(datetime.now())
#    print()

#print('Tim')
#print_time('print name')

#for x in range(1,11):
#    print(x)
#print_time('loop completed')

#def get_initial(name):
#    initial = name[0:1].upper()
#    return initial

#first_name = input('Enter your first name')
#last_name = input('Enter your last name')
#因為first_name是變數名稱，不需加引號
#print('Your initial are: '+ get_initial(first_name) + get_initial(last_name) )

#參數化函數，可有多個參數
#def get_initial(name, force_uppercase = True):
#    if force_uppercase :
#        initial = name[0:1].upper()
#    else :
#        initial = name[0:1]
#    return initial

#print(get_initial('tim', False))
#print(get_initial('mike'))

#多重輸入
#a,b = map(int,input().split())
#print(a ,end =' ')
#print(b)

#Importing a module

# import module as namespace
#import helpers
#helpers.display('XXX', is_warning=True)

# import all into current namespace
#from helpers import *
#display('OOO', is_warning=True)

# import specific items into current namespace
#from helpers import display
#display('ABC', is_warning=True)

#Packages

# from colorama import Fore,Back,Style
# print (Fore.RED + "some red text")
# print (Back.GREEN + "and with a green background")
# print (Style.DIM + "and in dim text")
# print (Style.RESET_ALL)
# print ("back to normal now!!")

# import tkinter as tk
# #建立主視窗
# win = tk.Tk()
# win.title('tkinter test')

# #常住主視窗
# win.mainloop()

# btn = tk.Button(text = 'btn')
# btn.pack

# x = -3
# if abs(x) == 3:
#     print('qq')

# from pip._vendor.colorama import init, Fore
# print(Fore.RED + '123')
# print(Fore.GREEN+'12345')
# print(Fore.WHITE+'')

#常見問題 用global
# x = 0
# def test():
#     global x
#     x = x+1
#     return

# test()
# print(x)


# length = input("多長？")
# length = int(length)

# print("       我是長長長長頸鹿喔～!           ")
# print("                                       ")
# print("         _  o o                        ")
# print("          \\  \\|/ _,                  ")
# print("      __.'   /`_/                      ")
# print("    /`    u   #                        ")
# print("    `c-_..__,/ ##                      ")
# print("           ):'##                       ")

# for x in range(length):
#     print("           |   ##                      ")
#     print("           |:.:##                      ")
    
# print("           |   ##                      ")
# print("           |:.:##                      ")
# print("           |.  ##                      ")
# print("           |:.'##                      ")
# print("           |.  ##                      ")
# print("          /  ' ##                      ")
# print("          |.:'  ##                     ")
# print("          ::' .:#                      ")
# print("         / '     '#                    ")
# print("         |  .: '::.`'-..__             ")
# print("         |:.         .::' `',          ")
# print("         |:::   ':.       .:, \\       ")
# print("           \\ ', .  .::' .::  | |      ")
# print("          |'.|.:|  '     '  / \\#      ")
# print("          |   \\ '|._.::  |   |##      ")
# print("          | /|.:|  `""`| .:|##         ")
# print("          / ||  /     |   '|           ")
# print("           \\ // |     \\:'   \\       ")
# print("          | / \\ /      |  \\          ")
# print("          | || |       | || /          ")
# print("          | || |       | || |          ")
# print("         _/ j| |      _/ J| |          ")
# print("        (/_/_/ J     (/_/_/ j          ")
# print("           (/_/         (/_/           ")

#切片 slice
# s = 'abcdefghijk'
# n1 = s[1:5:1]
# n2 = s[1:-1:2]
# n3 = s[6:1:-1]
# n4 = s[::-1]  #字串顛倒
# print(n1)
# print(n2)
# print(n3)
# print(n4)


'''
import random  as rd
a = []
b = random.randint(1,10)

for k in range(0,b):
    a.append(0)
    a[k+1] = k+1
print(a)

import random  as rd
a = []
b = rd.randint(1,10)

for k in range(0,b):
    a.append(0)
    a[k] = k+1
print(a)
'''
'''
import cv2

#讀取圖檔
img = cv2.imread('sun.png')
#建立視窗
cv2.namedWindow('My Image', cv2.WINDOW_KEEPRATIO)

#顯示圖片
cv2.imshow('My Image', img)
'''

# import pandas as pd

# WeeklyTempMean = [17.96071428571429, 18.491666666666667, 16.988095238095237, 16.0125, 17.577380952380953, 16.22142857142857, 18.0, 16.24047619047619, 17.421428571428574, 16.839285714285715, 19.09166666666667, 19.003333333333334, 19.696428571428573, 21.314285714285713, 21.28333333333333, 24.264583333333334, 19.723809523809525, 22.05, 24.101190476190478, 22.959166666666665, 25.09047619047619, 24.54642857142857, 25.974999999999998, 26.224999999999998, 27.846428571428568, 27.39047619047619, 27.711904761904766, 27.9125, 27.525000000000002, 28.651190476190475, 26.28571428571428, 27.544166666666666, 26.62142857142857, 26.384523809523806, 24.403571428571432, 23.58148148148148, 25.12857142857143, 23.675, 17.89047619047619, 21.904999999999998, 22.291666666666668, 20.21904761904762, 20.139285714285712, 19.990624999999998, 16.633333333333333, 18.38809523809524, 18.825]

# WeeklyTempMeanDataFrame = pd.DataFrame(WeeklyTempMean,index =['a', 'b', 'c', 'd', 'e', 'f', 'g'],columns=['Mean TEMP'])
# print(WeeklyTempMeanDataFrame)


# code-runner python2 to python3
# https://blog.csdn.net/xukang95/article/details/90483660
# Go to the users//"Username"//.vscode//extensions//"The code runner name"//package.json and edit it there
# 將裡面的python -u修改為 python3 -u