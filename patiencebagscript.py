from pyautogui import *
import pyautogui
import keyboard
import mouse
from threading import Thread

# This Script Opens PatientBags automatically.
# To use the script you need to bind your slot 8 and 9 to the respective keys: (slot "8" -> "r") and (slot "9" to "f")
# Then just place the patient bag in the "8th" slot, that is, on the "r" key and then Toggle the Script
# To toggle the script, you use the "o" key to toggle and the "p" key to untoggle whenever you want.

toggle = False

def checktoggle():
   global toggle
   while True:
      if keyboard.read_key() == "p":
        print("unToggle Key was read, Stopping script.")
        toggle = True
        
def main():
   while True:
      if toggle==False:
         print("Start")
         sleep(0.05)
         keyboard.press_and_release("r")
         sleep(0.05)
         mouse.click("right")
         sleep(0.1)
         pyautogui.moveTo(847, 346)
         sleep(0.05)
         keyboard.press("shift")
         sleep(0.05)
         mouse.click("left")
         sleep(0.05)
         keyboard.release("shift")
         sleep(0.05)
         keyboard.press_and_release("f")
         sleep(0.05)
         mouse.click("right")
         sleep(0.1)
         pyautogui.moveTo(847, 346)
         sleep(0.05)
         keyboard.press("shift")
         sleep(0.05)
         mouse.click("left")
         sleep(0.05)
         keyboard.release("shift")
      elif toggle==True:
         break

Thread(target=checktoggle).start()
while True:
   if keyboard.read_key() == "o":
      toggle = False
      print("Toggle Key was read, Starting script.")
      main()