import tkinter as tk
window=tk.Tk()
window.title("GUI")

# label=tk.Label(window, text="hello world")
# label.pack()
# window.mainloop()


# label=tk.Label(text="python rocks!")
# label=tk.Label(text="hello Tkinter",fg="white",bg="black",width=10,height=10)
# button=tk.Button(text="hello, tkinter",width=25,height=5, bg="blue",fg="green")
# entry=tk.Entry(fg="white",bg="blue",width=50)
# label=tk.Label(text="Name")
# name=entry.get()
# name
# entry=tk.Entry()
# label.pack()
# button.pack()
# entry.pack()
# window.mainloop()

# topframe=tk.Frame(window).pack()
# bottomframe=tk.Frame(window).pack(side="bottom")
# bt1=tk.Button(topframe,text="button1",fg="red").pack
# bt2=tk.Button(topframe,text="button2",fg="green").pack(side="right")
# window.mainloop()

tk.Label(window,text="Username").grid(row=0)
tk.Entry(window).grid(row=0,column=1)
tk.Label(window,text="Password").grid(row=1)
tk.Entry(window).grid(row=1,column=1)
tk.Checkbutton(window,text="Keep me logged in").grid(columnspan=2)
window.mainloop()