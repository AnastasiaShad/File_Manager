from tkinter import *
from tkinter import ttk
import re
from re import split
from tkinter.font import Font
from tkinter import messagebox
from folder import Folder
import os
from config import global_folder

class Registation(Tk):
    main_user_flag = False
    main_dirr = ''
    def __init__(self, path, delimiter):
        super().__init__()
        self.title("Регистрация/вход пользователя")
        self.path = path
        self.delimiter = delimiter
        self.geometry('400x350')
        self.configure(background="#8AB5B5")

        self.login = StringVar()
        self.passw = StringVar()
        self.welcome = StringVar()

        self.welcome.set('Добро пожаловать!')
        Label(self,textvariable=self.welcome, font=Font(size=15, weight="bold"), pady=20,background="#8AB5B5", fg="#364544").pack(side=TOP)

        Label(self, text="Логин:", font=Font(size=15, weight="bold"), pady=20,background="#8AB5B5", fg="#364544").pack(side=TOP)
        self.entry_name = Entry(self, textvariable=self.login).pack(side=TOP)

        Label(self, text="Пароль:", font=Font(size=15, weight="bold"), pady=20, background="#8AB5B5", fg="#364544").pack(side=TOP)
        self.entry_passwd = Entry(self, show="*", textvariable=self.passw).pack(side=TOP)

        # style = ttk.Style()
        # style.configure("BW.TLabel", foreground="white", background="#5B7574")
        s = ttk.Style()
        s.configure('Wild.TButton',
                    background='#8AB5B5',
                    foreground='#8AB5B5',
                    highlightthickness='20',
                    font=('Helvetica', 14, 'bold'))
        s.map('Wild.TButton',
              foreground=[('disabled', '#364544'),
                          ('pressed', '#364544'),
                          ('active', '#364544')],
              background=[('disabled', 'magenta'),
                          ('pressed', '!focus', 'cyan'),
                          ('active', 'green')],
              highlightcolor=[('focus', 'green'),
                              ('!focus', '#8AB5B5')],
              relief=[('pressed', 'groove'),
                      ('!pressed', 'ridge')])

        ttk.Button(self, text="Регистрация", style = "Wild.TButton", command=self.new_user).pack(side=BOTTOM, fill=X)
        ttk.Button(self, text="Войти", style = "Wild.TButton", command=self.log_user).pack(side=BOTTOM, fill=X)
        self.protocol("WM_DELETE_WINDOW", lambda: exit())


    @staticmethod
    def exit():
        raise SystemExit

    def registration(name, passwd):
        with open("logs_users.txt", 'a', encoding='utf-8') as s:
            s.write(name+';'+passwd+'\n')

    def login(name, passwd):
        users = Registation.open_log_file()
        if users:
            for n in users:
                if n[0] == name and n[1] == passwd:
                    return True
            return False
        return False

    def folder_exist(name, path):
        if name in os.listdir(path):
            return True
        return False
    @staticmethod
    def clear_text(log, passwd):
        log.set('')
        passwd.set('')


    def show_error_login(self):
        messagebox.showerror('Warning', "Wrong login or password")

    def show_error(self):
        messagebox.showerror('Warning', "This user already exists")

    def show_empty_error(self):
        messagebox.showerror('Warning', "No username or password")
    def log_user(self):
        name = self.login.get()
        passwd = self.passw.get()
        self.welcome.set(f'Добро пожаловать, {name}')
        Registation.clear_text(self.login, self.passw)
        new_usrd = Registation.login(name, passwd)
        if new_usrd:
            folder_ = Registation.folder_exist(name, self.path)
            if folder_:
                pass
            else:
                Folder(name, self.path, len(os.listdir(self.path)), self.delimiter).createdir()
            Registation.main_dirr = self.path + self.delimiter + name
            Registation.main_user_flag = True
            self.destroy()
        else:
            self.show_error_login()

    def new_user(self):
        name = self.login.get()
        passwd = self.passw.get()

        Registation.clear_text(self.login, self.passw)
        if len(name) != 0 and len(passwd) != 0:
            self.welcome.set(f'Добро пожаловать, {name}')
            users = Registation.open_log_file()
            if users:
                for n in users:
                    if n[0] == name:
                        self.show_error()
                        break
                else:
                    self.end_func(name, passwd)
            else:
                self.end_func(name, passwd)
        else:
            self.show_empty_error()

    @staticmethod
    def open_log_file():
        try:
            with open("logs_users.txt", 'r', encoding='utf-8') as file:
                users = [split(r'[;]', i) for i in split(r'\n', file.read())[:-1]]
                return users
        except:
            file = open('logs_users.txt', 'w', encoding='utf-8')
            file.close()
            return False

    def end_func(self, log, passw):
        Registation.registration(log, passw)
        Folder(log, self.path, len(os.listdir(self.path)), self.delimiter).createdir()
        Registation.main_dirr = self.path + self.delimiter + log
        Registation.main_user_flag = True
        self.destroy()

# def main():
#     delimiter = re.search(r'[\\/]', global_folder).group(0)
#     print(delimiter)
#     a = Registation(global_folder, delimiter)
#     a.mainloop()
#
# if __name__ == '__main__':
#     main()