from tkinter import *
import tkinter.messagebox as tsmg
import random
def play():
    computers_choice=random.choice(x)
    if user_choice.get()==computers_choice:
        tsmg.showinfo("Result","It's a tie.")
        b=tsmg.askyesno("Play again", "Would you like to retry?")
        if b==0:
               root.destroy()
           
    elif user_choice.get()=="Rock":
        if computers_choice=="Scissors":
            tsmg.showinfo("Result","You win!!")
            b=tsmg.askyesno("Play again", "Would you like to retry?")
            if b==0:
               root.destroy()
                    
        else:
            tsmg.showinfo("Result","You loose.")
            b=tsmg.askyesno("Play again", "Would you like to retry?")
            if b==0:
               root.destroy()
                
    elif user_choice.get()=="Scissors":
        if computers_choice=="Paper":
            tsmg.showinfo("Result", "You win!!")
            b=tsmg.askyesno("Play again", "Would you like to retry?")
            if b==0:
               root.destroy()
                    
        else:
            tsmg.showinfo("Result", "You loose.")
            b=tsmg.askyesno("Play again", "Would you like to retry?")
            if b==0:
               root.destroy()
                        
    elif user_choice.get()=="Paper":
        if computers_choice=="Rock":
            tsmg.showinfo("Result", "You win!!")
            b=tsmg.askyesno("Play again", "Would you like to retry?")
            if b==0:
               root.destroy()
            
            
        else:
            tsmg.showinfo("Result", "You loose.")
            b=tsmg.askyesno("Play again", "Would you like to retry?")
            if b==0:
               root.destroy()
            
        

root=Tk()
root.title("Rock-Paper-Scissor Game")
root.geometry("700x700")
root.config(bg="bisque1")
x=["Rock","Paper","Scissors"]
label=Label(root, text="Choose an option", font="roboto 35 bold underline",bg="bisque1",fg="brown2").pack()
user_choice=StringVar()
user_choice.set("choose")
for i in x:
    rb=Radiobutton(root, text=i, variable=user_choice, font="roboto 30 bold " , value=i, fg="coral1",bg="bisque1").pack(anchor="w")
b=Button(root, text="Play",font="roboto 19 ", relief=RAISED, command=play, bg="bisque1", fg="brown2").pack()
root.mainloop()