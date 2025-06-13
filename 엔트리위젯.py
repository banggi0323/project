import tkinter as tk
from tkinter import ttk

def buildgui():
    global text_label
    text_label = ttk.Label(win, text='안녕하세요')

    global name
    name = tk.StringVar()
    input_entry = ttk.Entry(win, textvariable=name)

    input_btn = ttk.Button(win, text='입력',
                           command=input_btn_handler)
    quit_btn = ttk.Button(win, text='종료',
                           command=win.destroy)
    text_label.pack()
    input_entry.pack()
    input_btn.pack()
    quit_btn.pack()

def input_btn_handler():
    text_label.configure(text='반가워요, ' + name.get())
    name.set('')
    
win = tk.Tk()
win.title('라벨 위젯 예1')
buildgui()
win.mainloop()
