import random
import tkinter as tk
from functools import partial
import pyttsx3
import time
import tkinter.scrolledtext as ScrolledText

def display(label_result,n1):
              userInput = int(n1.get())
              while n != "userInput":
                  engine = pyttsx3.init()
                  if userInput <=0:
                      engine.say('Enter Valid number')
                      label_result.config(text="ChatBot >>> Please enter a valid input.")
                      entryNum1 = tk.Entry(root, textvariable=number).grid(row=1, column=1)
                      display = partial(display, labelResult, number)
                  elif userInput < n:
                      engine.say('Guess is low')
                      label_result.config(text="ChatBot >>> guess is low")
                      entryNum1 = tk.Entry(root, textvariable=number).grid(row=1, column=1)
                      display = partial(display, labelResult, number)
                  elif userInput > n:
                      engine.say('guess in high')
                      label_result.config(text="ChatBot >>> guess is high")
                      entryNum1 = tk.Entry(root, textvariable=number).grid(row=1, column=1)
                      display = partial(display, labelResult, number)
                  else:
                      engine.say('Congo')
                      label_result.config(text="ChatBot >>> you guessed it!")
                      break
                  engine.runAndWait()


root=tk.Tk()
root.geometry('600x400+100+200')
root.title('Guess The Number')

number1=tk.StringVar()

n=random.randint(1, 99)

labelTitle = tk.Label(root, text="Guess The Number").grid(row=0, column=2)
labelNum1 = tk.Label(root, text="Enter any number b/w 1 to 100:").grid(row=1, column=0)

labelResult = tk.Label(root)
labelResult.grid(row=10, column=2)
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=1)

display = partial(display, labelResult, number1)


buttonCal = tk.Button(root, text="Enter",command=display).grid(row=6, column=0)


root.mainloop()
