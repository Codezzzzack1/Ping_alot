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

    
#                                                               Classes Defined
#####################################################################################################################################################################################
#####################################################################################################################################################################################

# Class to make canvas a button
class MyLabel(Label):
    def __init__(self,parent,  command=None,  **kwargs):
        Label.__init__(self,parent, **kwargs)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.command = command
        self.press_image = self.image

    def _on_press(self, event):
        self.configure(relief="sunken", bd=2)

    def _on_release(self, event):
        self.configure(relief="flat")
        if self.command is not None:
            self.command()

    def on_enter(self, event):
        self['background'] = self['activebackground']

    def on_leave(self, event):
        self['background'] = self.defaultBackground

# Class for threading value updates
class ValUpdateThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        val_update()

#Define Thread starter
def strt_val_update():
    try:
        val_thread = ValUpdateThread()
        val_thread.daemon = True
        val_thread.start()
    except Exception as e:
        print('unable to start strt_val_update, ' + str(e))

# Class for threading value updates
class PicAnimateThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        pic_animate()

#Define Thread starter
def strt_pic_animate():
    try:
        pic_thread = PicAnimateThread()
        pic_thread.daemon = True
        pic_thread.start()
    except Exception as e:
        print('unable to start strt_pic_animate, ' + str(e))

# Class for threading value updates
class PingAlotThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        ping_alot()

#Define Thread starter
def strt_ping_alot():
    try:
        ping_thread = PingAlotThread()
        ping_thread.daemon = True
        ping_thread.start()
    except Exception as e:
        print('unable to start strt_ping_alot, ' + str(e))

# Class for threading value updates
class PingBlinkThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        ping_blink()

#Define Thread starter
def strt_ping_blink():
    try:
        blink_thread = PingBlinkThread()
        blink_thread.daemon = True
        blink_thread.start()
    except Exception as e:
        print('unable to start strt_ping_blink, ' + str(e))

# Class for threading value updates
class StopScanThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        stop_scanning()

#Define Thread starter
def strt_stop_scanning():
    try:
        stop_thread = StopScanThread()
        stop_thread.daemon = True
        stop_thread.start()
    except Exception as e:
        print('unable to start strt_stop_scanning, ' + str(e))

#                                                               SPLASH INTRO
#####################################################################################################################################################################################
#####################################################################################################################################################################################

# Define Splash screen
def splash_win():
    global splash_root
    global pg_bar
    global load_lbl
    global img_lbl

    splash_root = Tk()
    splash_root.geometry('615x645+660+240')
    splash_root.config(relief='ridge', bd=15, bg='black')
    splash_root.overrideredirect(True)
    splash_root.bind("<Escape>", lambda event: sys.exit())
    #splash_root.wm_attributes('-transparentcolor', 'yellow')

    frame = Frame(splash_root, bg='black')
    frame.pack(side='bottom')

    img = PhotoImage(file="img/developer.png", height=600, width=600)
    img_0 = PhotoImage(file="img/python_power.png", height=600, width=600)

    s = ttk.Style()
    s.theme_use('clam')
    s.configure("gray.Horizontal.TProgressbar", background='black', foreground='gray')

    imprint16 = font.Font(family='Georgia', size=16, weight='bold')

    img_lbl = Label(splash_root, image=img_0)
    img_lbl.pack()

    load_lbl = Label(frame, bg='black', fg='gray', font=('Imprint MT Shadow', 18), text='Loading . . . ')  
    load_lbl.pack()

    pg_bar = ttk.Progressbar(frame, orient=HORIZONTAL, length=500, value=0, mode='determinate', style='gray.Horizontal.TProgressbar')
    pg_bar.pack()

    splash_root.after(1000, prog_bar)
    splash_root.update()
    splash_root.mainloop()

# Define Progress Bar Action
def prog_bar():

    img = PhotoImage(file="img/developer.png", height=600, width=600)
    img_0 = PhotoImage(file="img/python_power.png", height=600, width=600)
    
    
    start_time = time.time()
    while((time.time() - start_time) < 10):

        pg_bar['value'] += 10
        pg_val = pg_bar['value']
        if pg_val < 25:
            load_lbl['text'] = f'Loading . . . . {pg_val}%'
        elif 25 <= pg_val < 50:
            load_lbl['text'] = f'Loading . . . {pg_val}%'
        elif 50 <= pg_val < 75:
            load_lbl['text'] = f'Loading . . {pg_val}%'
            img_lbl['image'] = img
        elif 75 <= pg_val <= 90:
            load_lbl['text'] = f'Loading . {pg_val}%'
        elif pg_val > 91:
            load_lbl['text'] = f'Loading {pg_val}%'
        splash_root.update()
        time.sleep(1)

    else:
        splash_root.destroy()
        ping_win()

