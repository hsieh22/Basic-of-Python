import random
import tkinter as tk

#基本視窗
win = tk.Tk()
win.title('Random Number Generator')
win.geometry('300x200')
win.config(background = '#323232')

#設置物件
title_text = tk.Label(text ='Random Number Generator', fg = 'skyblue', bg= '#323232')
title_text.config(font = 'Arial 15')
title_text.pack()

min_range = tk.Label(text = 'Min ange', fg = 'white', bg = '#323232')
min_range.pack()

min_entry = tk.Entry(text = 'min')
min_entry.pack()

max_range = tk.Label(text = 'Max ange', fg = 'white', bg = '#323232')
max_range.pack()

max_entry = tk.Entry()
max_entry.pack()

num_show = tk.Label(text = '', fg = 'white', bg = '#323232' )
num_show.pack()

generate_btn = tk.Button(text = 'Generate')
generate_btn.pack()

#主要函式
def gen_num():
    min_val = int(min_entry.get())
    max_val = int(max_entry.get())
    x = random.randint(min_val, max_val)
    num_show.config(text = str(x))

generate_btn.config(command = gen_num)

#常駐主視窗
win.attributes('-topmost', True)
win.mainloop()