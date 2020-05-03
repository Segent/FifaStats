import tkinter as tk
import os
import random
import pandas as pd
import numpy as np

class Fifa:

    #def __init__(self):
        #pass

#Main Page
    def main_screen():
        root= tk.Tk()
        root.title("")
        root.geometry("400x300")
        
        title= tk.Label(root, text="FIFA 2019 PLAYERS", bg="red", width="300", height="2", font=("Calibri", 13))
        title.pack()
        
        space= tk.Label(root, text="")
        space.pack()
        
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
    
        root.mainloop()
    main_screen()
    
# Page 1: Club Channel Picker
#creating a random selector channel 

def random_select():
    fifa = pd.read_csv('fifadata.csv')
    fifa.dropna()
    club= fifa["Club"]
    print(club[random.randint(0,101)])
random_select()

def channel_surface():
    page= tk.Tk()
    page.title("")
    page.geometry("400x300")
    
    title1= tk.Label(page, text="Club Picker", bg="blue", width="300", height="2", font=("Calibri", 13))
    title1.pack()

    gap= tk.Label(page, text="")
    gap.pack()
    
    name= tk.Label(page, text="Welcome to our Club Picker program!")
    name.pack()
    
    shuffle= tk.Button(page, text="Shuffle", command=random_select)
    shuffle.pack()
    
    gap1= tk.Label(page, text="")
    gap1.pack() 
    
    page.mainloop()
channel_surface()
    

#Page 2: Player Information


#Page 3: Fifa 20 Quiz

def pageQuiz():
    page_quiz= tk.Tk()
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

    for text, value in answer1:
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

    page_quiz.mainloop()
pageQuiz()


    
    
    