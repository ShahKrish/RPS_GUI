from tkinter import *
import tkinter
import random

window = Tk()
window.title("RPS")
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))



#length=1300 height=565

choices = ('rock', 'paper', 'scissor')
human = ""
computer = ""
HUMAN_SCORE = 0
COMPUTER_SCORE = 0

def rock():
    global human
    global computer
    human = "rock"
    print(human)
    computer = random.choice(choices)


    print(computer)
    RPS()


def paper():
    global human
    global computer
    human = "paper"
    print(human)
    computer = random.choice(choices)
    print(computer)
    RPS()


def scissor():
    global human
    global computer
    human = "scissor"
    print(human)
    computer = random.choice(choices)
    print(computer)
    RPS()



rock_img = PhotoImage(file="Rock.png")
paper_img = PhotoImage(file="Paper.png")
scissor_img = PhotoImage(file="Scissor.png")

#canvas = Canvas(window, width=1300, height=565)
#canvas.pack()

#divider = canvas.create_line(768,0,768,864)

Rock = Button(window, image=rock_img, command=rock, height=230, width=230)
Rock.place(x=25, y=200)

Paper = Button(window, image=paper_img, command=paper, height=230, width=230)
Paper.place(x=525, y=200)

Scissor = Button(window, image=scissor_img, command=scissor, height=230, width=230)
Scissor.place(x=275, y=500)

label_1 = Label(window, text="COMPUTER CHOSE:", font=("Courier", 35))
label_1.place(x=900, y=125)

label_2 = Label(window, text="YOU CHOSE:", font=("Courier", 35))
label_2.place(x=258, y=125)

label_win = Label(window, text="YOU WON!", font=("Courier", 35))


label_lost= Label(window, text="YOU LOST", font=("Courier", 35))

label_again = Label(window, text="CHOOSE AGAIN", font=("Courier", 35))


def win():
    global HUMAN_SCORE
    global label_win
    global label_lost
    global label_again
    label_again.destroy()
    label_lost.destroy()
    label_win.destroy()
    label_win = Label(window, text="YOU WON!", font=("Courier", 35))
    label_win.place(x=980, y=480)
    HUMAN_SCORE = HUMAN_SCORE+1

def lost():
    global COMPUTER_SCORE
    global label_win
    global label_lost
    global label_again
    label_again.destroy()
    label_lost.destroy()
    label_win.destroy()
    label_lost = Label(window, text="YOU LOST", font=("Courier", 35))
    label_lost.place(x=980, y=480)
    COMPUTER_SCORE = COMPUTER_SCORE + 1

def again():
    global label_win
    global label_lost
    global label_again
    label_again.destroy()
    label_lost.destroy()
    label_win.destroy()
    label_again = Label(window, text="CHOOSE AGAIN", font=("Courier", 35))
    label_again.place(x=922, y=480)



def RPS():

    if human == "rock" and computer == "rock":
        again()
    elif human == "rock" and computer == "paper":
        lost()
    elif human == "rock" and computer == "scissor":
        win()
    elif human == "paper" and computer == "paper":
        again()
    elif human == "paper" and computer == "scissor":
        lost()
    elif human == "paper" and computer == "rock":
        win()
    elif human == "scissor" and computer == "scissor":
        again()
    elif human == "scissor" and computer == "rock":
        lost()
    elif human == "scissor" and computer == "paper":
        win()

    if computer == "rock":
        Rock = Button(window, image=rock_img, command=rock, height=230, width=230)
        Rock.place(x=975, y=200)
    elif computer == "paper":
        Paper = Button(window, image=paper_img, command=paper, height=230, width=230)
        Paper.place(x=975, y=200)
    else:
        Scissor = Button(window, image=scissor_img, command=scissor, height=230, width=230)
        Scissor.place(x=975, y=200)


window.mainloop()
