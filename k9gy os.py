import os
import datetime
import subprocess
import sys
import shutil
import platform
import urllib.request

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

path = "C:\\"
paths = "D:\\"

current_time = datetime.datetime.now()

result = subprocess.run('tasklist', shell=True, capture_output=True, text=True)

print("                                                     welcome in k9gy os")
print("_________________________________________________________________________________________________________________________")
print("type help for show a commands")
while True:
 command = input("> ")
 if command == "help":
    print("help - помощь")
    print("clear - очистить консоль")
    print("echo <сообщение> - вывести сообщение")
    print("list - список файлов на диске C или D если есть")
    print("read <имя файла> - запуск файла")
    print("time - время")
    print("add file - создать txt файл")
    print("calc - калькулятор")
    print("taskmgr - диспетчер задач")
    print("cmd - командная строка windows")
    print("sys - данные об ос")
    print("exit - выйти")
    print("pc info - информация о пк")
    print("browse - открыть сайт")
 elif command == "clear":
    os.system('cls' if os.name == 'nt' else 'clear')
 elif command == "echo":
   echo = input("введите сообщение: ")
   print(f"{echo}")
 elif command == "list":
   disk = input("введите диск > ")
   if disk == "C":
    try:
     files = os.listdir(path)
     print(f"Файлы и папки на диске {path}:")
     for filename in files:
        print(filename)
    except PermissionError:
     print("Нет доступа к диску C:. Запустите скрипт с правами администратора.")
    except FileNotFoundError:
     print("Диск C: не найден.")
   elif disk == "D":
    try:
     files = os.listdir(paths)
     print(f"Файлы и папки на диске {paths}:")
     for filename in files:
        print(filename)
    except PermissionError:
     print("Нет доступа к диску D:. Запустите скрипт с правами администратора.")
    except FileNotFoundError:
     print("Диск D: не найден.")
 elif command == "read":
   file_path = input("введите полный путь к файлу: ")
   os.system(f'"{file_path}"')
 elif command == "time":
   print("Текущее время:", current_time.strftime("%H:%M:%S"))
 elif command == "add file":
   text = input("введите текст в файле: ")
   with open("k9gy os file.txt", "w", encoding="utf-8") as file:
    file.write(f"{text}\n")
 elif command == "calc":
   print(eval(input("Введите выражение: ")))
 elif command == "taskmgr":
   print(result.stdout)
 elif command == "cmd":
   os.system('cmd')
 elif command == "sys":
   print(r""""
         00        00
         00       00
         00      00
         00     00             os: k9gy os
         00    00
         00   00
         00  00
         00 00
         00  00
         00   00               version:1.0
         00    00
         00     00
         00      00
         """)
 elif command == "exit":
   break
 elif command == "pc info":
   print("Операционная система:", platform.system())
   print("Имя компьютера:", os.environ.get('COMPUTERNAME', 'Не найдено'))
   print("Версия ОС:", platform.version())
   print("Архитектура:", platform.machine())
 elif command == "browse":
   site = input("введите сайт(например google.com) >")
   url = f"https://{site}"  
try:
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')  
        print(html)
except Exception as e:
    print("Ошибка при получении сайта:", e)
if __name__ == "__main__":
   add_to_startup_folder()