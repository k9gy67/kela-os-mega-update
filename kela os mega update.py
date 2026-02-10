import tkinter as tk
from tkinter import ttk
import os
import subprocess
from tkinter import messagebox
from tkinter import Label
import time

da = input("add custom apps: ")
if da == "yes":
    name = input("enter custom app name: ")
elif da == "no":
    print("starting...")
time.sleep(2)
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        
        self.attributes('-fullscreen', True)
        self.configure(bg="#04a0fa")
        self.title("kela os")

        self.protocol("WM_DELETE_WINDOW", lambda: None)

        label = tk.Label(
            self,
            text=r"""
            

╔══╗░░░░╔╦╗░░╔═════╗
║╚═╬════╬╣╠═╗║░▀░▀░║
╠═╗║╔╗╔╗║║║╩╣║╚═══╝║
╚══╩╝╚╝╚╩╩╩═╝╚═════╝

    """,
            font=("Arial", 16),
        )
        label.pack(expand=True)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        button_size = 80   
        x_offset = 20      
        y_start = 50      
        gap = 20          

        
        buttons = [
            ("корзина", self.custom_func_1),
            ("этот компьютер", self.custom_func_2),
            ("браузер", self.custom_func_3),
            ("проводник", self.custom_func_4),
            ("ос стор", self.custom_func_5),
            ("блокнот", self.custom_func_6),
            ("галерея", self.custom_func_7),
            ("калькулятор", self.custom_func_8),
            (f"{name}", self.custom_func_9)
        ]

        
        for i, (text, command) in enumerate(buttons):
            btn = ttk.Button(
                self,
                text=text,
                command=command
            )
            btn.place(
                x=x_offset,
                y=y_start + i * (button_size + gap),
                width=button_size,
                height=button_size
            )

        
        self.shutdown_button = ttk.Button(
            self,
            text="Выключить",
            command=self.quit_app
        )
        self.shutdown_button.place(
            x=20,
            y=screen_height - 60,
            width=120,
            height=30
        )

    

    def custom_func_1(self):
        self._show_message("", "корзина пуста")
        
        
    def custom_func_2(self):
        self._show_message("", "os: kela, комплектующие: в норме")
        

    def custom_func_3(self):
        import webbrowser

        url = "https://google.com"
        webbrowser.open(url)
        
    
    def custom_func_4(self):
        os.startfile(os.getcwd())
        

    def custom_func_5(self):
        self._show_message("kela store", "приложений временно нет")
        

    def _show_message(self, title: str, message: str):
        """Вспомогательный метод: открывает всплывающее окно с текстом."""
        popup = tk.Toplevel(self)
        popup.title(title)
        
        w, h = 500, 350
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        popup.geometry(f"{w}x{h}+{x}+{y}")
        popup.configure(bg="white")
        popup.grab_set()

        ttk.Label(popup, text=title, font=("Arial", 14, "bold")).pack(pady=20)
        ttk.Label(popup, text=message, wraplength=400, justify="center").pack(pady=10)

        ttk.Button(popup, text="Закрыть", command=popup.destroy).pack(pady=20)

        popup.protocol("WM_DELETE_WINDOW", popup.destroy)

    

    def custom_func_1(self):
        self._show_message("", "корзина пуста")
        
        
    def custom_func_2(self):
        self._show_message("", "os: kela, комплектующие: в норме")
        

    def custom_func_3(self):
        import webbrowser

        url = "https:google.com"
        webbrowser.open(url)
        

    def custom_func_4(self):
        os.startfile(os.getcwd())
        
    def custom_func_5(self):
        self._show_message("kela store", "приложений временно нет")
        
    
    def custom_func_6(self):
        os.system('notepad')
        
    
    def custom_func_7(self):
        import webbrowser

        url = "https://avatars.mds.yandex.net/i?id=4888b77867180de87ce8a65417c30d00_l-5910699-images-thumbs&n=13"
        webbrowser.open(url)
        

    def custom_func_8(self):
        os.system('calc')   

    def custom_func_9(self):
        self._show_message("custom func")
    
    def quit_app(self):
     self.destroy()  


if __name__ == "__main__":
    app = App()
    app.mainloop()
    root = tk.Tk()
    app = App(root)
    root.mainloop()