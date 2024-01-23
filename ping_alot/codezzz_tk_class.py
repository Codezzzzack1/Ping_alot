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

#                                                               Classes for import
#####################################################################################################################################################################################
#####################################################################################################################################################################################

#                                                               Class for Window Base
#####################################################################################################################################################################################

# Class for my base window templates
class NewWin():
    # setting class variables
    root = None
    pic_width = 0
    pic_height = 0
    bg_img_path_0 = None
    bg_img_path_1 = None
    bg_img_path_2 = None
    bg_img_path_3 = None
    bg_img_0 = None
    bg_img_1 = None
    bg_img_2 = None
    bg_img_3 = None
    bg_color = None
    __zero = 0
    font = None
    user = None
    txt_fill = None
    txt_pos_x = None
    txt_pos_y = None
    exited_app = False
    width = 0
    height = 0
    icon = None
    bg_canvas = None
    bg_image_0 = None
    bg_image_1 = None
    image_min = None
    image_exit = None
    date_txt = None
    user_txt = None
    center_x = None
    center_y = None
    dtN = None
    dNow = None
    tNow = None
    nDate = None
    newDate = None
    new_time = None
    nTime = None
    nMonth = None
    nDay = None
    nMinute = None
    nSecond = None
    nMonthYear = None
    user_msg = None
    button = None
    image = None
    text = None
    stop = threading.Event()

    # initialize needed parameters
    def __init__(self, title: str, pic_x: int, pic_y: int, pic_path_1: str, pic_path_2: str,
                  exit_btn_path: str, min_btn_path: str, logo_path: str):
        """title= 'max 10 characters', pic_x= background picture width, pic_y= background picture height, 
        pic_path_1= 1st background .png picture directory path, pic_path_2= 2nd background .png picture directory path, 
        exit_btn_path= your exit button .png picture directory path, min_btn_path= your minimizing button .png picture directory path,
         logo_path= your app .ico picture directory path """


        #Build a tkinter window
        self.title = title
        self.pic_width = pic_x
        self.pic_height = pic_y
        self.width = self.pic_width + 30
        self.height = self.pic_height + 30
        self.center_x = int((1920 - self.width) / 2)
        self.center_y = int((1080 - self.height) / 2)
        self.path_0 = pic_path_1
        self.path_1 = pic_path_2
        self.path_2 = exit_btn_path
        self.path_3 = min_btn_path
        self.bg_img_path_0 = (self.path_0, self.pic_width, self.pic_height)
        self.bg_img_path_1 = (self.path_1, self.pic_width, self.pic_height)
        self.bg_img_path_2 = (self.path_3, 25, 25)
        self.bg_img_path_3 = (self.path_2, 25, 25)
        self.icon = logo_path
        self.bg_color = 'black'
        self.title_pos = self.pic_width / 2

        self.root = Tk()
        self.root.title(self.title)
        self.root.geometry(f'{self.width}x{self.height}+{self.center_x}+{self.center_y}')
        self.root.config(relief='ridge', bd=15, bg=self.bg_color)
        
        self.root.iconbitmap(self.icon)
        self.root.bind("<Button-3>", lambda event: self.exit_msg())
        self.root.bind("<Map>", self.max_win)
        
        self.bg_img_0 = PhotoImage(file=self.bg_img_path_0[0], width=self.bg_img_path_0[1], height=self.bg_img_path_0[2])
        self.bg_img_1 = PhotoImage(file=self.bg_img_path_1[0], width=self.bg_img_path_1[1], height=self.bg_img_path_1[2])
        self.bg_img_2 = PhotoImage(file=self.bg_img_path_2[0], width=self.bg_img_path_2[1], height=self.bg_img_path_2[2])
        self.bg_img_3 = PhotoImage(file=self.bg_img_path_3[0], width=self.bg_img_path_3[1], height=self.bg_img_path_3[2])

        self.__zero = 0
        self.font = ('Imprint MT Shadow', 16)
        self.title_font = ('Imprint MT Shadow', 25)
        self.user_font = ('Imprint MT Shadow', 10)
        self.user = os.getenv('username')
        self.txt_fill = "#C2AD2D"
        self.txt_pos_x = self.pic_width - 70
        self.txt_pos_y = 45 
        self.exited_app = False
        

        #Build the background to the window
        self.bg_canvas = Canvas(self.root, width=self.width, height=self.height, bg=self.bg_color)
        self.bg_canvas.pack(fill=BOTH)

        # to add images
        self.image = self.bg_canvas.create_image

        #adding images to bg
        self.bg_image_0 = self.bg_canvas.create_image(self.__zero,self.__zero, image=self.bg_img_0, anchor=NW)
        self.bg_image_1 = self.bg_canvas.create_image(self.pic_width,self.__zero, image=self.bg_img_1, anchor=NW)

        #image that also minimizes window
        self.image_min = self.bg_canvas.create_image(55,20, image=self.bg_img_2, anchor=CENTER)
        self.bg_canvas.tag_bind(self.image_min, sequence="<Button-1>", func=lambda event: self.min_win())
        
        #image that also exits app
        self.image_exit = self.bg_canvas.create_image(20,20, image=self.bg_img_3, anchor=CENTER)
        self.bg_canvas.tag_bind(self.image_exit, sequence="<Button-1>", func=lambda event: self.exit_app())

        # text that shows the date
        self.date_txt = self.bg_canvas.create_text(self.txt_pos_x, self.txt_pos_y, fill=self.txt_fill, font=self.font, justify=CENTER)
        self.title_txt = self.bg_canvas.create_text(self.txt_pos_x, 85, fill=self.txt_fill, font=self.font, justify=CENTER, text=f'{self.title}')

        # text that shows the user
        self.user_txt = self.bg_canvas.create_text(self.txt_pos_x, 15, fill=self.txt_fill, font=self.user_font, justify=CENTER, text=f'{self.user} is Online')
        self.bg_canvas.tag_bind(self.user_txt, sequence="<Button-1>", func=lambda event: self.user_message())
        self.hover_config(self.user_txt, '#2E14AD', self.txt_fill)
        
        # Use for creating texts
        self.text = self.bg_canvas.create_text

        # to start functions and animation
        self.strt_date_update()
        self.strt_bg_update()

    # define creating button
    def create_button(self, x: int, y: int, image_static_path: str, image_pressed_path: str, image_hover_path: str, image_height: int, image_width: int, command=None):
        img_static = PhotoImage(file=image_static_path, width=image_width, height=image_height)
        img_pressed = PhotoImage(file=image_pressed_path, width=image_width, height=image_height)
        img_hover = PhotoImage(file=image_hover_path, width=image_width, height=image_height)

        self.button = self.bg_canvas.create_image(x, y, image=img_static, anchor=CENTER)
        self.btn_config(self.button, img_static, img_pressed, img_hover, command)

    # Define configuring button binds
    #----------------------------------------------------------------------------------------------------------
    def btn_config(self, btn, img, img_press, img_hover, command=None):
        if img['width'] == img_press['width'] and img['width'] == img_hover['width']:
            if img['height'] == img_press['height'] and img['height'] == img_hover['height']:
                self.bg_canvas.tag_bind(btn, sequence="<ButtonPress-1>", func=lambda event: self.on_press(btn, img_press))
                self.bg_canvas.tag_bind(btn, sequence="<ButtonRelease-1>", func=lambda event: self.on_release(btn, img, command))
                self.bg_canvas.tag_bind(btn, sequence="<Enter>", func=lambda event: self.on_enter(btn, img_hover))
                self.bg_canvas.tag_bind(btn, sequence="<Leave>", func=lambda event: self.on_leave(btn, img))
            else:
                raise Exception('ALL IMAGE SIZES MUST BE THE SAME!!')
        else:
            raise Exception('ALL IMAGE SIZES MUST BE THE SAME!!')

    # function for pressing buttons
    #-----------------------------------------------------------------------------------------------------------
    def on_press(self, btn, img1):
        self.bg_canvas.itemconfigure(btn, image=img1)

    def on_release(self, btn, img,  command):
        self.bg_canvas.itemconfigure(btn, image=img)
        if command is not None:
            command()

    def on_enter(self, btn, img2):
        self.bg_canvas.itemconfigure(btn, image=img2)

    def on_leave(self, btn, img):
        self.bg_canvas.itemconfigure(btn, image=img)

