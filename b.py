from Tkinter import*

root = Tk()
root.title('Python Tk Examples @ pythonspot.com')
Label(root, text='Python').pack(pady=20,padx=50)

root.mainloop()

root=Tk()
root.title('Python Tk Examples @ pythonspot.com')

var = StringVar()
textbox = Entry(root, textariable=var)
textbox.focus_set()
textbox.pack(pady=10, padx=10)

root.mainloop()
