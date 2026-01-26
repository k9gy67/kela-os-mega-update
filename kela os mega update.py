import tkinter as tk
from tkinter import ttk
import os

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        
        self.attributes('-fullscreen', True)
        self.configure(bg="#04a0fa")
        self.title("kela os")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        button_size = 80   # Размер кнопки (80×80 px)
        x_offset = 20      # Отступ от левого края
        y_start = 50      # Начальный отступ сверху
        gap = 20          # Промежуток между кнопками

        # Список кнопок: текст + команда 
        buttons = [
            ("корзина", self.custom_func_1),
            ("этот компьютер", self.custom_func_2),
            ("браузер", self.custom_func_3),
            ("проводник", self.custom_func_4),
            ("ос стор", self.custom_func_5),
            ("блокнот", self.custom_func_6),
            ("галерея", self.custom_func_7),
            
        ]

        # Создаём и размещаем кнопки
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

        # Кнопка Выключить
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

    #  Общие функции

    def custom_func_1(self):
        self._show_message("", "корзина пуста")
        
    def custom_func_2(self):
        self._show_message("", "os: kela, комплектующие: в норме")

    def custom_func_3(self):
        import webbrowser

        url = "https://google.com"
        webbrowser.open(url)
    
    def custom_func_4(self):
        self._show_message("файлы", "system:5 кб")

    def custom_func_5(self):
        self._show_message("", "зачем тебе приложения?")

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
        self._show_message("файлы", "system:5 кб")

    def custom_func_5(self):
        self._show_message("kela store", "приложений временно нет")
    
    def custom_func_6(self):
        os.system('notepad')
    
    def custom_func_7(self):
        import webbrowser

        url = "https://avatars.mds.yandex.net/i?id=4888b77867180de87ce8a65417c30d00_l-5910699-images-thumbs&n=13"
        webbrowser.open(url)

    def quit_app(self):
        """Закрывает приложение."""
        self.destroy()



if __name__ == "__main__":
    app = App()
    app.mainloop()
