import tkinter as tk
import os
import random
import pandas as pd
import numpy as np
""" organizes Fifa players information, random generator of clubs in fifa, statistics on fifa players, quiz"""

class Fifa(tk.Frame):
    def __init__(self, root):
        self.root= root
        super().__init__(root)
        root.title("")
        root.geometry("400x300")
        
        title= tk.Label(root, text="FIFA 2019 PLAYERS", bg="red", width="300", height="2", font=("Calibri", 13))
        title.pack()
        
        space= tk.Label(root, text="")
        space.pack()
        
        channel= tk.Button(root, text= "Player Information", height="2", width="30", command=self.channel_surface)
        channel.pack()

        space1= tk.Label(root, text="")
        space1.pack() 

        statistic= tk.Button(root, text="FIFA Quiz", height="2", width="30")
        statistic.pack()    

        space2= tk.Label(root, text="")
        space2.pack() 

        bucketlist= tk.Button(root, text="Club Picker", height="2", width="30")
        bucketlist.pack()
        
        space3= tk.Label(root, text="")
        space3.pack() 

        statistic= tk.Button(root, text="FIFA Quiz", height="2", width="30")
        statistic.pack()    
        
        space2= tk.Label(root, text="")
        space2.pack() 
        
        bucketlist= tk.Button(root, text="Statistics on Fifa Players", height="2", width="30")
        bucketlist.pack()
        
        space4= tk.Label(root, text="")
        space4.pack() 
        
    # Page 1: Club Channel Picker
    #creating a random selector channel 

    def random_select(self):
        fifa = pd.read_csv('fifadata.csv') #fix the file
        fifa.dropna()
        club= fifa["Club"]
        rand= club[random.randint(0,101)]
        return rand
    
    def random_label(self):
        val = self.random_select()
        self.var.set(val)

    def channel_surface(self):
        page= tk.Toplevel(self.root)
        page.title("")
        page.geometry("400x300")
        
        title1= tk.Label(page, text="Club Picker", bg="blue", width="300", height="2", font=("Calibri", 13))
        title1.pack()

        gap= tk.Label(page, text="")
        gap.pack()
        
        name= tk.Label(page, text="Welcome to our Club Picker program!")
        name.pack()
        
        self.var= tk.StringVar()
        
        text_shuffle= tk.Label(page, textvariable= self.var)
        text_shuffle.pack()
        
        shuffle= tk.Button(page, text="Shuffle", command=self.random_label)
        shuffle.pack()
        
        gap1= tk.Label(page, text="")
        gap1.pack()
        

    #Page 2: Player Information


    #Page 3: Fifa 20 Quiz

    def pagequiz(self):
        page_quiz= tk.Toplevel(self.root)
        page_quiz.title("")
        page_quiz.geometry("800x600")
        
        title1= tk.Label(page_quiz, text="FIFA 20 QUIZ", bg="blue", width="300",
                        height="2", font=("Calibri", 13))
        title1.pack()

        gap= tk.Label(page_quiz, text="")
        gap.pack()
        
        name= tk.Label(page_quiz, text="Welcome to our Fifa 20 Quiz!")
        name.pack()
        
        name2= tk.Label(page_quiz, text="")
        name2.pack()
            
        answer1= [("700", 1), ("500", 2), ("1,000", 3), ("100", 4), ("100", 5)]
        
        question1= tk.Label(page_quiz, text= "How many FIFA clubs are there?")
        question1.pack()

        for text, value in answer1: #fix later
            b = tk.Radiobutton(page_quiz, text=text, value=value)
            b.pack(anchor="w")
            
            if value == "700":
                print("You're correct!")
            else:
                print("You're wrong")
                
        name3= tk.Label(page_quiz, text="")
        name3.pack()
                
        answer2= [("Lionel Messi", 1), ("Cristiano Ronaldo", 2), ("Mohamed Salah", 3), ("Eden Hazard", 4)]
        
        question2= tk.Label(page_quiz, text= "Who is the FIFA World's Best Player in 2019?")
        question2.pack()

        for key, word in answer2:
            a = tk.Radiobutton(page_quiz, text=key, value=word)
            a.pack(anchor="w")
            
            if value == "Lionel Messi":
                print("You're correct!")
            else:
                print("You're wrong")
                
        name4= tk.Label(page_quiz, text="")
        name4.pack()
        
        answer3= [("Argentina", 1), ("Italy", 2), ("USA", 3), ("Brazil", 4)]
        
        question3= tk.Label(page_quiz, text= "Which country has won the most world cup wins?")
        question3.pack()

        for ab, cd in answer3:
            c = tk.Radiobutton(page_quiz, text=ab, value=cd)
            c.pack(anchor="w")
            
            if value == "Brazil":
                print("You're correct!")
            else:
                print("You're wrong")
                
        submit_button= tk.Button (page_quiz, text= "Submit")
        submit_button.pack()


def main():
    root = tk.Tk()
    f= Fifa(root)
    f.pack()
    root.mainloop()
    
if __name__ == "__main__":
    main()
    
    
    