#                                                               App Window and Functions
#####################################################################################################################################################################################
#####################################################################################################################################################################################

# Define temp and time window
def ping_win():
    global ping_root
    global canvas
    global exited_app
    global pinging
    global stop_scan
    global date_txt
    global ping_txt
    global pinged_lbox
    global pinged_ebox
    global pinged_btn
    global pinged_ip
    global image_0
    global image_1
    global image_2
    global x_1
    global x_2

    exited_app = False
    pinging = False
    stop_scan = False
    x_1 = 0
    x_2 = 600
    y_1 = -600
    user = os.getenv('username')

    customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    ping_root = CTk()
    ping_root.title('Ping All Application')
    ping_root.geometry('630x630+645+225')
    ping_root.config(relief='ridge', bd=15, bg='black')
    icon = 'img/All.ico'
    ping_root.iconbitmap(icon)
    ping_root.overrideredirect(True)
    ping_root.bind("<Escape>", lambda event: exit_app())
    #ping_root.bind("<Button-1>", lambda event: right_click())
    ping_root.bind("<Button-3>", lambda event: exit_msg())
    ping_root.bind("<Map>", max_win)

    img_0 = PhotoImage(file="img/bg_ping_0.png", height=600, width=600)
    img_1 = PhotoImage(file="img/bg_ping_1.png", height=600, width=600)
    img_2 = PhotoImage(file="img/All.png", height=600, width=600)
    img_ping = PhotoImage(file="img/press_chrome.png", height=50, width=80)
    img_stop = PhotoImage(file="img/press_chrome_stop.png", height=50, width=80)
    img_ping_0 = PhotoImage(file="img/pressed.png", height=50, width=80)
    img_ping_1 = PhotoImage(file="img/press_hover.png", height=50, width=80)
    img_min = PhotoImage(file="img/min_btn1.png", height=50, width=50)
    img_lbl = PhotoImage(file="img/developer.png", height=100, width=100)

    canvas = Canvas(ping_root, width=630, height=630, bg='black')
    canvas.pack(fill=BOTH)
    # new_button = MyCanvas(ping_root, width=80, height=240, bg='black', command=strt_ping_alot)
    # new_button.place(x=325, y=340)
    image_0 = canvas.create_image(x_1,0, image=img_0, anchor=NW)
    image_1 = canvas.create_image(x_2,0, image=img_1, anchor=NW)
    image_2 = canvas.create_image(0,y_1, image=img_2, anchor=NW)
    image_3 = canvas.create_image(35,35, image=img_min, anchor=CENTER)
    canvas.tag_bind(image_3, sequence="<Button-1>", func=lambda event: min_win())
    date_txt = canvas.create_text(480, 80, fill="#C2AD2D", font=('Imprint MT Shadow', 30), justify=CENTER)
    user_txt = canvas.create_text(480, 20, fill="#C2AD2D", font=('Imprint MT Shadow', 14), justify=CENTER, text=f'{user} is Online')
    canvas.tag_bind(user_txt, sequence="<Button-1>", func=lambda event: right_click())
    hover_config(canvas, user_txt, '#2E14AD', '#C2AD2D')
    ping_txt = canvas.create_text(400, 200, fill="#C2AD2D", text='PING NETWORK', font=('Imprint MT Shadow', 30), justify=CENTER)

    pinged_lbox = Listbox(ping_root, font=('Imprint MT Shadow', 10), bg='#000000', 
                           fg='#DBD910', width=45, height=15)
    pinged_lbox.place(x=15, y=340)

    pinged_ip = StringVar()
    pinged_ip.set('Enter ###.###.###')
    pinged_ebox = Entry(ping_root, relief='sunken', bd=3, textvariable=pinged_ip, font=('Imprint MT Shadow', 18), bg='#000000', fg='#DBD910', width=26)
    pinged_ebox.bind('<FocusIn>', lambda e: e.widget.select_range(0, 'end'))
    pinged_ebox.bind("<Return>", lambda event: strt_ping_alot())
    pinged_ebox.place(x=15, y=295)

    pinged_btn = canvas.create_image(375,313, image=img_ping, anchor=CENTER)
    btn_config(canvas, pinged_btn, img_ping, img_ping_0, img_ping_1, strt_ping_alot)     

    stop_btn = canvas.create_image(375,353, image=img_stop, anchor=CENTER)
    btn_config(canvas, stop_btn, img_stop, img_ping_0, img_ping_1, strt_stop_scanning)            

    ping_root.after(1000, strt_val_update)
    ping_root.after(1007, strt_pic_animate)
    ping_root.update()
    ping_root.mainloop()

