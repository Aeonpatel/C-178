from tkinter import *
import random

root = Tk()
root.title("Encapsulation")
root.geometry("400x300")
root.config(bg = "white")

score_lbl = Label(root,text="Score : ",bg="orange",fg="white")
score_lbl.pack()

lbl_color = Label(root, font = ("Comic Sans MS", 20, "bold"), bg = "white")
lbl_color.pack()

input_color = Entry(root,text="Write the Color")
input_color.pack()


class Score():
    
    def __init__(self):
        self.__score = 0
        
    def updateScore(self):
        self.text = ["BLUE", "GREEN", "ORANGE", "PINK", "RED", "YELLOW", "PURPLE", "BROWN", "GREY", "BLACK"]
        self.random_no_text = random.randint(0, 9)
        
        self.color = ["blue", "green", "orange", "pink", "red", "yellow", "purple", "brown", "grey", "black"]
        self.random_no_color = random.randint(0, 9)
        
        lbl_color["text"] = self.text[self.random_no_text]
        lbl_color["fg"] = self.color[self.random_no_color]
        
    def check_score(self):
        color_to_check = input_color.get()
        
        
        if(color_to_check == self.color[self.random_no_color]):
            label_yes_no["text"] = "Yess you got it right!!!!"
            self.__score = self.__score + 1
            score_lbl["text"] = self.__score
        else:
            label_yes_no["text"] = "No its not correct. Try again!!!!"

obj = Score()
        
btn_start = Button(root, text = "Start", command = obj.updateScore, relief = FLAT, bg = "dark green", fg = "white", padx = 10, pady = 1, font = ("Arial", 15))
btn_start.pack()

btn_check = Button(root,text="Check",command = obj.check_score,relief = FLAT,bg="dark green",fg = "white",padx=10,pady=1,font=("Arial",15))
btn_check.pack()

label_yes_no = Label(root,bg="orange",fg="white")
label_yes_no.pack()

root.mainloop()