#----------------------------------------------------------------------------------------------------------------   

# fuctions for hover color change
#----------------------------------------------------------------------------------------------------------------   
    # Define hover configs
    def hover_config(self, tag, color_hover, color_static):
        self.bg_canvas.tag_bind(tag, sequence="<Enter>", func=lambda event: self.color_change(tag, color_hover))
        self.bg_canvas.tag_bind(tag, sequence="<Leave>", func=lambda event: self.color_resume(tag, color_static))

    # Define color change on hover
    def color_change(self, tag, color):
        self.bg_canvas.itemconfigure(tag, fill=color)

    # Define color change on hover
    def color_resume(self, tag, color):
        self.bg_canvas.itemconfigure(tag, fill=color)

#----------------------------------------------------------------------------------------------------------------

    #Defining date thread
    def strt_date_update(self):
        self.date_thread = threading.Thread(target=self.date_update)
        self.date_thread.daemon = True
        self.date_thread.start()

    #Defining background thread
    def strt_bg_update(self):
        self.bg_thread = threading.Thread(target=self.pic_animate)
        self.bg_thread.daemon = True
        self.bg_thread.start()

    # Define updating values
    def date_update(self):
        try:
            while not self.exited_app:
                self.date_time()
                new_date = self.nDate
                new_time = self.nTime

                self.bg_canvas.itemconfig(self.date_txt, text=f'{new_date}\n{new_time}')

                time.sleep(.1)
            else:
                pass
        except Exception as e:
            if not self.exited_app:
                print(e)
                self.root.after(1001, self.strt_bg_update)
            else:
                pass


    # Define picture animation
    def pic_animate(self):

        while not self.exited_app:

            time.sleep(20)
            hop = self.pic_width
            for i in range(self.pic_width):
                if not self.exited_app:
                    self.bg_canvas.moveto(self.bg_image_1, x=hop, y=hop)
                    hop -= 1
                    time.sleep(.01)
                
            time.sleep(10)
            hop = 0
            hop_neg = 0
            for i in range(self.pic_width):
                if not self.exited_app:
                    self.bg_canvas.moveto(self.bg_image_1, x=hop, y=hop_neg)
                    hop += 1
                    hop_neg -= 1
                    time.sleep(.01)

            time.sleep(20)
            hop = 0 - self.pic_width
            for i in range(self.pic_width):
                if not self.exited_app:
                    self.bg_canvas.moveto(self.bg_image_1, x=hop, y=hop)
                    hop += 1
                    time.sleep(.01)
            
            time.sleep(10)
            hop = 0
            hop_neg = 0
            for i in range(self.pic_width):
                if not self.exited_app:
                    self.bg_canvas.moveto(self.bg_image_1, x=hop, y=hop_neg)
                    hop -= 1
                    hop_neg += 1
                    time.sleep(.01)

            time.sleep(1.1)

    # Define date and time for window
    def date_time(self):
        
        self.dtN = dTime.datetime.now()
        self.dNow = self.dtN.date()
        self.tNow = self.dtN.time()
        self.nDate = self.dNow.strftime('%m/%d/%Y')
        self.newDate = self.dNow.strftime('%m_%d_%Y')
        self.new_time = self.tNow.strftime('%H_%M')
        self.nTime = self.tNow.strftime('%H:%M:%S')
        self.nMonth = self.dNow.strftime('%m')
        self.nDay = self.dNow.strftime('%d')
        self.nMinute = self.tNow.strftime('%M')
        self.nSecond = self.tNow.strftime('%S')
        self.nMonthYear = self.dNow.strftime('%m_%Y')

    # Define Minimizing window
    def min_win(self):
        self.root.state('withdrawn')
        self.root.overrideredirect(False)
        self.root.state('iconic')

    # Define Maximizing window
    def max_win(self, event):
        self.root.overrideredirect(True)

    # Define user message
    def user_message(self):
        self.user_msg = messagebox.showinfo('Developed by Codezzz --> INFORMATION', '-->YOUR INFO HERE<--')

    #Define setting window and pic height
    def set_window_size(self, x: int, y: int):
        self.pic_width = x
        self.pic_height = y
        self.width = self.pic_width + 30 
        self.height = self.pic_height + 30
        self.root.update()

    @property
    def zero(self):
        return self.__zero
    
    # Define right click msg
    def exit_msg(self):
        self.msg_exit = messagebox.askyesno('EXITING', 'WOULD YOU LIKE TO CLOSE THE LAB APP?')
        if self.msg_exit:
            self.exit_app()
        else:
            pass
    
    # Define exiting app
    def exit_app(self):

        self.exited_app = True
        time.sleep(.5)
        self.bg_canvas.delete('all')
        self.stop.set()
        self.root.destroy()       
           
