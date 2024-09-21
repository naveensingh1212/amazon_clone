"""import tkinter as tk
#print(tk.TkVersion)
root= tk.Tk()
root.title("First Window")
root.mainloop()"""
#Add Title and Label
"""from tkinter import Tk,Label
root=Tk()
root.title("Python GUI")
msg=Label(root,text='Welcome to Programming with Tkinter')
msg.pack()
root.mainloop()
import tkinter as tk
root=tk.Tk()
msg=tk.Label(root,text='Welcome to Programming with Tkinter')
msg.pack()
root.mainloop()"""
#To change the font
import tkinter as tk
root=tk.Tk()
msg=tk.Message(root,text='Welcome to Programming with Tkinter')
msg.config(font=('callibri',24,'italic bold underline'))
msg.pack()
root.mainloop()
#To display two labels with different cplored background
import tkinter as tk
root=tk.Tk()
label1=tk.Label(root,text="Welcome to Python",background='red')
label2=tk.Label(root,text="have a Good day",background='green')
label1.pack(fill=tk.Y,pady=20,ipady=25,side=tk.LEFT)
label2.pack(fill=tk.Y,padx=20,ipady=40,side=tk.LEFT)
root.mainloop()
"""#To display an image
import sys
import tkinter as tk
root=tk.Tk()
img=tk.PhotoImage(file=sys.argv[1])
IMG=tk.Label(root,image=img)
IMG.pack()
root.mainloop()
import sys
from tkinter import Tk,Label, PhotoImage
root=Tk()
img=PhotoImage(file=sys.argv[1])
IMG=Label(root,image=img)
IMG.pack()
root.mainloop()"""
#to print a colored text on colored backgroud of GUI window
import tkinter as tk
root=tk.Tk()
label=tk.Label(root,text="Hello world")
label.pack()
label.config(foreground="Yellow",background="blue",text="Updated Text")
root.mainloop()