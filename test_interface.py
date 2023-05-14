# Créé par antonin.nadaud, le 05/04/2023 en Python 3.7
from tkinter import *
from tkinter import messagebox
import random
import os
#pip install pyenchant
import enchant
dicoVerification = enchant.Dict("fr_FR")


try:
    import customtkinter
except ImportError:
    print("Vous devez installer customtkinter")


customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

root.geometry("400x400")

root.attributes('-fullscreen', True)

def on_focus_in(entry):
    if entry.cget('state') == 'disabled':
        entry.configure(state='normal')
        entry.delete(0, 'end')

def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')


class devtools:

    def __init__(self,root,x,y):



        self.frame = customtkinter.CTkFrame(master=root,
                                       width=250,
                                       height=1200,
                                       corner_radius=10)
        self.frame.place(x=x, y=y)



        label = customtkinter.CTkLabel(master=self.frame,
                                       text="DEVS TOOLS",
                                       width=140,
                                       height=25,
                                       corner_radius=8, font=("Arial", 25))
        label.place(x=30 + x, y=20 + y)




        self.var = StringVar()

        label = customtkinter.CTkLabel(master=self.frame,
                                       textvariable=self.var,
                                       width=120,
                                       height=25,
                                       corner_radius=8, font=("Arial", 12))


        self.var.set("Taille max 10")

        label.place(x=65 + x, y=80 + y)

        slider = customtkinter.CTkSlider(master=self.frame,
                                         width=160,
                                         height=16,
                                         border_width=5,
                                         command=self.slider_event)
        slider.place(x=45 + x, y=110 + y)


        button = customtkinter.CTkButton(master=self.frame, text="Actualiser")

        button.place(x=55+x,y=220+y)

        buttonStart = customtkinter.CTkButton(master=self.frame, text="Commencer")

        buttonStart.place(x=55+x,y=290+y)

        entry = customtkinter.CTkEntry(master=self.frame)
        entry.place(x=55+x,y=160 + y)
        entry.insert(0, "Nouveau mot")
        entry.configure(state='disabled')
        entry.bind('<Button-1>', lambda x: on_focus_in(entry))
        entry.bind('<FocusOut>', lambda x: on_focus_out(entry, 'Nouveau mot'))

        buttonStart.bind("<Button-1>", lambda e: Body.start(root))



    def slider_event(self,value):
        tmax = 20
        self.var.set(f"Taille max {round(value * tmax)}")


class TextTransition:

    def __init__(self, canvas, x= 700, y= 330, text = "Test", start= 0):

        self.canvas = canvas

        self.delay = start
        self.canvas_text = canvas.create_text(x, y, text='', anchor=NW, fill='white', font=("Arial", 32))
        test_string = text
        #Time delay between chars, in milliseconds
        delta = 35
        for i in range(len(test_string) + 1):
            s = test_string[:i]
            update_text = lambda s=s: canvas.itemconfigure(self.canvas_text, text=s)
            canvas.after(self.delay, update_text)
            self.delay += delta

    def destroy(self, destoyTps = 500, callback = lambda : ...):

        self.canvas.after(destoyTps+ self.delay, lambda : self.canvas.delete(self.canvas_text))

    @staticmethod
    def delay(canvas, temps, callback):

        canvas.after(temps, callback)



class Start:

    def __init__(self, canvas):

        self.canvas = canvas
        TextTransition(canvas, text= "Bienvenu dans le jeu du motus", x = 550).destroy()

        temps = 35 * len("Bienvenu dans le jeu du motus") + 500
        TextTransition(canvas, text= "Vous proposez un mot dans un délai maximal de 16 seconde.", x = 200, start = temps).destroy()

        temps += len("Vous proposez un mot dans un délai maximal de 16 seconde.") * 35 + 500

        TextTransition(canvas, text= "Le mot doit contenir le bon nombre de lettres", x = 350, start = temps).destroy()

        temps +=  len("Le mot doit contenir le bon nombre de lettres") * 35 + 500

        TextTransition(canvas, text= "et être correctement orthographié, sinon il est refusé.", x = 250, start = temps).destroy()

        temps += len("et être correctement orthographié, sinon il est refusé.") * 35 + 500

        TextTransition(canvas, text= "Commençons !", x = 700, start = temps).destroy()

        temps += len("Commençons !") * 35 + 500

        TextTransition(canvas, text= "trois", x = 700, start = temps).destroy()

        temps += len("trois") * 35 + 500

        TextTransition(canvas, text= "deux", x = 700, start = temps).destroy()

        temps += len("deux") * 35 + 500

        TextTransition(canvas, text= "un", x = 700, start = temps).destroy()

        temps += len("un") * 35 + 500

        TextTransition(canvas, text= "C'est parti !", x = 700, start = temps).destroy()

        temps += len("C'est parti !") * 35 + 500

        TextTransition.delay(canvas, temps, lambda : Game(canvas))


