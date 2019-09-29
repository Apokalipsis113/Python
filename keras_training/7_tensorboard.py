import import tkinter as tk
import os

#main window with name 'GameWindow'
root = tk.Tk(className='GameWindow')
HEIGHT = 500
WIDTH = 600
canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

#set background image
bg_file = tk.PhotoImage(file='bg_image.png')
bg_label = tk.Label(root,image=bg_file)
#placing image for fill background
bg_label.place(relwidth=1,relheight=1)