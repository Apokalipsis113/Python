import tkinter as tkr
import os

#main window with name 'GameWindow'
root = tkr.Tk(className='GameWindow')
HEIGHT = 500
WIDTH = 600
canvas = tkr.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

bg_path = os.path.abspath('bg_image.png')
bg_file = tkr.PhotoImage(file=bg_path)
bg_file.
print(bg_path)
#set background 
bg_label = tkr.Label(root, image=bg_file)
bg_label.place(relwidth=1,relheight=1)


root.mainloop()