# Define configuring button binds
#----------------------------------------------------------------------------------------------------------
def btn_config(parent, btn, img, img1, img2, command):
    parent.tag_bind(btn, sequence="<ButtonPress-1>", func=lambda event: on_press(parent, btn, img1))
    parent.tag_bind(btn, sequence="<ButtonRelease-1>", func=lambda event: on_release(parent, btn, img, command))
    parent.tag_bind(btn, sequence="<Enter>", func=lambda event: on_enter(parent, btn, img2))
    parent.tag_bind(btn, sequence="<Leave>", func=lambda event: on_leave(parent, btn, img))

# function for pressing buttons
#-----------------------------------------------------------------------------------------------------------
def on_press(parent, btn, img1):
    parent.itemconfigure(btn, image=img1)

def on_release(parent, btn, img,  command):
    parent.itemconfigure(btn, image=img)
    command()

def on_enter(parent, btn, img2):
    parent.itemconfigure(btn, image=img2)

def on_leave(parent, btn, img):
    parent.itemconfigure(btn, image=img)

# fuctions for hover color change
#----------------------------------------------------------------------------------------------------------------   
# Define hover configs
def hover_config(parent, tag, color_1, color_2):
    parent.tag_bind(tag, sequence="<Enter>", func=lambda event: color_change(parent, tag, color_1))
    parent.tag_bind(tag, sequence="<Leave>", func=lambda event: color_resume(parent, tag, color_2))

# Define color change on hover
def color_change(parent, tag, color):
    parent.itemconfigure(tag, fill=color)

# Define color change on hover
def color_resume(parent, tag, color):
    parent.itemconfigure(tag, fill=color)

#----------------------------------------------------------------------------------------------------------------

# Define exiting app
def exit_app():
    global exited_app

    exited_app = True
    ping_root.destroy()
    sys.exit()

# Define updating values
def val_update():
    global canvas
    global temp_txt
    global date_txt

    try:
        while not exited_app:
            date_time()
            new_date = nDate
            new_time = nTime

            canvas.itemconfigure(date_txt, text=f'{new_date}\n{new_time}')

            time.sleep(.1)
        else:
            pass


    except Exception as e:
        if not exited_app:
            print(e)
            ping_root.after(1001, strt_val_update)
        else:
            pass

# Define Pinging array of IP's
def ping_alot():
    global pinging
    global stop_scan

    network = str(pinged_ip.get())
    pinged_lbox.delete(0, END)
    pinging = True
    stop_scan = False
    strt_ping_blink()

    if valid_network(network):
        start_time = time.time()
        for n in range(1, 254):
            if not (exited_app or stop_scan):
                result = os.popen(f'ping -n 2 {network}.{n}').read()
                result = str(result)
                print(result)
                if 'not recognized' in result:
                    pinged_lbox.insert(END, f'{network} INVALID')
                    break
                else:
                    if 'Request' in result:
                        pinged_lbox.insert(END, f'{network}.{n} AVAILABLE!')
                    elif 'Destination' in result:
                        pinged_lbox.insert(END, f'{network}.{n} AVAILABLE!')
                    else:
                        pinged_lbox.insert(END, f'{network}.{n} NOT AVAILABLE!')
                        
                time.sleep(1)
            else:
                break
        end_time = (time.time() - start_time) / 60
        end_time = round(end_time, 2)
        msg_time = messagebox.showinfo('PING TIME', f'PING HAS COMPLETED!\nELAPSED TIME: {end_time} MINUTES')
        pinging = False
    else:
        pinging = False
        msg_ip = messagebox.showwarning('ERROR', 'MUST ONLY ENTER 1ST 3 OCTALS LIKE SO:\nEXAMPLE: 192.168.0')

