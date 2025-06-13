import tkinter as tk
from tkinter import ttk, messagebox
import os

def buildgui():
    global entry_word, entry_meaning

    ttk.Label(win, text="단어:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entry_word = ttk.Entry(win, width=20)
    entry_word.grid(row=0, column=1, padx=5, pady=5)

    ttk.Button(win, text="검색", command=search_word).grid(row=0, column=2, padx=5)
    ttk.Button(win, text="추가", command=add_word).grid(row=0, column=3, padx=5)

    ttk.Label(win, text="뜻:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_meaning = ttk.Entry(win, width=40)
    entry_meaning.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="we")

    ttk.Button(win, text="초기화", command=reset_fields).grid(row=2, column=1, pady=10)
    ttk.Button(win, text="종료", command=close_program).grid(row=2, column=2, pady=10)
    
words = {}

def load_words():
    if os.path.exists("words.txt"):
        with open("words.txt", "r", encoding="utf-8") as f:
            for line in f:
                if ":" in line:
                    word, meaning = line.strip().split(":", 1)
                    words[word] = meaning

def save_words():
    with open("words.txt", "w", encoding="utf-8") as f:
        for word, meaning in words.items():
            f.write(f"{word}:{meaning}\n")

def add_word():
    word = entry_word.get().strip()
    meaning = entry_meaning.get().strip()
    if word and meaning:
        words[word] = meaning
        messagebox.showinfo("추가 확인", f"단어 {word}를 추가했습니다.")
    else:
        messagebox.showwarning("입력 오류", "단어와 뜻을 모두 입력하세요.")

def search_word():
    word = entry_word.get().strip()
    if word in words:
        entry_meaning.delete(0, tk.END)
        entry_meaning.insert(0, words[word])
    else:
        messagebox.showinfo("검색 오류", f"{word}란 단어는 없습니다.")
        entry_meaning.delete(0, tk.END)

def reset_fields():
    entry_word.delete(0, tk.END)
    entry_meaning.delete(0, tk.END)

def close_program():
    save_words()
    win.destroy()

win = tk.Tk()
win.title("단어장")
buildgui()

load_words()
win.mainloop()
