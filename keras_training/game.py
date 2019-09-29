import tkinter as tkr
import os

#main window with name 'GameWindow'
root = tkr.Tk(className='GameWindow')
HEIGHT = 500
WIDTH = 600
canvas = tkr.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()


bg_file = tkr.PhotoImage(file=os.path.abspath('bg_image.png'))
#set background color
bg_label = tkr.Label(root, image=bg_file)
bg_label.place(relwidth=1,relheight=1)


root.mainloop()