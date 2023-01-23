import tkinter
import tkinter.messagebox as messagebox

top = tkinter.Tk()

def helloCallBack():
messagebox.showinfo( "Program GUI", "Hello Restu")

B = tkinter.Button(top, text ="Hello Restu", command =helloCallBack)

B.pack()
top.mainloop()
