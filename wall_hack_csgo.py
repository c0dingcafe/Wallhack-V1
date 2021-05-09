from tkinter import *
import pymem
import re
import os
import webbrowser

#Banner
print("""
        _,.-------.,_
     ,;~'             '~;, 
   ,;                     ;,
  ;                         ;
 ,'                         ',
,;                           ;,
; ;      .           .      ; ;
| ;   ______       ______   ; | 
|  `/~"     ~" . "~     "~\'  |
|  ~  ,-~~~^~, | ,~^~~~-,  ~  |
 |   |        }:{        |   | 
 |   l       / | \       !   |
 .~  (__,.--" .^. "--.,__)  ~. 
 |     ---;' / | \ `;---     |  
  \__.       \/^\/       .__/  
   V| \                 / |V  
    | |T~\___!___!___/~T| |  
    | |`IIII_I_I_I_IIII'| |  
    |  \,III I I I III,/  |  
     \   `~~~~~~~~~~'    /
       \   .       .   /
         \.    ^    ./   
           ^~~~^~~~^ 

  _________ .____      ___________ ___________ __________  _____.___.  /\               .__                         __             
 /   _____/ |    |     \_   _____/ \_   _____/ \______   \ \__  |   |  )/   ______      |  |__   _____      ____   |  | __   ______
 \_____  \  |    |      |    __)_   |    __)_   |     ___/  /   |   |      /  ___/      |  |  \  \__  \   _/ ___\  |  |/ /  /  ___/
 /        \ |    |___   |        \  |        \  |    |      \____   |      \___ \       |   Y  \  / __ \_ \  \___  |    <   \___ \ 
/_______  / |_______ \ /_______  / /_______  /  |____|      / ______|     /____  >      |___|  / (____  /  \___  > |__|_ \ /____  >
        \/          \/         \/          \/               \/                 \/            \/       \/       \/       \/      \/ 
     (FREE CSGO HACKS JOIN MY DISCORD)
""")

# defs
def callback(url):
    webbrowser.open_new(url)

def button_action():
    if(change_button["text"]=="Start"):
        change_button.configure(text="Stop")
        print("\n")
        print("SCRIPT IS RUNNING")
        print("\n")
    else:
        change_button.configure(text="Start")
        print("\n")
        print("SCRIPT IS STOPPED")
        print("\n")
    try:
        pm = pymem.Pymem('csgo.exe')
        client = pymem.process.module_from_name(pm.process_handle, 'client.dll')

        clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
        address = client.lpBaseOfDll + re.search(rb'\x83\xF8.\x8B\x45\x08\x0F', clientModule).start() + 2

        pm.write_uchar(address, 2 if pm.read_uchar(address) == 1 else 1)
        pm.close_process()
    except:
        change_button.configure(text="Start")
        print("error: please read the README file If you're having trouble join my discord")
        print("\n")

# GUI
gui = Tk()
gui.title("Sleepy's hacks")
gui.geometry("500x300")

# Button
change_button = Button(gui, text="Start", command=button_action)
change_button.place(x = 100, y = 50, width=300, height=100)

# Hyperlink
link = Label(gui, text="DISCORD", fg="blue", cursor="hand2")
link.place(x = 100, y = 175, width=300, height=100)
link.bind("<Button-1>", lambda e: callback("https://discord.gg/FYdcF4FsYy"))

mainloop()
