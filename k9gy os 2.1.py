import tkinter as tk
import subprocess
import ctypes

HWND_TOPMOST = -1
SWP_NOMOVE = 0x0002
SWP_NOSIZE = 0x0001

def set_always_on_top(root):
    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
    ctypes.windll.user32.SetWindowPos(
        hwnd,
        HWND_TOPMOST,
        0, 0, 0, 0,
        SWP_NOMOVE | SWP_NOSIZE
    )

def keep_on_top_periodically(root):
    set_always_on_top(root)
    root.after(1000, keep_on_top_periodically, root)

def execute_command(event=None):
    cmd = entry.get()
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        output = e.output
    text.delete('1.0', tk.END)
    text.insert(tk.END, output)
    if cmd == "exit":
        root.destroy()

root = tk.Tk()
root.title("k9gy os")
root.geometry("700x400")
root.attributes("-fullscreen", True)
root.configure(bg="black")
root.protocol("WM_DELETE_WINDOW", lambda: None)

entry = tk.Entry(root, width=80)
entry.pack(pady=10)

entry.bind('<Return>', execute_command)

text = tk.Text(root, bg="black", fg="white")
text.pack(expand=True, fill='both')

keep_on_top_periodically(root)
root.mainloop()