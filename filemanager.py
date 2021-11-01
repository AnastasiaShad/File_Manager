import shutil
import os
from tkinter import *
from tkinter.font import Font
from config import global_folder
from tkinter import messagebox
import re
from functools import partial
import fileinput
from zipfile import ZipFile
from registration import Registation

class FileManager:
    def __init__(self, current_directory):
        self.main_path = [current_directory]
        self.experts = 0
        self.current_directory = [current_directory]
        self.chng = ''
        self.commands = {
            "makedir": self.make_dir,
            "removedir": self.rem_dir,
            "changedir": self.change_dir,
            "makefile": self.make_file,
            "addtext": self.add_text,
            "showtext": self.show_text,
            "removefile": self.rem_file,
            "copyfile": self.copy_file,
            "movefile": self.move_file,
            "changename": self.change_fie,
            "zip": self.zip,
            "unzip": self.unzip,
            "help":self.help
        }

        # Дисплей
        self.window = Tk()
        self.curr_dir_now = Frame(self.window)
        self.top_text = Frame(self.window)
        self.top_frame = Frame(self.window)
        self.bottom_frame = Frame(self.window)
        self.curr_dir = Label(self.curr_dir_now, text = "Текущая директория: ")
        self.file_list = Listbox(self.top_frame, width=90, height=20)

        self.text = StringVar()
        self.path = self.current_directory[0]
        self.text.set(self.path)
        self.label = Label(self.top_text, width=30, height=2, textvariable=self.text)

        # консоль команд
        self.console = Entry(self.bottom_frame, width=90, bd = 7)



        self.settings_window()


    def settings_window(self):
        self.window.title("File manager")
        self.window.bind('<Return>', self.now_command)
        self.curr_dir_now.configure(bg="#8AB5B5")
        self.curr_dir_now.pack(fill=BOTH)
        self.curr_dir.pack(side=LEFT, padx=15)
        self.curr_dir.configure(font=Font(size=13, weight="bold"),bg="#8AB5B5", fg="#FFFFFF")
        self.top_frame.configure(bg="#8AB5B4")
        self.bottom_frame.configure(bg="#8AB5B4")
        self.top_text.configure(bg="#8AB5B4")
        self.top_text.pack(fill=BOTH)
        self.top_frame.pack(fill=BOTH)
        self.bottom_frame.pack(fill=BOTH)

        self.label.pack(side=LEFT, padx=10)
        self.label.configure(font=Font(size=10, weight="bold"), bg="#359492", fg="#FFFFFF")

        self.file_list.pack(side=LEFT, padx=10, pady=10)
        self.file_list.configure(font=Font(size=9, weight="bold"), bg="#364544", fg="#F3F5D9",
                                 selectbackground="#F3F5D9", selectforeground="#364544")

        self.console.pack(side=TOP, padx=10, pady=2)
        self.console.configure(font=Font(size=9, weight="bold"), bg="#5B7574", fg="#FFFFFF")

        self.all_dir_content()
        self.current_path()

        self.window.mainloop()

    def all_dir_content(self):
        self.file_list.delete(0, END)
        if self.chng == '':

            for file in os.listdir(self.current_directory[0]):
                self.file_list.insert(END, file)
        else:
            self.current_directory = self.chng[1]

            for file in os.listdir(self.chng[0]):
                self.file_list.insert(END, file)




    def show_error(self):
        messagebox.showerror('Warning', "Too much arg")


    def current_path(self):
        if self.chng == '':
            self.text.set(self.current_directory[0])
        else:
            if self.experts == 1:
                self.experts = 0
            else:
                self.current_directory = self.chng[1]
                self.text.set(self.chng[0])


    def show_file_text(self, content):
        self.file_content.delete(0, END)
        for line in content:
            self.file_content.insert(END, line)

    def now_command(self, event):
        line = self.console.get().split(" ")
        self.console.delete(0, END)
        # if len(line) == 1:
        #     messagebox.showerror('Warning', "Empty field")
        if len(line) > 0:
            command, arguments = line[0], line[1:]
            if command in self.commands.keys():
                self.commands[command](*arguments)
            else:
                messagebox.showerror('Warning', "This command does not exist")
            self.current_path()



    def read_path(self, path, mode=True):

        path = [item for el in path.split('\\') for item in el.split('/')]

        if path[0] == '.':
            path = list(self.current_directory + path[1:])

        elif path[0] == '..':
            if len(self.current_directory) > 1:
                path = list(self.current_directory[:-1] + path[1:])

            else:
                path = list(self.current_directory + path[1:])
        elif path[0] == '':
            path[0] = self.main_path[0]
        else:

            path = list(self.current_directory + path)

        secondary = '/' + '/'.join(path[1:]) if mode else path
        # print("path3", os.path.join(*path))
        # print(os.path.join(*path))
        return os.path.join(*path), secondary

