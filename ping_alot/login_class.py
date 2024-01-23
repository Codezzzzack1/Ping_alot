from codezzz_tk_class import NewWin, MyDict
import csv
from csv import DictReader
import datetime as dTime
import inspect, os, shutil
import sys
import threading 
import time
from tkinter import *
from tkinter import messagebox, filedialog, ttk
import tkinter.font as font
import customtkinter
from customtkinter import *
import sys
import math

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class LoginScreen():

    # initialize photos
    def __init__(self, login_window, next_window_function):

        self.next_win = next_window_function
        self.log_win = login_window
        self.log_btn_path_static = 'img/start_stop_120/chrome.png'
        self.btn_path_press = 'img/start_stop_120/pressed.png'
        self.btn_path_hover = 'img/start_stop_120/hover.png'
        self.reg_btn_path_static = 'img/start_stop_120/purple.png'
        self.user_perm = ''
        self.user_first = ''
        self.user_last = ''
        self.username = ''
        self.user_pass = ''
        self.app_reg = None


        # Build Window
        self.app = NewWin('Login', 400, 400, 'img/temp_bg_0.png', 'img/temp_bg_1.png', 'img/min_btn3.png', 'img/min_btn2.png', 'img/logo.ico')

        self.entry_width = self.app.pic_width * .045
        self.app.root.bind("<Return>", lambda event: self.user_login())

        self.user = StringVar()
        self.user.set('Enter User Name')
        self.user_enter = Entry(self.app.root, font=('Imprint MT Shadow', 16), fg=self.app.txt_fill, bg='black', relief='sunken', bd=2,
                                 width=int(self.entry_width), textvariable=self.user, justify='center')
        self.user_enter.bind("<FocusIn>", lambda e: e.widget.select_range(0, 'end'))
        self.user_enter.place(x=15, y=240)

        self.pword = StringVar()
        self.pword.set('Password')
        self.pword_enter = Entry(self.app.root, font=('Imprint MT Shadow', 16), fg=self.app.txt_fill, bg='black', relief='sunken', bd=2,
                                 width=int(self.entry_width), textvariable=self.pword, justify='center', show='*')
        self.pword_enter.bind("<FocusIn>", lambda e: e.widget.select_range(0, 'end'))
        self.pword_enter.place(x=15, y=290)

        self.header = self.app.text(115, 220, text='Login', font=('Imprint MT Shadow', 20), justify='center', fill=self.app.txt_fill)

        self.log_btn = self.app.create_button(115, 360, self.log_btn_path_static, self.btn_path_press, 
                                              self.btn_path_hover, 75, 120, command=self.user_login)
        
        self.reg_btn = self.app.create_button(330, 170, self.reg_btn_path_static, self.btn_path_press, 
                                              self.btn_path_hover, 75, 120, command=self.command_reg)

    # Define function to run button caommand    
    def command_reg(self):
        self.app.exit_app()
        time.sleep(.5)
        self.reg_win()

    # Functionality of logging in
    def user_login(self):

        self.user_perm = ''
        self.user_first = ''
        self.user_last = ''
        self.username = ''
        self.user_pass = ''


        user = str(self.user.get())
        pword = str(self.pword.get())
        
        cc = 0
        coded = []
        dir = 'users'
        path = 'users/users.csv'
        dir_exist = os.path.exists(path)
        
        for p in pword:
            code = ord(p)
            coded.append(code)
        for c in coded:
            cc += c
        new_code = str(cc)
        
        zaeggers = 'zaeggers'
        my_pass = 'z23e45'
            
        try:
            if user == zaeggers and pword == my_pass:
                self.user_first = 'Zack'
                self.user_last = 'Eggers'
                self.username = 'zaeggers'
                self.user_perm = 'engineer'
                self.app.exit_app()
                time.sleep(.5)
                self.next_win()
                
            else:
                if dir_exist:
                    with open(path, 'r') as user_csv:
                        csv_reader = DictReader(user_csv)
                
                        for row in csv_reader:
                            user_csv = row['username']
                            pword_csv = row['password']
                            if user != 'Enter User Name':
                                new_user = user.replace(' ', '')
                                if new_code != 'Password' or new_code != '':
                                    if user_csv.casefold() == new_user.casefold() and pword_csv == new_code:
                                        self.user_first = row['firstname']
                                        self.user_last = row['lastname']
                                        self.username = row['username']
                                        self.user_perm = row['usertype'] 
                                        self.user_pass = row['password']
                                        break
                        if self.user_perm == 'admin' or self.user_perm == 'user' or self.user_perm == 'engineer':
                            self.app.exit_app()
                            time.sleep(.5)
                            self.next_win()
                        else:
                            msg_30 = messagebox.showwarning('NO ACCESS', 'CHECK USERNAME AND PASSWORD OR REGISTER')
                else:
                    msg_dir = messagebox.showwarning('NO DATABASE', 'NO DATABASE EXIST YOU NEED TO REGISTER!')

        except Exception as e:
            if self.app.exited_app:
                pass
            else:
                print(str(e))

    # Function for starting registry Window
    def reg_win(self):
        #instance of new class
        self.app_reg

        dir = 'users'
        dir_exist = os.path.exists(dir)
        path = 'users/users.csv'
        path_exist = os.path.exists(path)
        user_list = ['firstname', 'lastname', 'username', 'password', 'usertype']
        fieldnames = user_list

        if not dir_exist:
            os.makedirs(dir)
            if not path_exist:
                with open(path, 'w', newline='') as user_csv:
                        csv_writer = csv.DictWriter(user_csv, fieldnames=fieldnames)

                        csv_writer.writeheader()

        self.app_reg = RegistryScreen(self.log_win, self.register_user)

        root = self.app_reg.app
        root.root.update()
        root.root.mainloop()     

    # Functionality for the registration
    def register_user(self):

        user_get = str(self.app_reg.user.get())
        first_get = str(self.app_reg.firstname.get())
        last_get = str(self.app_reg.lastname.get())
        pword_get = str(self.app_reg.pword.get())
        c_pword_get = str(self.app_reg.c_pword.get())
        rights_get = str(self.app_reg.rights.get())

        current_rights = ''
        user_list = ['firstname', 'lastname', 'username', 'password', 'usertype']
        user_dict = MyDict()
        for user in user_list:
            user_dict.add(user, '')
        fieldnames = user_list
        cc = 0
        path = 'Users/Users.csv'
        path_exist = os.path.exists(path)
        coded = []
        
        try:
            if path_exist:
                if current_rights != 'user':
                    if first_get != '' or first_get != 'Enter First Name': 
                        if last_get != '' or last_get != 'Enter Last Name':
                            if user_get != '' or user_get != 'Enter User Name':
                                new_user = user_get.replace(' ', '')
                                if pword_get != '':
                                    if rights_get == 'engineer' or rights_get == 'admin' or rights_get == 'user':
                                        if self.password_check(pword_get):
                                            if c_pword_get != 'Password' or c_pword_get != '':
                                                if pword_get == c_pword_get:                           
                                                    for i in pword_get:
                                                        code = ord(i)
                                                        coded.append(code)
                                                        print(coded)
                                                    for c in coded:
                                                        cc += c
                                                    new_code = str(cc)                                                
        
                                                    with open(path, 'a', newline='') as user_csv:
                                                        csv_writer = csv.DictWriter(user_csv, fieldnames=fieldnames)
                                                        user_dict['firstname'] = first_get
                                                        user_dict['lastname'] = last_get
                                                        user_dict['username'] = new_user
                                                        user_dict['password'] = new_code
                                                        user_dict['usertype'] = rights_get
            
                                                        csv_writer.writerow(user_dict)
                                                        print(user_dict)
                                                    self.app_reg.app.exit_app()
                                                    time.sleep(.5)                                        
                                                    self.log_win()
                                                else:
                                                    msg_33 = messagebox.showwarning('PASSWORD', 'PASSWORDS DO NOT MATCH!!')  
                                            else:
                                                msg_34 = messagebox.showwarning('PASSWORD', 'PLEASE CONFIRM PASSWORD!!')
                                            
                                        else:
                                            msg_35 = messagebox.showwarning('PASSWORD', 'PASSWORD MUST CONTAIN AT LEAST 8 CHARACTERS\n'
                                                                            'ONE CAPITAL AND ONE LOWER CASE\nONE NUMBER AND ONE SPECIAL CHARACTER')
                                    else:
                                        msg_38 = messagebox.showwarning('USERTYPE', 'PLEASE ENTER USERTYPE!!\n OR PRESS ESC TO EXIT!')                                       
                                else:
                                    msg_36 = messagebox.showwarning('PASSWORD', 'PLEASE ENTER AND CONFIRM PASSWORD!!\n OR PRESS ESC TO EXIT!') 
                            else:
                                msg_37 = messagebox.showwarning('USER NAME', ' PLEASE ENTER A USERNAME!!\n OR PRESS ESC TO EXIT!') 
                        else:
                            msg_37 = messagebox.showwarning('LAST NAME', ' PLEASE ENTER YOUR LAST NAME!!\n OR PRESS ESC TO EXIT!') 
                    else:
                        msg_37 = messagebox.showwarning('USER NAME', ' PLEASE ENTER YOUR FIRST NAME!!\n OR PRESS ESC TO EXIT!')
                else:
                    msg_39 = messagebox.showwarning('REGISTRATION ERROR', 'MUST BE LOGGED OUT TO REGISTER!!')
                    self.app_reg.app.exit_app()
                    time.sleep(.5)                                        
                    self.log_win()
            else:
                msg_40 = messagebox.askyesno('REGISTRATION ERROR', 'PATH TO USERS.CSV DOES NOT EXIST?\nWOULD YOU LIKE TO TRY AGAIN?')
                if msg_40:
                    pass
                else:
                    self.app_reg.app.exit_app()
                    time.sleep(.5)                                        
                    self.log_win()

        except Exception as e:
            if self.app_reg.app.exited_app:
                pass
            else:
                print(str(e)) 

    # Function to validate the password
    def password_check(self, passwd):
        
        special_symbol =['$', '@', '#', '%', '!', '&', '*', '+', '?']
        val = True
        
        if len(passwd) < 8:
            print('length should be at least 6')
            val = False
            
        if len(passwd) > 20:
            print('length should be not be greater than 8')
            val = False
            
        if not any(char.isdigit() for char in passwd):
            print('Password should have at least one numeral')
            val = False
            
        if not any(char.isupper() for char in passwd):
            print('Password should have at least one uppercase letter')
            val = False
            
        if not any(char.islower() for char in passwd):
            print('Password should have at least one lowercase letter')
            val = False
            
        if not any(char in special_symbol for char in passwd):
            print('Password should have at least one of the symbols $@#')
            val = False
        if val:
            return val
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class RegistryScreen():

    # initialize photos
    def __init__(self, log_btn_command, reg_btn_command):

        self.log_btn_command = log_btn_command
        self.reg_btn_command = reg_btn_command
        self.log_btn_path_static = 'img/start_stop_120/chrome.png'
        self.btn_path_press = 'img/start_stop_120/pressed.png'
        self.btn_path_hover = 'img/start_stop_120/hover.png'
        self.reg_btn_path_static = 'img/start_stop_120/purple.png'


        # Build Window
        self.app = NewWin('Registry', 400, 400, 'img/temp_bg_0.png', 'img/temp_bg_1.png', 'img/min_btn3.png', 'img/min_btn2.png', 'img/logo.ico')

        self.entry_width = self.app.pic_width * .04
        self.app.root.bind("<Return>", lambda event: self.command_reg())

        self.firstname = StringVar()
        self.firstname.set('Enter First Name')
        self.first_enter = Entry(self.app.root, font=('Imprint MT Shadow', 16), fg=self.app.txt_fill, bg='black', relief='sunken', bd=2,
                                 width=int(self.entry_width), textvariable=self.firstname, justify='center')
        self.first_enter.bind("<FocusIn>", lambda e: e.widget.select_range(0, 'end'))
        self.first_enter.place(x=10, y=190)

        self.lastname = StringVar()
        self.lastname.set('Enter Last Name')
        self.last_enter = Entry(self.app.root, font=('Imprint MT Shadow', 16), fg=self.app.txt_fill, bg='black', relief='sunken', bd=2,
                                 width=int(self.entry_width), textvariable=self.lastname, justify='center')
        self.last_enter.bind("<FocusIn>", lambda e: e.widget.select_range(0, 'end'))
        self.last_enter.place(x=10, y=250)
        
        self.rights = StringVar()
        self.rights.set('Enter Permissions')
        self.rights_enter = Entry(self.app.root, font=('Imprint MT Shadow', 16), fg=self.app.txt_fill, bg='black', relief='sunken', bd=2,
                                 width=int(self.entry_width), textvariable=self.rights, justify='center')
        self.rights_enter.bind("<FocusIn>", lambda e: e.widget.select_range(0, 'end'))
        self.rights_enter.place(x=10, y=310)

        self.user = StringVar()
        self.user.set('Enter User Name')
        self.user_enter = Entry(self.app.root, font=('Imprint MT Shadow', 16), fg=self.app.txt_fill, bg='black', relief='sunken', bd=2,
                                 width=int(self.entry_width), textvariable=self.user, justify='center')
        self.user_enter.bind("<FocusIn>", lambda e: e.widget.select_range(0, 'end'))
        self.user_enter.place(x=205, y=190)

        self.pword = StringVar()
        self.pword.set('Password')
        self.pword_enter = Entry(self.app.root, font=('Imprint MT Shadow', 16), fg=self.app.txt_fill, bg='black', relief='sunken', bd=2,
                                 width=int(self.entry_width), textvariable=self.pword, justify='center', show='*')
        self.pword_enter.bind("<FocusIn>", lambda e: e.widget.select_range(0, 'end'))
        self.pword_enter.place(x=205, y=250)

        self.c_pword = StringVar()
        self.c_pword.set('Password')
        self.c_pword_enter = Entry(self.app.root, font=('Imprint MT Shadow', 16), fg=self.app.txt_fill, bg='black', relief='sunken', bd=2,
                                 width=int(self.entry_width), textvariable=self.c_pword, justify='center', show='*')
        self.c_pword_enter.bind("<FocusIn>", lambda e: e.widget.select_range(0, 'end'))
        self.c_pword_enter.place(x=205, y=310)

        self.header = self.app.text(193, 170, text='Register', font=('Imprint MT Shadow', 20), justify='center', fill=self.app.txt_fill)

        self.reg_btn = self.app.create_button(115, 370, self.reg_btn_path_static, self.btn_path_press, 
                                              self.btn_path_hover, 75, 120, command=self.command_reg)
        
        self.log_btn = self.app.create_button(330, 150, self.log_btn_path_static, self.btn_path_press, 
                                              self.btn_path_hover, 75, 120, command=self.command_log)

    # Define function to run button caommand    
    def command_log(self):

        self.app.exit_app()
        time.sleep(.5)
        if self.log_btn_command is not None:
            self.log_btn_command()

    # Define function to run button caommand    
    def command_reg(self):
       
        if self.reg_btn_command is not None:
            self.reg_btn_command()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# EXAMPLE #######################################################################################
def log_win():
    #instance of new class
    global app_log
    app_log = LoginScreen(log_win, new_win)

    

    root = app_log.app
    root.root.update()
    root.root.mainloop()

def new_win():

    app_new_win = NewWin('New window',600,600,'img/bg_ping_0.png','img/bg_ping_0.png','img/min_btn3.png','img/min_btn2.png','img/logo.ico')

    root = app_new_win.root

    root.update()
    root.mainloop()

###################################################################################################

if __name__=='__main__':
    log_win()
