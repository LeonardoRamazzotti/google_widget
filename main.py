# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 10:11:02 2021

@author: Leo
"""
from tkinter import *
import webbrowser


def Searchbar(entry):
    
    search_word =str(entry_google.get())
    
    webbrowser.open('https://www.google.com/search?q='+ search_word)
    
    entry_google.delete(0,'end')




root = Tk()
root.title('Essential Widget')
root.geometry('900x60+450+70')





root.overrideredirect(True)
root.wait_visibility(root)
root.wm_attributes('-transparentcolor','#3D3D3D')
root.config(bg='#3D3D3D')


image_bg = PhotoImage(file='bg.png')
b_google = PhotoImage(file='google.png')

Label_bg = Label(root, image =image_bg , bg = '#3D3D3D')
Label_bg.pack()

entry_google = Entry(root,width=64,bg='#636363',fg='#1F2226',font = ('ABeeZee',16),highlightthickness = 0,borderwidth=0,selectbackground='white')
entry_google.place(x=30,y=16)

Button_search = Button(root,image = b_google,bg='#414141',command = lambda: Searchbar(entry_google),highlightthickness = 0,borderwidth=0,activebackground='#33363B')
Button_search.place(x=845,y=14)

root.bind('<F1>', lambda event: root.destroy())


root.mainloop()