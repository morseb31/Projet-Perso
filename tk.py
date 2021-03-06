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
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasAgg, FigureCanvasTkAgg, NavigationToolbar2Tk
import re

#-----------------------------------------------------------------------------------------------------
# functions

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)

def led():
    setup()

    global compte
    global last_line

    with open("comptage") as file:
        
        for last_line in file:

            pass

    compte = int(last_line)

    if compte < int(scale1.get()):
        GPIO.output(22, GPIO.HIGH)

    if compte == int(scale1.get()):
        GPIO.output(22, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)

    if compte > int(scale1.get()):
       GPIO.output(24, GPIO.LOW)    
       GPIO.output(26, GPIO.HIGH)
    
    else:
        time.sleep(0.05)
     
def avant():
    page1.pack_forget()

    page2.pack()

    bg_label2.pack() 

    frame10.place(relx=0.1, rely=0.3, relwidth=0.15, relheight=0.1)

    frame11.place(relx=0.3, rely=0.3, relwidth=0.15, relheight=0.1)

    frame12.place(relx=0.5, rely=0.3, relwidth=0.15, relheight=0.1)

    frame13.place(relx=0.7, rely=0.3, relwidth=0.15, relheight=0.1)

    frame14.place(relx=0.5, rely=0.5, relwidth=0.15, relheight=0.1)

    frame16.place(relx=0.2, rely=0.6, relwidth=0.15, relheight=0.3)

    frame17.place(relx=0.4, rely=0.1, relwidth=0.25, relheight=0.15)

    frame18.place(relx=0.9, rely=0.9, relwidth=0.15, relheight=0.1)

    lbi.pack()

    bt1.pack()

    bt2.pack()

    bt3.pack()

    bt4.pack()

    bt5.pack()

    btback.pack()

    lbra.pack()

def config1():
    bt1.config(bg="red", command=return1)

def config2():
    bt2.config(bg="red", command=return2)

def config3():
    bt3.config(bg="red", command=return3)

def config4():
    bt4.config(bg="red", command=return4)

def return1():
    bt1.config(bg="beige", command=proc1)

    p1.terminate()
    p1.join()

def return2():
    bt2.config(bg="beige", command=proc2)

    p2.terminate()
    p2.join()

def return3():
    bt3.config(bg="beige", command=proc3)

    p3.terminate()
    p3.join()

def return4():
    bt4.config(bg="beige", command=proc4)

    p4.terminate()
    p4.join()

def arriere():
    page2.pack_forget()
    page1.pack()

def feed():

    while True:
        now = datetime.now()
        hm = now.strftime("%H" + "%M")

        if combo1.get() + combo2.get() == hm:

            texte = "?? " + hm + " heure" + " votre chien a ??t?? nourrit"

            with open("resume","a") as f:
                f.write(texte)
                f.close
            
            launch_motor()

        if combo3.get() + combo4.get() == hm:

            texte = "?? " + hm + " heure" + " votre chien a ??t?? nourrit"

            with open("resume","a") as f:
                f.write(texte)
                f.close

            launch_motor()

        if combo5.get() + combo6.get() == hm:

            texte = "?? " + hm + " heure" + " votre chien a ??t?? nourrit"

            with open("resume","a") as f:
                f.write(texte)
                f.close

            launch_motor()

