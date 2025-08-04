from encodings.punycode import T
from operator import sub
from xml.dom.minidom import Attr
import keyboard #hotkeys
import os
import subprocess #running chrome
import win32com.client #process monitoring
import win32com.client
import ctypes

def open_terminal():
    os.system("start cmd")

def open_chrome():
    shortcut= r"C:/Users/rexha/Desktop/chrome - Shortcut.lnk"
    subprocess.run(f'start "" "{shortcut}"', shell=True)  

def open_time():
    os.system("start cmd && time")      

keyboard.add_hotkey("win+e", open_terminal, suppress=True)
keyboard.add_hotkey("win+c", open_chrome, suppress=True )
keyboard.add_hotkey("win+t", open_time, suppress=True)


def monitor_new_process():
    wmi = win32com.client.GetObject("winmgmts:")
    watcher = wmi.ExecNotificationQuery("SELECT * FROM __InstanceCreationEvent WITHIN 1 WHERE TargetInstance ISA 'Win32_Process'")

    print("Monitoring for new processes...")
    while True:
        event = watcher.NextEvent()
        process_name = event.TargetInstance.Name
        print(f"New process detected: {process_name}")

        


monitor_new_process()

keyboard.wait()