# Define stop scanning
def stop_scanning():
    global stop_scan
    global pinged_ip

    stop_scan = True
    time.sleep(3)
    pinged_ip.set('Enter ###.###.###')
    canvas.itemconfigure(ping_txt, text='PING NETWORK')

#Define how to get Ip out of string
def valid_network(s):
    a = s.split('.')
    if len(a) != 3:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

# Define Pinging Blink
def ping_blink():
    global ping_txt

    while pinging:
        canvas.itemconfigure(ping_txt, text='PINGING')
        time.sleep(.5)
        canvas.itemconfigure(ping_txt, text='')
        time.sleep(.5)
    else:
        canvas.itemconfigure(ping_txt, text='PING NETWORK')

# Define picture animation
def pic_animate():
    global image_0
    global image_1

    while not exited_app:

        time.sleep(20)
        hop = 600
        for i in range(600):
            canvas.moveto(image_1, x=hop, y=hop)
            hop -= 1
            time.sleep(.01)
            
        time.sleep(10)
        hop = 0
        hop_neg = 0
        for i in range(600):
            canvas.moveto(image_1, x=hop, y=hop_neg)
            hop += 1
            hop_neg -= 1
            time.sleep(.01)

        time.sleep(20)
        hop = -600
        for i in range(600):
            canvas.moveto(image_1, x=hop, y=hop)
            hop += 1
            time.sleep(.01)
        
        time.sleep(10)
        hop = 0
        hop_neg = 0
        for i in range(600):
            canvas.moveto(image_1, x=hop, y=hop_neg)
            hop -= 1
            hop_neg += 1
            time.sleep(.01)
        
        time.sleep(10)
        hop = 0
        hop_neg = -600
        for i in range(1000):
            canvas.moveto(image_2, x=hop, y=hop_neg)
            hop_neg += 1
            time.sleep(.01)

        hop = 0
        hop_neg = 400
        for i in range(400):
            canvas.moveto(image_2, x=hop, y=hop_neg)
            hop += 1
            time.sleep(.01)

        hop = 400
        hop_neg = 400
        for i in range(400):
            canvas.moveto(image_2, x=hop, y=hop_neg)
            hop_neg -= 1
            time.sleep(.01)

        hop = 400
        hop_neg = 0
        for i in range(600):
            canvas.moveto(image_2, x=hop, y=hop_neg)
            hop -= 1
            time.sleep(.01)

        time.sleep(1.1)

# Define Date and time
def date_time():
    global nTime
    global nDate
    global newDate
    global new_time
    global nMonth
    global nDay
    global nMinute
    global nSecond
    global nMonthYear
    
    dtN = dTime.datetime.now()
    dNow = dtN.date()
    tNow = dtN.time()
    nDate = dNow.strftime('%m/%d/%Y')
    newDate = dNow.strftime('%m_%d_%Y')
    new_time = tNow.strftime('%H_%M')
    nTime = tNow.strftime('%H:%M:%S')
    nMonth = dNow.strftime('%m')
    nDay = dNow.strftime('%d')
    nMinute = tNow.strftime('%M')
    nSecond = tNow.strftime('%S')
    nMonthYear = dNow.strftime('%m_%Y')

# Define Minimizing window
def min_win():
    ping_root.state('withdrawn')
    ping_root.overrideredirect(False)
    ping_root.state('iconic')

# Define Maximizing window
def max_win(event):
    ping_root.overrideredirect(True)

# Define right click msg
def exit_msg():
    msg_exit = messagebox.askyesno('EXITING', 'WOULD YOU LIKE TO CLOSE THE LAB APP?')
    if msg_exit:
        exit_app()
    else:
        pass

# Define Information on left click
def right_click():
    
    msg_info = messagebox.showinfo('Devoloped by Codezzz --> INFORMATION', f'--> ENTER THE 1ST 3 OCTALS IN A NETWORK AND PRESS PING.\n--> RIGHT CLICK TO EXIT THE APP!')

if __name__=='__main__':
    ping_win()