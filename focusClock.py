import tkinter as tk
from tkinter import messagebox
import time

def start_timer():
    try:
        minutes = int(entry.get())
        seconds = minutes * 60
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            timer_display.config(text=f'{mins:02d}:{secs:02d}')
            root.update()
            time.sleep(1)
            seconds -= 1
        messagebox.showinfo("专注时钟", "时间到！")
    except ValueError:
        messagebox.showerror("错误", "请输入有效的分钟数")

root = tk.Tk()
root.title("专注时钟")

label = tk.Label(root, text="请输入专注时间（分钟）:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text="开始专注", command=start_timer)
start_button.pack(pady=10)

timer_display = tk.Label(root, text="00:00", font=("Helvetica", 48))
timer_display.pack(pady=10)

root.mainloop()
