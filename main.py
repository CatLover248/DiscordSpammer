from pynput.keyboard import *
import time


keyboard = Controller()

def press_key(key):
    keyboard.press(str(key))
    keyboard.release(str(key))

print("Discord Spammer b1 - By Yusuf <3 - Made to destroy irl friends on discord!")
message = input("Input message you want to spam: ")
msgdelay = float(input("Input Typing Delay[example: 0.1] : "))
msgsenddelay = float(input("Input the delay between every message sent[example: 2] : "))
print("Go in the window and click on where you send the message - Spammer Activates in 5 Seconds")
message = message + "^"
time.sleep(5)

count = 0
while True:
    time.sleep(msgsenddelay)
    for i in message:
        if i != "^":
            time.sleep(msgdelay)
            press_key(i)
        elif i == "^":
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            print("Message sent! <Message -> " + message.replace("^", "") + " | Count -> " + str(count) + ">")
            count += 1




