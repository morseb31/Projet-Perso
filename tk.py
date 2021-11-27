from multiprocessing.spawn import import_main_path
import tkinter
from tkinter import ttk
from datetime import date
import multiprocessing
from queue import Empty, Full
from typing_extensions import IntVar
import webbrowser
from Motor import *
from soundalert import *
from multiprocessing import *
import os
from queue import *
import PIL
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import mat

#-----------------------------------------------------------------------------------------------------
# functions   
def avant():
    page1.pack_forget()
    bg_label2 = tkinter.Label(page2, image=bg_img)
    frame10 = tkinter.Frame(page2)
    frame10.place(relx=0.9, rely=0.9, relwidth=0.15, relheight=0.1)
    endbt2 = tkinter.Button(frame10, text="Retour", command=arriere)
    endbt2.pack()
    bg_label2.pack() 
    page2.pack()

    frame10 = tkinter.Frame(page2)
    frame10.place(relx=0.1, rely=0.3, relwidth=0.15, relheight=0.1)

    frame11 = tkinter.Frame(page2)
    frame11.place(relx=0.3, rely=0.3, relwidth=0.15, relheight=0.1)

    frame12 = tkinter.Frame(page2)
    frame12.place(relx=0.5, rely=0.3, relwidth=0.15, relheight=0.1)

    frame13 = tkinter.Frame(page2)
    frame13.place(relx=0.7, rely=0.3, relwidth=0.15, relheight=0.1)

    frame14 = tkinter.Frame(page2)
    frame14.place(relx=0.5, rely=0.5, relwidth=0.15, relheight=0.1)

    bt1 = tkinter.Button(frame10, text="Active le système de nutition", command=proc1)
    bt1.pack()

    bt2 = tkinter.Button(frame11, text="Active le système de surveillance", command=proc2)
    bt2.pack()

    bt3 = tkinter.Button(frame12, text="Montrer la diffusion camera", command=proc3)
    bt3.pack()

    bt4 = tkinter.Button(frame13, text="Envoyer des notifications", command=proc4)
    bt4.pack()

    bt5 = tkinter.Button(frame14, text="Resumer de la journee", command=proc5)
    bt5.pack()
    

def arriere():
    page2.pack_forget()
    endbt.config(text= "Terminer", command=avant)
    page1.pack()

def feed():
    #while True:
        #now = datetime.now()
        #hm = now.strftime("%Y,%H")

        #if combo1.get() + combo2.get() == hm:
    launch_motor()

        #if combo3.get() + combo4.get() == hm:
            #launch_motor()

        #if combo5.get() + combo6.get() == hm:
            #launch_motor()

def Message():
    user_mail = e3.get()
    mail.ehlo()
    mail.starttls()
    mail.login('raspicodeuser123@gmail.com', 'eczvylxwcdzxorkq')
    mail.sendmail('raspicodeuser123@gmail.com',user_mail,content)
    mail.close()

def stream():
    webbrowser.open("http://192.168.2.68:5000/")

def alert_status(compte, lifo):

    now = datetime.now()

    obj_int = scale1.get()

    dt1 = now.strftime("%B %d, %Y %H")

    print(dt1)

    while True:


        if lifo.empty() == True:

            time.sleep(0.005)

            
        if lifo.empty() == False:

            print("not empty")

            obj_int = scale1.get()

            item = int(lifo.get(compte)) 

            item2 = int(obj_int)
            
            if item2 > item:

                print("losing")

            
            if item - item2 == 0:

                print("tie")

            
            if item + 0 > item2:

                print("oh no")

                Message()

                return

def diagram():
    mat.matcool()
    

#-----------------------------------------------------------------------------------------------------
#mutliprocess
def proc1():
    if __name__ == '__main__':
        p1 = Process(target=feed)
        p1.start()

def proc2():
    if __name__ == '__main__':
        p2 = Process(target=launch_alert, args=(compte, lifo))
        p2.start()

def proc3():
    if __name__ == '__main__':
        p3 = Process(target=stream)
        p3.start()

def proc4():
    if __name__ == '__main__':
        p4 = Process(target=alert_status, args=(compte, lifo))   

        p4.start()


def proc5():
    if __name__ == '__main__':
        p5 = Process(target=diagram)   

        p5.start()

#-----------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    root = tkinter.Tk()

    #root.attributes("-fullscreen", True)

    manager = MyManager()

    manager.start()
    
    compte = int(compte)

    lifo = manager.LifoQueue()

    q1 = queue.Queue()

    item = 0

    item2 = 0

    mail = smtplib.SMTP('smtp.gmail.com',587)

#---------------------------------------------------------------
    #pages
    page1 = tkinter.Frame(root)
    page1.pack()

    page2 = tkinter.Frame(root)
#---------------------------------------------------------------

#---------------------------------------------------------------
    #arriere plan
    bg_img = tkinter.PhotoImage(file=r"/home/pi/Downloads/84248.png")
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
    obj_int = tkinter.IntVar()

    scale1 = tkinter.Entry(frame8,textvariable= obj_int)
    scale1.pack()
#---------------------------------------------------------------

#Page2


    root.mainloop()