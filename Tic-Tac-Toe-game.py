from tkinter import*
from tkinter import messagebox

#display
root=Tk()
root.title("Tic Tac Toe")
root.iconbitmap("Tic-Tac-Toe-\logo.ico")

#start to true
clicked=True
count=0

def disable_all_buttons():
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)
#check to see if someone won

def check_if_won():
    global winner
    winner=False

#Turn to win X

    if button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X":
        button1.config(bg="blue",fg="white")
        button2.config(bg="blue",fg="white")
        button3.config(bg="blue",fg="white")
        winner=True
        messagebox.showinfo("Tic Tae Tow"," X wins")
        disable_all_buttons()
    elif button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X":
        button4.config(bg="blue",fg="white")
        button5.config(bg="blue",fg="white")
        button6.config(bg="blue",fg="white")
        winner=True
        messagebox.showinfo("Tic Tac Toe"," X wins")
        disable_all_buttons()
    elif button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X":
        button7.config(bg="blue",fg="white")
        button8.config(bg="blue",fg="white")
        button9.config(bg="blue",fg="white")
        winner=True
        messagebox.showinfo("Tic Tae Tow"," X wins")
        disable_all_buttons()
    elif button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X":
        button1.config(bg="blue",fg="white")
        button4.config(bg="blue",fg="white")
        button7.config(bg="blue",fg="white")
        winner=True
        messagebox.showinfo("Tic Tae Tow"," X wins")
        disable_all_buttons()
    elif button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X":
        button2.config(bg="blue",fg="white")
        button5.config(bg="blue",fg="white")
        button8.config(bg="blue",fg="white")
        winner=True
        messagebox.showinfo("Tic Tae Tow"," X wins")
        disable_all_buttons()
    elif button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X":
        button3.config(bg="blue",fg="white")
        button6.config(bg="blue",fg="white")
        button9.config(bg="blue", fg="white")
        winner=True
        messagebox.showinfo("Tic Tae Tow"," X wins")
        disable_all_buttons()
    elif button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X":
        button1.config(bg="blue",fg="white")
        button5.config(bg="blue",fg="white")
        button9.config(bg="blue",fg="white")
        winner=True
        messagebox.showinfo("Tic Tae Tow"," X wins")
        disable_all_buttons()
    elif button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X":
        button3.config(bg="blue",fg="white")
        button5.config(bg="blue",fg="white")
        button7.config(bg="blue",fg="white")
        winner=True
        messagebox.showinfo("Tic Tae Tow"," X wins")
        disable_all_buttons()

# Turn to win O
    elif button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O":
        button1.config(bg="red",fg="white")
        button2.config(bg="red",fg="white")
        button3.config(bg="red",fg="white")
        winner=True
        messagebox.showinfo("Tic Tae Tow"," O wins")
        disable_all_buttons()
    elif button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O":
        button4.config(bg="red",fg="white")
        button5.config(bg="red",fg="white")
        button6.config(bg="red",fg="white")
        winner=True
        messagebox.showinfo("Tic Tac Toe"," O wins")
        disable_all_buttons()
    elif button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O":
        button7.config(bg="red",fg="white")
        button8.config(bg="red",fg="white")
        button9.config(bg="red",fg="white")
        winner=True
        messagebox.showinfo("Tic Tae Tow"," O wins")
        disable_all_buttons()
    elif button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O":
        button1.config(bg="red",fg="white")
        button4.config(bg="red",fg="white")
        button7.config(bg="red",fg="white")
        winner=True
        messagebox.showinfo("Tic Tae Tow"," O wins")
        disable_all_buttons()
    elif button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O":
        button2.config(bg="red",fg="white")
        button5.config(bg="red",fg="white")
        button8.config(bg="red",fg="white")
        winner=True
        messagebox.showinfo("Tic Tae Tow"," O wins")
        disable_all_buttons()
    elif button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O":
        button3.config(bg="red",fg="white")
        button6.config(bg="red",fg="white")
        button9.config(bg="red", fg="white")
        winner=True
        messagebox.showinfo("Tic Tae Tow"," O wins")
        disable_all_buttons()
    elif button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O":
        button1.config(bg="red",fg="white") 
        button5.config(bg="red",fg="white")
        button9.config(bg="red",fg="white")
        winner=True
        messagebox.showinfo("Tic Tae Tow"," O wins")
        disable_all_buttons()
    elif button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O":
        button3.config(bg="red",fg="white")
        button5.config(bg="red",fg="white")
        button7.config(bg="red",fg="white")
        winner=True
        messagebox.showinfo("Tic Tae Tow"," O wins")
        disable_all_buttons()
     
    if count==9 and winner==False:
        messagebox.showinfo("Tic Tac Toe","It's Tie")
        disable_all_buttons()

def b_click(b):
    global clicked,count

    if b["text"]=="" and clicked==True:
        b["text"]="X"
        clicked=False
        count+=1
        check_if_won()
    elif b["text"]=="" and clicked==False:
        b["text"]="O"
        clicked=True
        count+=1
        check_if_won()
    else:
        messagebox.showerror("Tic Tac Toe","Hey The box has alreday been selected \n         Try to pick another box")

#button
button1=Button(root,text="",font=("Helvetica",17),height=3,width=6,bg="#edf7f5",command=lambda:b_click(button1))
button2=Button(root,text="",font=("Helvetica",17),height=3,width=6,bg="#edf7f5",command=lambda:b_click(button2))
button3=Button(root,text="",font=("Helvetica",17),height=3,width=6,bg="#edf7f5",command=lambda:b_click(button3))

button4=Button(root,text="",font=("Helvetica",17),height=3,width=6,bg="#edf7f5",command=lambda:b_click(button4))
button5=Button(root,text="",font=("Helvetica",17),height=3,width=6,bg="#edf7f5",command=lambda:b_click(button5))
button6=Button(root,text="",font=("Helvetica",17),height=3,width=6,bg="#edf7f5",command=lambda:b_click(button6))

button7=Button(root,text="",font=("Helvetica",17),height=3,width=6,bg="#edf7f5",command=lambda:b_click(button7))
button8=Button(root,text="",font=("Helvetica",17),height=3,width=6,bg="#edf7f5",command=lambda:b_click(button8))
button9=Button(root,text="",font=("Helvetica",17),height=3,width=6,bg="#edf7f5",command=lambda:b_click(button9))

#place on screen
button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)

button4.grid(row=1,column=0)
button5.grid(row=1,column=1)
button6.grid(row=1,column=2)

button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
















root.mainloop()