import random

import tkinter as tk
from tkinter import *
from tkinter import messagebox

#Start the game - dialog box
win = tk.Tk()

win.option_add("*Button.Foreground", "white")
win.option_add("*Button.Background", "blue")

win.title("Bingo")
win.geometry("400x200")
win.resizable(0, 0)

back = tk.Frame(master=win, bg='black', highlightbackground="green", highlightcolor="green", highlightthickness=1, bd=0)
back.pack_propagate(0)  # Don't allow the widgets inside to determine the frame's width / height
back.pack(fill=tk.BOTH, expand=1)  # Expand the frame to fill the root window

tk.Label(master=back,text="\n\nBINGO!\n", bg="black", fg="green").pack()
rules="    >> Create your 5x5 Bingo Grid    \n     >> Try to cross 5 rows and/or columns before your opponent     \n      >> You can only enter one number of choice at a time    \n"
tk.Label(master=back,text=rules,bg="black",fg="yellow").pack()
confirmation="   Are you ready?   \n"
tk.Label(master=back,text=confirmation, bg="black", fg="red").pack()

def close_window():
    win.destroy()

action = Button (master = back, text = "YES", command = close_window)
action.pack()

win.mainloop()

# Bingo Game banner
def banner():
	print("""
     ________    _______________
    |   ___  \\  /              /
    |  |   \\  |/              /\\
    |  |   |  |__  ___     __/ _\\____   ______
    |  |__/  /|  |/   \\   |  |/  ____\\ /  __  \\
    |   __  < |  |     \\  |  |  |     |  |  |  |
    |  |  \\  \\|  |  |\\  \\ |  |  |  ___|  |  |  |
    |  |   |  |  |  | \\  \\|  |  | /_  |  |  |  |
    |  |___/  |  |  |  \\     |  |__/  |  |__|  |
    |________/|__|\\_|  /\\___/ \\______/\\\\______/
      /               /\\               \\
     /______GAME_____/OF\\____NUMBERS____\\
""")

# Create the User's Bingo Grid
def userGrid():
    x = []
    errCount = 0
    while(1):
        if(errCount == 4):
    	    print("""
	    	AM I A JOKE TO YOU? 
	    Common! Gather your senses!
	    """)
    	    errCount = 0
        u = input("    ")
        if u in ['a','A']:
        	x = compGrid()
        	errCount = 0
        	return(x)
        if u.isnumeric():
            n = int(u)
        else:
            print("    Please! Enter an integer in range of 1 to 25.")
            errCount+=1
            continue
        if n not in range(1,26):
            print("    LOL! The range is 1 to 25. Try again!")
            errCount+=1
            continue
        if n in x:
            print("    You have alrady added {0} to your grid".format(n))
            errCount+=1
            continue
        x = x + [n]
        if len(x) == 25:
            return(x)

# Create the Computer's Bingo Grid
def compGrid():
    y = random.sample(range(1,26),25)
    return(y)

# Modify by User's choice
def modifyByUserChoice(x,y,n):
    e = x.index(n)
    x[e] = "X"
    e = y.index(n)
    y[e] = "X"
    return(x,y)

# Modify by Computer's random choice
def modifyByCompRandChoice(x,y):
    while(1):
        n = random.choice(y)
        if(n == "X"):
            continue
        e = y.index(n)
        y[e] = "X"
        e = x.index(n)
        x[e] = "X"
        return(x,y,n)

# Modify by Computer's logical choice
def modifyByCompLogChoice(x,y):
    r = [0,0,0,0,0]
    c = [0,0,0,0,0]
    n = 0
    for i in range(0,25,5):
        for j in range(i,i+5):
            if y[j] == "X":
                r[int(i/5)] = r[int(i/5)] + 1
    for i in range(5):
        for j in range(i,i+20,5):
            if y[j] == "X":
                c[i] = c[i] + 1

    sorted_r = sorted(r)
    sorted_c = sorted(c)

    for i in range(4,-1,-1):
        if sorted_r[i] == 5:
            continue
        m_r = sorted_r[i]
        break
    for i in range(4,-1,-1):
        if sorted_c[i] == 5:
            continue
        m_c = sorted_c[i]
        break

    r_i = r.index(m_r)
    c_i = c.index(m_c)

    if m_r > m_c:
        for i in range(r_i,r_i+5):
            if y[i] == "X":
                continue
            n = y[i]
            y[i] = "X"
            break
    if m_r < m_c:
    	for i in range(c_i,c_i+20,5):
            if y[i] == "X":
                continue
            n = y[i]
            y[i] = "X"
            break
    if m_r == m_c:
        for i in range(r_i,r_i+5):
            if y[i] == "X":
                continue
            n = y[i]
            y[i] = "X"
            break
    if n == 0:
    	for i in range(c_i,c_i+20,5):
            if y[i] == "X":
                continue
            n = y[i]
            y[i] = "X"
            break
    if n == 0:
    	x,y,n = modifyByCompRandChoice(x,y)
    	return(x,y,n)
    e = x.index(n)
    x[e] = "X"
    return(x,y,n)