#                                                            Dictionary Classes
#####################################################################################################################################################################################

# Define Adding element to dict()
class MyDict(dict):
  # __init__ function
  def __init__(self):
    self = dict()
 
  # Function to add key:value
  def add(self, key, value):
    self[key] = value

#####################################################################################################################################################################################

# Method to build ny window template
def new_win():

    # declare global varibles
    global list_box
    global app
    global path_0, path_00, path_01, path_001, path_1, path_2, path_10, path_20, path_round_1, path_round_2, path_round_01, path_round_02, path_round_3

    path_bg_1 = 'img/bg_ping_0.png'
    path_bg_2 = 'img/bg_ping_1.png'
    exit_btn_pic = 'img/min_btn3.png'
    min_btn_pic = 'img/min_btn2.png'
    icon = 'img/logo.ico'
    pic_x = 600
    pic_y = 600

    # making instance of window
    app = NewWin(title='1st Window', pic_x=pic_x, pic_y=pic_y, pic_path_1=path_bg_1, pic_path_2=path_bg_2,
                  exit_btn_path=exit_btn_pic, min_btn_path=min_btn_pic, logo_path=icon
                  )

    #setting dispay font
    app.font = ('Imprint MT Shadow', 12)

    # assigning a variable to my background Canvas
    cv = app.bg_canvas
    root = app.root

    # Path to my button pics
    path_0 = 'img/start_stop_80/start.png'
    path_00 = 'img/start_stop_80/stop.png'
    path_01 = 'img/start_stop_160/start.png'
    path_001 = 'img/start_stop_160/stop.png'
    path_1 = 'img/start_stop_80/pressed.png'
    path_2 = 'img/start_stop_80/hover.png'
    path_10 = 'img/start_stop_160/pressed.png'
    path_20 = 'img/start_stop_160/hover.png'
    path_round_1 = 'img/buttons_round/red_up.png'
    path_round_2 = 'img/buttons_round/red_down.png'
    path_round_01 = 'img/buttons_round/green_up.png'
    path_round_02 = 'img/buttons_round/green_down.png'
    path_round_3 = 'img/buttons_round/hov_up.png'

    new_button = app.create_button(x=360, y=180, image_static_path=path_0, image_pressed_path=path_1,
                                    image_hover_path=path_2, image_width=80, image_height=50, command=little_print
                                   )

    stop_btn = app.create_button(x=360, y=240, image_static_path=path_00, image_pressed_path=path_1,
                                    image_hover_path=path_2, image_width=80, image_height=50, command=lil_stop_print
                                   )
    
    round_stop_btn = app.create_button(x=290, y=240, image_static_path=path_round_1, image_pressed_path=path_round_2,
                                    image_hover_path=path_round_3, image_width=50, image_height=50, command=lil_stop_print
                                   )
     
    round_start_btn = app.create_button(x=290, y=180, image_static_path=path_round_01, image_pressed_path=path_round_02,
                                    image_hover_path=path_round_3, image_width=50, image_height=50, command=little_print
                                   )
    
    big_button = app.create_button(x=480, y=180, image_static_path=path_01, image_pressed_path=path_10,
                                    image_hover_path=path_20, image_width=160, image_height=100, command=big_print
                                   )

    big_stop_btn = app.create_button(x=480, y=240, image_static_path=path_001, image_pressed_path=path_10,
                                    image_hover_path=path_20, image_width=160, image_height=100, command=lambda: change_screen(1)
                                   )

    app_title = app.text(300, 300, fill="#C2AD2D", font=('Imprint MT Shadow', 30), text='Testing My NewWin Class')

    list_box = Listbox(root, font=('Imprint MT Shadow', 10), bg='#000000', 
                           fg='#DBD910', width=45, height=15)
    list_box.place(x=15, y=340)

    app.root.update()
    app.root.mainloop()