def Message():
    mail.ehlo()
    mail.starttls()
    mail.login('raspicodeuser123@gmail.com', 'eczvylxwcdzxorkq')
    mail.sendmail(from_addr="raspicodeuser123@gmail.com",to_addrs=e3.get(), msg="Bonjour " + e1.get() + " " + e2.get() + " semble avoir depasser votre objectif de bruits. Veuiller verifier la diffusion en direct pour assurer sa securite.")
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

            led()

            time.sleep(0.005)

            
        if lifo.empty() == False:

            led()

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

    a_file = open("resume")

    res = a_file.readlines()

    print(res)

    lbra.config(text=res)

    patron1 = re.compile("1 ")

    patron2 = re.compile("2 ")

    patron3 = re.compile("3 ")

    patron4 = re.compile("4 ")

    patron5 = re.compile("5 ")

    patron6 = re.compile("6 ")

    patron7 = re.compile("7 ")

    patron8 = re.compile("8 ")

    patron9 = re.compile("9 ")

    patron10 = re.compile("10")

    patron11 = re.compile("11")

    patron12 = re.compile("12")

    patron13 = re.compile("13")

    patron14 = re.compile("14")

    patron15 = re.compile("15")

    patron16 = re.compile("16")

    patron17 = re.compile("17")

    patron18 = re.compile("18")

    patron19 = re.compile("19")

    patron20 = re.compile("20")

    patron21 = re.compile("21")

    patron22 = re.compile("22")

    patron23 = re.compile("23")

    patron24 = re.compile("24")

    one = 0

    two = 0

    three = 0

    four = 0

    five = 0

    six = 0

    seven = 0

    eight = 0

    nine = 0

    ten = 0

    eleven = 0

    twelve = 0

    thirteen= 0

    fourteen = 0

    fifteen = 0

    sixteen = 0

    seventeen = 0

    eighteen = 0

    nineteen = 0

    twenty = 0

    twentyone = 0

    twentytwo = 0

    twentythree = 0

    twentyfour = 0


    for line in open("sdsn.results"):
        for match in re.finditer(patron1, line):
            one += 1

    for line in open("sdsn.results"):
        for match in re.finditer(patron2, line):
            two += 1

    for line in open("sdsn.results"):
        for match in re.finditer(patron3, line):
            three += 1

    for line in open("sdsn.results"):
        for match in re.finditer(patron4, line):
            four += 1
    
    for line in open("sdsn.results"):
        for match in re.finditer(patron5, line):
            five += 1
    
    for line in open("sdsn.results"):
        for match in re.finditer(patron6, line):
            six += 1
    
    for line in open("sdsn.results"):
        for match in re.finditer(patron7, line):
            seven += 1
    
    for line in open("sdsn.results"):
        for match in re.finditer(patron8, line):
            eight += 1
    
    for line in open("sdsn.results"):
        for match in re.finditer(patron9, line):
            nine += 1
    
    for line in open("sdsn.results"):
        for match in re.finditer(patron10, line):
            ten += 1
    
    for line in open("sdsn.results"):
        for match in re.finditer(patron11, line):
            eleven += 1
    
    for line in open("sdsn.results"):
        for match in re.finditer(patron12, line):
            twelve += 1
    
    for line in open("sdsn.results"):
        for match in re.finditer(patron13, line):
            thirteen += 1
    
    for line in open("sdsn.results"):
        for match in re.finditer(patron14, line):
            fourteen += 1
    
    for line in open("sdsn.results"):
        for match in re.finditer(patron15, line):
            fifteen += 1
    
    for line in open("sdsn.results"):
        for match in re.finditer(patron16, line):
            sixteen += 1
    
    for line in open("sdsn.results"):
        for match in re.finditer(patron17, line):
            seventeen += 1
    
    for line in open("sdsn.results"):
        for match in re.finditer(patron18, line):
            eighteen += 1
    
    for line in open("sdsn.results"):
        for match in re.finditer(patron19, line):
            nineteen += 1
    
    for line in open("sdsn.results"):
        for match in re.finditer(patron20, line):
            twenty += 1

    for line in open("sdsn.results"):
        for match in re.finditer(patron21, line):
            twentyone += 1

    for line in open("sdsn.results"):
        for match in re.finditer(patron22, line):
            twentytwo += 1
    
    for line in open("sdsn.results"):
        for match in re.finditer(patron23, line):
            twentythree += 1
    
    for line in open("sdsn.results"):
        for match in re.finditer(patron24, line):
            twentyfour += 1

    plt.plot([one, two, three, four, five, six, seven, eight, nine , ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, twentyone, twentytwo, twentythree, twentyfour])
    plt.ylabel('Heure')
    plt.xlabel('Nombre de bruits')
    plt.show()