# Display Bingo Grid
def displayGrid(g):
    for i in range(0,25,5):
        for j in range(i,i+5):
            if(j==i):
                print("    ",end="")
            else:
                print(" ",end="")
            if g[j] in range(1,10) or g[j] == "X":
                print("" , g[j],end=" ")
            else:
                print(g[j],end=" ")
        print("\n")

# Check the current ingame status of the Grids
def checkStatus(x,y,statX,statY,cx,rx,cy,ry):
    for i in range(0,25,5):
        if x[i] == x[i+1] == x[i+2] == x[i+3] == x[i+4]:
            if i not in rx:
                statX = statX + 1
                rx = rx + [i]
    for i in range(5):
        if x[i] == x[i+5] == x[i+10] == x[i+15] == x[i+20]:
            if i not in cx:
                statX = statX + 1
                cx = cx + [i]
    for i in range(0,25,5):
        if y[i] == y[i+1] == y[i+2] == y[i+3] == y[i+4]:
            if i not in ry:
                statY = statY + 1
                ry = ry + [i]
    for i in range(5):
        if y[i] == y[i+5] == y[i+10] == y[i+15] == y[i+20]:
            if i not in cy:
                statY = statY + 1
                cy = cy + [i]
    return(statX,statY,cx,rx,cy,ry)

# main program
if __name__=="__main__":
    global finalResult, name
    banner()
    name = input("    Enter your name: ").upper()
    print("\n  Hello " + name + "! Welcome to Bingo.")
    while(1):
    	gridType = input("\n  Create grid automatically or manually? (Enter 'a' for automatic or 'm' for manual): ")
    	if (gridType not in ['a','A','m','M']): 
    		print("  NOTE: Press 'a' for automatic or 'm' for manual.")
    		continue
    	if gridType in ['a','A']: 
    		x = compGrid()
    		break
    	else: 
		    print("\n  Let's create your Bingo Grid!\n\n  Enter your 5 rows sequentially (You can still create grid automatically- Type 'a' and press ENTER, anytime.):\n")
		    x = userGrid()
		    break
    y = compGrid()
    statX = 0
    statY = 0
    cx = []
    rx = []
    cy = []
    ry = []
    print("\n  Your Bingo Grid is:\n")
    displayGrid(x)
    print("\n  Computer has also created its Bingo Grid! Get ready!\n\n  Let's start with you then!\n")
    while(1):
        u = input("\n  Enter the number of your choice: ")
        if u.isnumeric():
            n = int(u)
        else:
            print("\n  Please! Enter an integer in range of 1 to 25.\n")
            continue
        if n not in range(1,26):
            print("\n  LOL! The range is 1 to 25. Try again!\n")
            continue
        if n not in x:
            print("\n  {0} is ALREADY CUT from your grid. See your grid above.\n".format(n))
            continue
        x,y = modifyByUserChoice(x,y,n)
        print("\n  Your modified Grid:\n")
        displayGrid(x)
        statX,statY,cx,rx,cy,ry = checkStatus(x,y,statX,statY,cx,rx,cy,ry)
        if statX >= 5:
            finalResult = 'u'
            print("\n  Congratulations " + name + "! YOU WON!\n")
            print("\n  Final status of Computer's Grid:\n")
            displayGrid(y)
            break
        if statY >= 5:
            finalResult = "c"
            print("\n  BINGO " + name + "! YOU ARE DEFEATED! BETTER LUCK NEXT TIME.\n")
            print("\n  Final status of Computer's Grid:\n")
            displayGrid(y)
            break
        x,y,n = modifyByCompLogChoice(x,y)
        print("\n  Computer chose {0}. So, your modified Grid is:\n".format(n))
        displayGrid(x)
        statX,statY,cx,rx,cy,ry = checkStatus(x,y,statX,statY,cx,rx,cy,ry)
        if statY >= 5:
            finalResult = 'c'
            print("\n  BINGO " + name + "! YOU ARE DEFEATED! BETTER LUCK NEXT TIME.\n")
            print("\n  Final status of Computer's Grid:\n")
            displayGrid(y)
            break
        if statX >= 5:
            finalResult = 'u'
            print("\n  Congratulations " + name + "! YOU WON!\n")
            print("\n  Final status of Computer's Grid:\n")
            displayGrid(y)
            break

# End the game - dialog box
win = tk.Tk()

win.option_add("*Button.Foreground", "white")
win.option_add("*Button.Background", "blue")

win.title("Bingo")
win.geometry("300x150")
win.resizable(0,0)

back = tk.Frame(master=win,bg='black', highlightbackground="yellow", highlightcolor="yellow", highlightthickness=1, bd=0)
back.pack_propagate(0)
back.pack(fill=tk.BOTH, expand=1)

if(finalResult == 'u'):
	frtext = "\nBINGO " + name + "! YOU LOST!\n"
elif(finalResult == 'c'):
	frtext = "\nBINGO " + name + "! YOU WON!\n"
else:
	frtext = "\nBINGO " + name + "!\n"

tk.Label(master=back,text=frtext, bg="black", fg="yellow").pack()
confirmEnd="    Thank you! Hope you enjoyed the game.    \n    See the results in the end.    \n"
tk.Label(master=back,text=confirmEnd,bg="black",fg="green").pack()

def close_window():
    win.destroy()

action = Button (master = back, text = "Exit", command = close_window)
action.pack()

win.mainloop()
