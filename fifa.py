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
        
        channel= tk.Button(root, text= "Player Information", height="2", width="30", command="channel_surface")
        channel.pack()
        
        space1= tk.Label(root, text="")
        space1.pack() 
        
        statistic= tk.Button(root, text="FIFA 20 Quiz", height="2", width="30")
        statistic.pack()    
        
        space2= tk.Label(root, text="")
        space2.pack() 
        
        bucketlist= tk.Button(root, text="Club Picker", height="2", width="30")
        bucketlist.pack()
        
        space3= tk.Label(root, text="")
        space3.pack() 
        
        bucketlist= tk.Button(root, text="Statistics on Fifa Players", height="2", width="30")
        bucketlist.pack()
        
        space4= tk.Label(root, text="")
        space4.pack() 
    
        root.mainloop()
    main_screen()
    
# Page 1: Club Channel Picker
#creating a random selector channel 

def random_select():
    youtube = pd.read_csv('fifadata.csv')
    youtube.dropna()
    genre= youtube["Club"]
    print(genre[random.randint(0,101)])
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
#def top_20():
    #fifa= pd.read_csv('fifadata.csv')
    #top_100= fifa.sort_values('Value', ascending= False)
    #top_100[:21]
    #top_100["Name"]

def pageQuiz():
    page_quiz= tk.Tk()
    page_quiz.title("")
    page_quiz.geometry("400x300")
    
    title1= tk.Label(page_quiz, text="FIFA 20 QUIZ", bg="blue", width="300", height="2", font=("Calibri", 13))
    title1.pack()

    gap= tk.Label(page_quiz, text="")
    gap.pack()
    
    name= tk.Label(page_quiz, text="Welcome to our Fifa 20 Quiz!")
    name.pack()

    page_quiz.mainloop()
pageQuiz()
    
#Page 4: Statistics on Fifa Players

# test
# test2