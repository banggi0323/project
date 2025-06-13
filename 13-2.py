import tkinter as tk
from tkinter import ttk

def buildgui():
    label1 = ttk.Label(win, text="화씨")
    label1.grid(row=0, column=0)

    global tmp1, entry_f
    tmp1 = tk.DoubleVar()
    entry_f = ttk.Entry(win, textvariable=tmp1)
    entry_f.grid(row=0, column=1)

    label2=ttk.Label(win, text="섭씨")
    label2.grid(row=0, column=2)

    global tmp2, entry_c
    tmp2 = tk.DoubleVar()
    entry_c = ttk.Entry(win, textvariable=tmp2)
    entry_c.grid(row=0, column=3)

    btn1 = ttk.Button(win, text="화씨->섭씨", command=f_to_c)
    btn2 = ttk.Button(win, text="섭씨->화씨", command=c_to_f)
    btn3 = ttk.Button(win, text="초기화", command=reset)
    btn4 = ttk.Button(win, text="종료", command=win.destroy)
    btn1.grid(row=1, column=0)
    btn2.grid(row=1, column=1)
    btn3.grid(row=1, column=2)
    btn4.grid(row=1, column=3)
    
def f_to_c():
    f = entry_f.get()
    c = (float(f) - 32) / 1.8
    entry_c.delete(0, tk.END)
    entry_c.insert(0, f"{c:.1f}")

def c_to_f():
    c = entry_c.get()
    f = float(c) * 1.8 + 32
    entry_f.delete(0, tk.END)
    entry_f.insert(0, f"{f:.1f}")

def reset():
    entry_f.delete(0, tk.END)
    entry_c.delete(0, tk.END)

win = tk.Tk()
win.title("온도변환기-2단계")
buildgui()
win.mainloop()