#-----------------------------------------------------------------------------------------------------
#mutliprocess
def proc1():
    if __name__ == '__main__':
        config1()
        p1.start()

def proc2():
    if __name__ == '__main__':
        config2()
        p2.start()

def proc3():
    if __name__ == '__main__':
        config3()
        p3.start()

def proc4():
    if __name__ == '__main__':
        config4()
        p4.start()

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

    last_line = 0

    p1 = Process(target=feed)

    p2 = Process(target=launch_alert, args=(compte, lifo))

    p3 = Process(target=stream)

    p4 = Process(target=alert_status, args=(compte, lifo))   

    
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
    frame1 = tkinter.Frame(page1, bg="#69537d")
    frame1.place(relx=0.425, rely=0.05, relwidth=0.15, relheight=0.05)

    frame2 = tkinter.Frame(page1, bg="#69537d")
    frame2.place(relx=0.425, rely=0.10, relwidth=0.15, relheight=0.05)

    frame3 = tkinter.Frame(page1, bg="#69537d")
    frame3.place(relx=0.425, rely=0.20, relwidth=0.15, relheight=0.05)

    frame4 = tkinter.Frame(page1, bg="#69537d")
    frame4.place(relx=0.425, rely=0.30, relwidth=0.15, relheight=0.05)

    frame5 = tkinter.Frame(page1, bg="#69537d")
    frame5.place(relx=0.2, rely=0.40, relwidth=0.15, relheight=0.1)

    frame6 = tkinter.Frame(page1, bg="#69537d")
    frame6.place(relx=0.425, rely=0.40, relwidth=0.15, relheight=0.1)

    frame7 = tkinter.Frame(page1, bg="#69537d")
    frame7.place(relx=0.65, rely=0.40, relwidth=0.15, relheight=0.1)

    frame8 = tkinter.Frame(page1, bg="#69537d")
    frame8.place(relx=0.425, rely=0.50, relwidth=0.15, relheight=0.1)

    frame9 = tkinter.Frame(page1, bg="#69537d")
    frame9.place(relx=0.9, rely=0.9, relwidth=0.15, relheight=0.1)

    frame16 = tkinter.Frame(page2, bg="#69537d")
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

    lbra = tkinter.Label(frame16, text="hi")
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
    bg_label2 = tkinter.Label(page2, image=bg_img)

    frame10 = tkinter.Frame(page2, bg="#69537d")

    frame11 = tkinter.Frame(page2, bg="#69537d")

    frame12 = tkinter.Frame(page2, bg="#69537d")

    frame13 = tkinter.Frame(page2, bg="#69537d")

    frame14 = tkinter.Frame(page2, bg="#69537d")

    frame16 = tkinter.Frame(page2, bg="#69537d")

    frame17 = tkinter.Frame(page2, bg="#69537d")

    frame18 = tkinter.Frame(page2, bg="#69537d")

    frame19 = tkinter.Frame(page2, bg="#69537d")

    lbi = tkinter.Label(frame17, text="Bienvenue aux configurations de l'app." + "\n" + "Veillez choisir les systeme que vous voulez activer.", bg="beige")
    lbi.config(font=("Ariel, 12"))

    bt1 = tkinter.Button(frame10, text="Active le syst??me de nutrition", bg="beige", command=proc1)
  
    bt2 = tkinter.Button(frame11, text="Active le syst??me de surveillance", bg="beige", command=proc2)

    bt3 = tkinter.Button(frame12, text="Montrer la diffusion camera", bg="beige", command=proc3)

    bt4 = tkinter.Button(frame13, text="Envoyer des notifications", bg="beige", command=proc4)

    bt5 = tkinter.Button(frame14, text="Resumer de la journee", bg="beige", command=diagram)
    
    btback = tkinter.Button(frame18, text="Arriere", bg="beige", command= arriere)

    lbras = tkinter.Label(frame19, text='Resumer de la journee')

    lbra = tkinter.Label(frame16, text="En attente de vos resultats...")

    root.mainloop()