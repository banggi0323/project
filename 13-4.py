import tkinter as tk
from tkinter import ttk

def on_submit():
    name = entry_name.get()
    grade = grade_var.get()
    hobbies = []

    if hobby_vars[0].get():
        hobbies.append("영화시청")
    if hobby_vars[1].get():
        hobbies.append("음악감상")
    if hobby_vars[2].get():
        hobbies.append("사진찍기")
    if hobby_vars[3].get():
        hobbies.append("운동")

    print("\n" + name)
    print(grade)
    for h in hobbies:
        print(h)

win = tk.Tk()
win.title("회원 가입")

# 이름 입력
ttk.Label(win, text="이름:").grid(row=0, column=0, sticky="w")
entry_name = ttk.Entry(win, width=20)
entry_name.grid(row=0, column=1, columnspan=4, sticky="w")

# 학년 선택 (Radiobutton)
ttk.Label(win, text="학년:").grid(row=1, column=0, sticky="w")
grade_var = tk.StringVar(value="1")
ttk.Radiobutton(win, text="1학년", variable=grade_var, value="1").grid(row=1, column=1)
ttk.Radiobutton(win, text="2학년", variable=grade_var, value="2").grid(row=1, column=2)
ttk.Radiobutton(win, text="3학년", variable=grade_var, value="3").grid(row=1, column=3)
ttk.Radiobutton(win, text="4학년", variable=grade_var, value="4").grid(row=1, column=4)

# 취미 선택 (Checkbutton)
ttk.Label(win, text="취미:").grid(row=2, column=0, sticky="w")
hobby_texts = ["영화시청", "음악감상", "사진찍기", "운동"]
hobby_vars = [tk.BooleanVar() for _ in hobby_texts]
for i, text in enumerate(hobby_texts):
    ttk.Checkbutton(win, text=text, variable=hobby_vars[i]).grid(row=2, column=i+1)

# 입력 / 종료 버튼
ttk.Button(win, text="입력", command=on_submit).grid(row=3, column=2, pady=5)
ttk.Button(win, text="종료", command=win.destroy).grid(row=3, column=3, pady=5)

win.mainloop()