class Table:

    def __init__(self, canvas, word):

        self.canvas = canvas

        startCord = (250,200)

        self.indiceStart = canvas.create_rectangle(0,0,0,0)

        for i in range(1,len(word) + 1):

            for line in range(6):

                if i == 1 and not line:
                    canvas.create_rectangle(startCord[0] + 50 * i,startCord[1] + 50 * line,30 + startCord[0] + 50 * i + 21,startCord[1] + 50 * line + 50, fill="#40bbdc", outline="white", width=1)
                    canvas.create_text(startCord[0] + 50 * i + 25, startCord[1] + 50 * line + 25, text=word[0], font=("Arial", 18), fill="white")
                elif not line:
                    canvas.create_rectangle(startCord[0] + 50 * i,startCord[1] + 50 * line,30 + startCord[0] + 50 * i + 21,startCord[1] + 50 * line + 50, fill="#40bbdc", outline="white", width=1)
                    canvas.create_text(startCord[0] + 50 * i + 25, startCord[1] + 50 * line + 22, text=".", font=("Arial", 18), fill="white")
                else:
                    canvas.create_rectangle(startCord[0] + 50 * i,startCord[1] + 50 * line,30 + startCord[0] + 50 * i + 21,startCord[1] + 50 * line + 50, fill="#40bbdc", outline="white", width=1)
                    canvas.create_text(startCord[0] + 50 * i + 25, startCord[1] + 50 * line + 22, text="", font=("Arial", 18), fill="white")

        self.wordcount = 0
    def addWord(self, word , entry):

        if self.wordcount > 10:
            return

        for i in range(len(word)):
            if word[i] == entry[i]:
                self.canvas.itemconfig(self.indiceStart + 2 + self.wordcount + 12 * i, text=entry[i])
                self.canvas.itemconfig(self.indiceStart + 1 + self.wordcount + 12 * i, fill="red")
            elif entry[i] in list(word):
                self.canvas.itemconfig(self.indiceStart + 2 + self.wordcount + 12 * i, text=entry[i], fill="black")
                self.canvas.itemconfig(self.indiceStart + 1 + self.wordcount + 12 * i, fill="yellow")
            else:
                self.canvas.itemconfig(self.indiceStart + 2 + self.wordcount + 12 * i, text=entry[i])

        self.wordcount += 2


class Print:

    @staticmethod
    def errorShow(msg):

        messagebox.showwarning("Except error", msg)

    @staticmethod
    def normalShow(msg):

        messagebox.showinfo("Info", msg)



class Game:

    def __init__(self, canvas):

        global root
        word = Game.choose_rand_word().encode("windows-1252").decode("utf-8")[:-1]

        filter =  [" " , ""]
        resultat = ""

        for lettre in word:

            if lettre not in filter:
                print(lettre)
                resultat += lettre

        word = resultat



        self.word = word

        self.entry = customtkinter.CTkEntry(master=root,width=root.winfo_screenwidth() - 320, height=40)
        self.entry.place(x=300, y=root.winfo_screenheight() - 80)

        print(word)
        self.table = Table(canvas, word)
        root.bind('<Return>', self.click_event)

    def click_event(self, event):

        global dicoVerification

        if len(self.word) == len(self.entry.get()) and dicoVerification.check(self.entry.get()):
            Print.normalShow("Clicked")
            self.table.addWord(self.word, self.entry.get())
        elif not dicoVerification.check(self.entry.get()):

            suggestion = dicoVerification.suggest(self.entry.get())
            
            
            finalString = "  "
            for i in range(min(5,len(suggestion))):
                finalString += " " +  str(suggestion[i]) + " "

            Print.errorShow(f"Le mot doit être correctement orhtographié pas comme vous l'avez fait essayé plutôt avec " + finalString)
        else:
            Print.errorShow(f"Le mot doit être de {len(self.word)} non pas de {len(self.entry.get())} commme vous l'avez entrez ")







    @staticmethod
    def choose_rand_word():

        #on cherche un mot aleatoirement

        with open("./data/word.txt") as f:


            listeDeMot = f.readlines()

        word = listeDeMot[random.randint(1, len(listeDeMot) - 1)]

        print(len(word))

        return word if len(word) > 3 else Game.choose_rand_word()





class Body:


    @staticmethod
    def start(root):

        canvas = customtkinter.CTkCanvas(master=root, bg="#333333", bd=0, highlightthickness=0, relief='ridge')
        canvas.place(x=300, y=10, width=root.winfo_screenwidth() - 320, height= root.winfo_screenheight() - 120)


        Game(canvas)





devtools(root,0,0)



root.mainloop()

root.mainloop()
