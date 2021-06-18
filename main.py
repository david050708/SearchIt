import tkinter as tk
import webbrowser
from tkinter import *
from googlesearch import search

frame = root = Tk()
root.geometry("500x500")
root.title("SearchIT")
root.iconbitmap("C:/Users/kani/Downloads/images.ico")

searching = Entry(root,width=50,bg="white",fg="black")
searching.pack(padx=10,pady=20)

def remove():
    label1.pack_forget()

def searchit():
    try:
        searchWeb = searching.get()
        for j in search(searchWeb, num=1,stop=1,pause=1):
            print(j)
            global label1
            label1 = Label(root,text=j)
            label1.pack()
    except Exception as e:
		    print(f'Sorry cannot complete your request please check your connection and try after sometime')

def opening():
    webbrowser.open_new(url="https://en.wikipedia.org/wiki/" + searching.get())

def google():
    webbrowser.open_new(url="https://www.google.co.in/")



b1 = tk.Button(root,text="Seach",bg="grey",fg="black",command=searchit).pack()
b2 = tk.Button(root,text="Clear",bg="grey",fg="black",command=remove).pack()
b3 = tk.Button(root,text="Open in the Web",bg="grey",fg="black",command=opening).pack()
b4 = tk.Button(root,text="Open Google",bg="grey",fg="black",command=google).pack()

root.mainloop()
