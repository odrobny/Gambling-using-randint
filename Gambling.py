import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import Menu
import random

global rounds, p1_score, p2_score, gamble, odds, lump_sum, choice_com, luck_com, luck_p1, lbl_top, p_bar, tot_rds
p1_score = 0
p2_score = 0
rounds = 1
tot_rds = 10

gamble = random.randint(1,1000)
odds = random.randint(1,100)
lump_sum = int(gamble*odds/100)
choice_com = random.randint(1,100)
luck_com = random.randint(1,100)
luck_p1 = random.randint(1,100)

def generate_new():
    global gamble, odds, lump_sum, choice_com, luck_com, luck_p1, rounds, lbl_top, p1_score, p2_score, tot_rds
    if rounds > tot_rds:
        if  p1_score > p2_score:
            messagebox.showinfo("Game Over", "Player 1 Wins!")
        if  p1_score < p2_score:
            messagebox.showinfo("Game Over", "Computer Wins!")
        if  p1_score == p2_score:
            messagebox.showinfo("Game Over", "It's a tie! Well played.")
        quitt()
    gamble = random.randint(1,1000)
    odds = random.randint(1,100)
    lump_sum = int(gamble*odds/100)
    choice_com = random.randint(1,100)
    luck_com = random.randint(1,100)
    luck_p1 = random.randint(1,100)
    newone = "You have a "+str(odds)+"% chance of winning $ "+str(gamble)+"\nor you can take the lump sum of $ "+str(lump_sum)
    newone2 = "Round # "+str(rounds)+"/"+str(tot_rds)
    lbl_top.configure(text=newone)
    lbl_round.configure(text=newone2)
    p_bar.configure('value')

def gambleit():
    global rounds, p1_score, p2_score, gamble, odds, lump_sum, choice_com, luck_com, luck_p1
    if luck_p1<=odds:
        p1_score += gamble
        #print (p1_score, p2_score)
    if choice_com <= odds and luck_com<=odds:
        p2_score += gamble
        #print (p1_score, p2_score)
    if choice_com > odds:
        p2_score += lump_sum
        #print (p1_score, p2_score)
    s1["text"] = int(p1_score)
    s2["text"] = int(p2_score)
    rounds = rounds + 1
    p_bar['value'] = p_bar['value'] + (100/tot_rds)
    generate_new()
    return

def lumpsum():
    global rounds, p1_score, p2_score, gamble, odds, lump_sum, choice_com, luck_com, luck_p1, p_bar
    p1_score += lump_sum
    if choice_com <= odds and luck_com<=odds:
        p2_score += gamble
        #print (p1_score, p2_score)
    if choice_com > odds:
        p2_score += lump_sum
    s1["text"] = int(p1_score)
    s2["text"] = int(p2_score)
    rounds = rounds + 1
    p_bar['value'] = p_bar['value'] + (100/tot_rds)
    generate_new()
    return

def tot_rds_sv():
    global tot_rds, spin, s_win, rounds, p1_score, p2_score, s1, s2
    p1_score = 0
    p2_score = 0
    s1.configure(text = 0)
    s2.configure(text = 0)
    rounds = 1
    tmpvar = spin.get()
    #print (int(tmpvar))
    tot_rds = int(tmpvar)
    newone2 = "Round # "+str(rounds)+"/"+str(tot_rds)
    lbl_round.configure(text = newone2)
    s_win.destroy()

def cancel():
    s_win.destroy()
    return

def settings():
    global tot_rds, spin, s_win
    s_win = tk.Toplevel()
    lbl_top1 = tk.Label(s_win,text = 'Set the number of rounds you want to play',font='Serif')
    lbl_top1.grid(column=0,row=1, columnspan = 4)
    lbl_top2 = tk.Label(s_win,text = '# of rounds:',font='Serif 12 italic')
    lbl_top2.grid(column=0,row=2)
    spindefault = tk.IntVar()
    spindefault.set(tot_rds)
    spin = tk.Spinbox(s_win,from_=1, to=100, width=5, textvariable=spindefault)
    spin.grid(column=1,row=2)
    save_button = tk.Button(s_win, text="Save & Return", command=tot_rds_sv)
    save_button.grid(column=3,row=2)
    cancel_button = tk.Button(s_win, text="Cancel", command=cancel)
    cancel_button.grid(column=4,row=2)
    
    
def howtoplay():
    messagebox.showinfo("How to play the gambling game", "A gambling game where it's the user vs. the computer. Given a scenario you can either choose to try your luck and gamble or take a proportional lump sum. Goal is to end up with more $ than the computer after 10 rounds. Sound good?")
    return

def quitt():
    root.destroy()
    return

root = tk.Tk()
root.title("Gambling Game")
root.geometry('640x480')
root.rowconfigure([1,2,3,4,5,6],minsize=0, weight=100)
root.columnconfigure([0,1],minsize=0,weight=1)

menu = Menu(root)
menu_item = Menu(menu)
menu_item.add_command(label = "Settings", command = settings)
menu_item.add_command(label = "How to play", command = howtoplay)
menu.add_cascade(label="Info", menu=menu_item)
root.config(menu=menu)

lbl_round = tk.Label(root,text = ("Round # "+str(rounds)+"/"+str(tot_rds)),font='Serif 16')
lbl_round.grid(row=0, sticky=tk.W)
p_bar = Progressbar(root,length=500)
p_bar['value']= 0 
p_bar.grid(column = 0, row = 1, columnspan = 2)
lbl_top = tk.Label(root,text = ("You have a "+str(odds)+"% chance of winning $ "+str(gamble)+"\nor you can take the lump sum of $ "+str(lump_sum)), font=("Serif",18))
lbl_top.grid(row=2, columnspan = 2)
lbl_top1 = tk.Label(root,text = 'Player 1 Score:',font='Serif 16 italic')
lbl_top1.grid(column=0,row=4)
lbl_top2 = tk.Label(root,text = 'Computer Score:',font='Serif 16 italic')
lbl_top2.grid(column=0,row=5)
s1 = tk.Label(master=root,text="0",font='Serif 16')
s1.grid(row=4,column=1)
s2 = tk.Label(master=root,text="0",font='Serif 16')
s2.grid(row=5,column=1)

button1 = tk.Button(root, text="Gamble", command=gambleit)
button1.grid(column=0,row=6)
button2 = tk.Button(root, text="Lump Sum", command=lumpsum)
button2.grid(column=1,row=6)
button3 = tk.Button(root, text="Quit", command=quitt)
button3.grid(column=1,row=0, sticky = tk.E)

howtoplay()

##if __name__ == "__main__":
##    # execute only if run as a script
##    main()
