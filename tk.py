import tkinter
from tkinter import ttk

    
def avant():
    page1.pack_forget()
    bg_label2 = tkinter.Label(page2, image=bg_img)
    frame10 = tkinter.Frame(page2)
    frame10.place(relx=0.9, rely=0.9, relwidth=0.15, relheight=0.1)
    endbt2 = tkinter.Button(frame10, text="Retour", command=arriere)
    endbt2.pack()
    bg_label2.pack() 
    page2.pack()

def arriere():
    page2.pack_forget()
    endbt.config(text= "Terminer", command=avant)
    page1.pack() 

if __name__ == "__main__":

    root = tkinter.Tk()

    root.attributes("-fullscreen", True)
#---------------------------------------------------------------
    #pages
    page1 = tkinter.Frame(root)
    page1.pack()

    page2 = tkinter.Frame(root)
#---------------------------------------------------------------

#---------------------------------------------------------------
    #arriere plan
    bg_img = tkinter.PhotoImage(file=r"C:\Users\sebas\Downloads\84248.png")
    bg_label = tkinter.Label(page1, image=bg_img)
    bg_label.pack()
#---------------------------------------------------------------

#Page 1
#---------------------------------------------------------------
    frame1 = tkinter.Frame(page1)
    frame1.place(relx=0.425, rely=0.05, relwidth=0.15, relheight=0.05)

    frame2 = tkinter.Frame(page1)
    frame2.place(relx=0.425, rely=0.10, relwidth=0.15, relheight=0.05)

    frame3 = tkinter.Frame(page1)
    frame3.place(relx=0.425, rely=0.20, relwidth=0.15, relheight=0.05)

    frame4 = tkinter.Frame(page1)
    frame4.place(relx=0.425, rely=0.30, relwidth=0.15, relheight=0.05)

    frame5 = tkinter.Frame(page1)
    frame5.place(relx=0.2, rely=0.40, relwidth=0.15, relheight=0.1)

    frame6 = tkinter.Frame(page1)
    frame6.place(relx=0.425, rely=0.40, relwidth=0.15, relheight=0.1)

    frame7 = tkinter.Frame(page1)
    frame7.place(relx=0.65, rely=0.40, relwidth=0.15, relheight=0.1)

    frame8 = tkinter.Frame(page1)
    frame8.place(relx=0.425, rely=0.50, relwidth=0.15, relheight=0.1)

    frame9 = tkinter.Frame(page1)
    frame9.place(relx=0.9, rely=0.9, relwidth=0.15, relheight=0.1)

#---------------------------------------------------------------

#---------------------------------------------------------------
    #buttons

    endbt = tkinter.Button(frame9, text="Termine", command=avant)
    endbt.pack()

#---------------------------------------------------------------
    #labels
    tlb = tkinter.Label(frame1, text= "Bienvenue au SDSN!")
    tlb.config(font=("Arial", 14))
    tlb.pack()

    lb1 = tkinter.Label(frame2, text= "Quel est ton nom?")
    lb1.config(font=("Arial", 10))
    lb1.pack()

    lb2 = tkinter.Label(frame3, text= "Quel est le nom de votre animal?")
    lb2.config(font=("Arial", 8))
    lb2.pack()

    lb3 = tkinter.Label(frame4, text= "Quel est votre adresse courriel?")
    lb3.config(font=("Arial", 8))
    lb3.pack()

    lb4 = tkinter.Label(frame5, text= "Temps de nutrition 1")
    lb4.config(font=("Arial", 8))
    lb4.pack()

    lb5 = tkinter.Label(frame6, text= "Temps de nutrition 2")
    lb5.config(font=("Arial", 8))
    lb5.pack()

    lb6 = tkinter.Label(frame7, text= "Temps de nutrition 3")
    lb6.config(font=("Arial", 8))
    lb6.pack()

    lb7 = tkinter.Label(frame8, text= "Objectif de bruit")
    lb7.config(font=("Arial", 8))
    lb7.pack()
#---------------------------------------------------------------

#---------------------------------------------------------------
    #entry
    e1 = tkinter.Entry(frame2)
    e1.pack()

    e2 = tkinter.Entry(frame3)
    e2.pack()

    e3 = tkinter.Entry(frame4)
    e3.pack()
#---------------------------------------------------------------
    #combobox

    combo1 = ttk.Combobox(frame5, values=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
    combo1.pack()

    combo2 = ttk.Combobox(frame5, values=[0,1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60])
    combo2.pack()

    combo3 = ttk.Combobox(frame6, values=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
    combo3.pack()

    combo4 = ttk.Combobox(frame6, values=[0,1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60])
    combo4.pack()

    combo5 = ttk.Combobox(frame7, values=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
    combo5.pack()

    combo6 = ttk.Combobox(frame7, values=[0,1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60])
    combo6.pack()
#---------------------------------------------------------------
    #scale

    scale1 = tkinter.Scale(frame8, from_=0, to=1000, orient=tkinter.HORIZONTAL)
    scale1.pack()
#---------------------------------------------------------------

#Page2


    root.mainloop()