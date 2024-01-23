from PIL import Image
import sys
import keyboard


import serial

from pycomm3 import SLCDriver
from pycomm3 import CIPDriver
from pycomm3 import LogixDriver









filen = 'img/All.png'
img = Image.open(filen)
img.save('img/All.ico', format= 'ICO', sizes=[(32,32)])

# def stop(event):  
#     sys.exit()

  
# press ctrl+esc to stop the script 
# keyboard.add_hotkey("ctrl+esc", lambda: stop)

# def slc_connection():

#     with LogixDriver('192.168.0.2/0') as plc:
#         print(plc.get_plc_name())
    
# def connect_serial():
#     PARITY_NONE = None

#     keyboard.add_hotkey("ctrl+esc", lambda: stop)
#     serialPort = serial.Serial(port="COM5", baudrate=1200, bytesize=8, parity=PARITY_NONE, stopbits=serial.STOPBITS_ONE, xonxoff=True)
#     serialString = ""  # Used to hold data coming over UART
#     while 1:
#         # Wait until there is data waiting in the serial buffer
#         if serialPort.in_waiting > 0:

#             # Read data out of the buffer until a carraige return / new line is found
#             serialString = serialPort.readline()

#             # Print the contents of the serial data
#             try:
#                 print(serialString.decode("Ascii"))
#             except:
#                 pass

# if __name__=='__main__':
#     connect_serial()