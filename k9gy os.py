import os
import datetime
import subprocess
import sys
import shutil

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

current_time = datetime.datetime.now()

result = subprocess.run('tasklist', shell=True, capture_output=True, text=True)

print("                                                     welcome in k9gy os")
print("_________________________________________________________________________________________________________________________")
print("enter help for show a commands")
while True:
 command = input("> ")
 if command == "help":
    print("help - помощь")
    print("clear - очистить консоль")
    print("echo <сообщение> - вывести сообщение")
    print("list - список файлов")
    print("read <имя файла> - запуск файла")
    print("time - время")
    print("add file - создать txt файл")
    print("calc - калькулятор")
    print("taskmgr - диспетчер задач")
    print("cmd - командная строка windows")
 elif command == "clear":
    os.system('cls' if os.name == 'nt' else 'clear')
 elif command == "echo":
   echo = input("введите сообщение: ")
   print(f"{echo}")
 elif command == "list":
   try:
    files = os.listdir(path)
    print(f"Файлы и папки на диске {path}:")
    for filename in files:
        print(filename)
   except PermissionError:
    print("Нет доступа к диску C:. Запустите скрипт с правами администратора.")
   except FileNotFoundError:
    print("Диск C: не найден.")
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
 else:
   print("unknown command")
 if __name__ == "__main__":
   add_to_startup_folder()