def change_screen(screen: int):
    if screen == 1:
        app.exit_app()
        second_win()
    elif screen == 2:
        app_second.exit_app()
        new_win()
    else:
        pass

def second_win():
    global app_second
    global list_box

    path_bg_1 = 'img/temp_bg_0.png'
    path_bg_2 = 'img/temp_bg_1.png'
    exit_btn_pic = 'img/min_btn3.png'
    min_btn_pic = 'img/min_btn2.png'
    icon = 'img/all.ico'
    pic_x = 400
    pic_y = 400

    app_second = NewWin(title='2nd Window', pic_x=pic_x, pic_y=pic_y, pic_path_1=path_bg_1, pic_path_2=path_bg_2,
                         exit_btn_path=exit_btn_pic, min_btn_path=min_btn_pic, logo_path=icon
                         )

    cv = app_second.bg_canvas
    root = app_second.root
    lbl_place_y = app_second.pic_height * .66
    btn_x = app_second.pic_width * .80
    btn_y_1 = app_second.pic_height * .35
    btn_y_2 = app_second.pic_height * .5
    text_geo = (app_second.pic_width + app_second.pic_height) / 4
    print(text_geo)
    

    big_button = app_second.create_button(x=int(btn_x), y=int(btn_y_1), image_static_path=path_01, image_pressed_path=path_10,
                                    image_hover_path=path_20, image_width=160, image_height=100, command=big_print
                                   )

    big_stop_btn = app_second.create_button(x=int(btn_x), y=int(btn_y_2), image_static_path=path_001, image_pressed_path=path_10,
                                    image_hover_path=path_20, image_width=160, image_height=100, command=lambda: change_screen(2)
                                   )

    app_title = app_second.text(int(text_geo), int(text_geo), fill="#C2AD2D", font=('Imprint MT Shadow', 20), text='Testing My NewWin Class')

    list_box = Listbox(root, font=('Imprint MT Shadow', 10), bg='#000000', 
                           fg='#DBD910', width=30, height=3)
    list_box.place(x=15, y=int(lbl_place_y))


    app_second.root.update()
    app_second.root.mainloop()

def little_print():
    print('start')
    list_box.insert(END, 'little start button is working')

def lil_stop_print():
    print('stop')
    list_box.insert(END, 'little stop button is working')

def big_print():
    print('START')
    list_box.insert(END, 'BIG START BUTTON IS WORKING')

def big_stop_print():
    print('STOP')
    list_box.insert(END, 'BIG STOP BUTTON IS WORKING')

if  __name__=='__main__':
    new_win()