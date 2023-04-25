import tkinter as tk
from tkinter import ttk

counter = 0

def callback():
  global counter
  counter += 1
  print(counter)
  

root =tk.Tk()
root.geometry('300x400')
root.title('Hello Button')
helloButton = ttk.Button(
   root, 
   text="Hello", 
   command=callback
)

helloButton.pack(
  ipadx=5,
  ipady=5,
  expand=True
)

root.mainloop()