# Команды

    def make_dir(self, names):

            dir_name = self.read_path(names)
            try:
                os.mkdir(dir_name[0])
                self.all_dir_content()
            except Exception:
                self.show_error()



    def rem_dir(self, *names):
        if len(names) < 2:
            for name in names:
                dir_name = self.read_path(name)
                try:
                    os.rmdir(dir_name[0])
                    self.all_dir_content()
                except FileNotFoundError:
                    messagebox.showerror("Warning", f'The folder does not exist {dir_name[1]}')
                except OSError:
                    messagebox.showerror("Warning", f'Current folder is not empty {dir_name[1]}. Delete all files')
        else:
            self.show_error()
# РАБОТАЕТ
    def change_dir(self, name):

        try:
                chng = self.read_path(name, mode = False)
                self.chng = chng
                if self.chng[1][0] == self.main_path[0]:
                    os.chdir(self.chng[0])
                    # self.current_directory = chng[0]
                    self.all_dir_content()

                else:
                    self.show_error()
        except:
            self.experts = 1
            messagebox.showerror("Warning", f'The folder does not exist {self.chng[0]}')

    def make_file(self, *names):
        try:
            for name in names:
                if ".txt" not in name:
                    name += ".txt"
                file_name = self.read_path(name)

                open(file_name[0], 'x').close()
                self.all_dir_content()
        except Exception:
            pass

    def add_text_menu(self,file):
        self.wind =  Tk()
        item = file
        self.wind.title(f'File editor {item}')
        global add_file
        add_file = Text(self.wind, bg="#364544", fg="#FFFFFF")
        add_file.pack(side=TOP)
        Button(self.wind, text="Cохранить",  background="#359492", foreground="#FFFFFF", command=partial(
            self.save, item, self.wind)).pack(fill=X)
        add_file.insert(INSERT, ''.join(self.show(item)))
        self.window.mainloop()
    def add_text(self, *names):
        if len(names) < 2:
                for name in names:
                    if ".txt" not in name:
                        name += ".txt"
                    try:
                        self.file_name = self.read_path(name)
                        if os.path.exists(self.file_name[0]):
                            self.add_text_menu(self.file_name[0])
                        else:
                            messagebox.showerror("Warning", f'The file does not exist {self.file_name[0]}')
                    except FileNotFoundError:
                        messagebox.showerror("Warning", f'The file does not exist {self.file_name[0]}')
                        pass
        else:
            self.show_error()

    def save(self, it, win):
        new_text = add_file.get(1.0, END)
        with open(self.file_name[0], 'w') as s:
            s.write(new_text)
        win.destroy()

    def show(self, it):
        add_file = []
        for i in fileinput.input(self.file_name[0]):
            add_file.append(i)
        return add_file

    def show_text(self, *names):
        if len(names) < 2:
            for name in names:
                if ".txt" not in name:
                    name += ".txt"
                self.file_name = self.read_path(name)
                if os.path.exists(self.file_name[0]):
                        self.show_text_menu(self.file_name[0])
                else:
                    messagebox.showerror("Warning", f'The file does not exist {self.file_name[1]}')
        else:
            self.show_error()

    def show_text_menu(self, file):
        self.wind = Tk()
        item = file
        self.wind.title(f'File text {item}')
        global show_text_just
        show_text_just = Listbox(self.wind, bg="#364544", fg="#FFFFFF", width=70, height=30)
        show_text_just.pack(side=TOP)
        with open(item, 'r') as file:
            for line in file:
                show_text_just.insert(END, line)
        self.wind.mainloop()
    def rem_file(self, *names):
        for name in names:
            if ".txt" not in name:
                name += ".txt"
            self.rem_files = self.read_path(name)
            try:
                os.remove(self.rem_files[0])
                self.all_dir_content()
            except FileNotFoundError:
                messagebox.showerror("Warning", f'The file does not exist {self.rem_files[1]}')

    def copy_file(self, *names):
        file_names = names[:-1]
        dir_path = names[-1]
        to_dir = self.read_path(dir_path)
        try:
            for name in file_names:
                if ".txt" not in name:
                    name += ".txt"
                self.file_n = self.read_path(name)
                shutil.copy(self.file_n[0], to_dir[0])
            self.all_dir_content()
        except Exception:
            messagebox.showerror("Warning", f'wrong')
    def move_file(self, *names):
        file_names = names[:-1]
        dir_path = names[-1]
        to_dir = self.read_path(dir_path)
        try:
            for name in file_names:
                if ".txt" not in name:
                    name += ".txt"
                self.file_n = self.read_path(name)

                shutil.move(self.file_n[0], to_dir[0])
            self.all_dir_content()
        except Exception:
            messagebox.showerror("Warning", f'wrong')
    def change_fie(self, *names):
        if len(names) == 2:
            old_name = names[0]
            if ".txt" not in  old_name:
                old_name += ".txt"
            new_name = names[1]
            if ".txt" not in  new_name:
                new_name += ".txt"
            self.old = self.read_path(old_name)
            self.new = self.read_path(new_name)
            os.rename(self.old[0], self.new[0])
            self.all_dir_content()
        else:
            self.show_error()

    def zip(self, *names):
        try:
            with ZipFile(names[0].split(".")[0] + ".zip", "w") as zip_file:
                for file_name in names:
                    if len(self.current_directory) == 1:
                        print(self.current_directory)
                        zip_file.write(file_name, self.current_directory[0])
                    # arg = self.read_path(file_name)
                    # print(arg[0])
                    else:
                        zip_file.write(file_name)
                self.all_dir_content()
        except Exception as e:
            self.show_error()

    def unzip(self, *names):
        try:
            with ZipFile(names[0]) as zip_file:
                self.make_dir(names[0].replace(".zip", ""))
                zip_file.extractall(names[0].replace(".zip", ""))
                self.all_dir_content()
        except Exception as e:
            self.show_error()
    def help(self):
        help_comm = '''
'makedir [folder]' ---- make folders
'removedir [folder]' ---- remove folders
'changedir [folder]' ---- changes current folder
'changedir " " ' ---- change to main folder
'changedir ..' ---- change to the previous folder
'makefile [file1] [file2]' ---- create files
'addtext [file]' ---- write to file, stream string input
'showtext [file]' ---- displays files
'removefile [file1] [file2]' ---- remove files
'copyfile [files] [folder_name_to]' ---- copy file_name to folder
'movefile [files] [folder_name_to]' ---- replace file to other folder
'changename [old name] [new name]' ---- rename file
'help' -- command list'''
        messagebox.showinfo('Commands', help_comm)

def regist_use():
    delimetr = re.search(r'[\\/]', global_folder).group(0)
    reg_m = Registation(global_folder, delimetr)
    reg_m.mainloop()

def main():
    regist_use()
    while not Registation.main_user_flag:
        pass
    main_path = Registation.main_dirr
    FileManager(main_path)

if __name__ == '__main__':
    main()