#MIT License

#Copyright (c) 2022 Yusuf

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

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




