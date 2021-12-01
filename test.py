import tkinter

root = tkinter.Tk()

root.geometry("300x300")

a_file = open("resume")

res = a_file.readlines()

lb = tkinter.Label(root, text=res)

lb.pack()

root.mainloop()