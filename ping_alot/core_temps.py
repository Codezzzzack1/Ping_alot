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
import wmi
import platform
import wmi
import cpuinfo
import psutil
import subprocess

def process_exists(process_name):
    progs = str(subprocess.check_output('tasklist'))
    if process_name in progs:
        return True
    else:
        return False
    
def core_checker():
    w = wmi.WMI(namespace="root\OpenHardwareMonitor")
    deg = chr(176)

    start_time = time.time()

    if process_exists('OpenHardwareMonitor.exe'):
        while((time.time() - start_time) < 100):
            temperature_infos = w.Sensor()
            for sensor in temperature_infos:
                if sensor.SensorType==u'Temperature':
                    if sensor.Name == 'CPU Package':
                        print(f'{sensor.Name}: {sensor.Value} {deg}C')
                        break
                    time.sleep(.1)
    else:
        os.system(r"C:\OpenHardwareMonitor\OpenHardwareMonitor.exe")
        time.sleep(3)
        core_checker()

if __name__=='__main__':
    core_checker()

