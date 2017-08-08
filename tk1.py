from tkinter import *

root = Tk()

texkLabel = Label(root,
                  text='您所下载的影片含有限制',
                  justify=LEFT,
                  padx=10)
texkLabel.pack(side=LEFT)

photo = PhotoImage(file='18.gif')
imgLabel = Label(root, image=photo)
imgLabel.pack()

mainloop()
