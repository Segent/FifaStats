import tkinter as tk
import os
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Fifa:

    #def __init__(self):
        #pass

#Main Page
    def main_screen():
        """
        shows main screen and let users choose pages they want to see
        """
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
def player_information():
    page= tk.Tk()
    page.title("")
    page.geometry("400x300")
    
    title1= tk.Label(page, text="Player Information", bg="red", width="300", height="2", font=("Calibri", 13))
    title1.pack()

    gap= tk.Label(page, text="")
    gap.pack()
    
    name= tk.Label(page, text="Welcome to our Player Information Page!")
    name.pack()
    
    shuffle= tk.Button(page, text="Shuffle", command=random_select)
    shuffle.pack()
    
    gap1= tk.Label(page, text="")
    gap1.pack() 
    
    page.mainloop()
player_information()

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

df = pd.read_csv("fifadata.csv")
print(df)

#average_age of all players
average_age = df.Age.mean()
print(average_age)

#average_age of players by nationality
avg_age_Bynationality = df.groupby('Nationality').Age.mean()
print(avg_age_Bynationality.sort_values())

#convert the wages from string to integer value
#For example 5k = 5000
def convert_wage_to_int(wage_str):
    res = wage_str.replace('€', '').replace('K', '')
    res = int(res)*1000
    return res

age_salary_df = df[['Age', 'Wage']].copy()

#convert wage into numerical values
for ind, val in enumerate(list(age_salary_df['Wage'])):
    age_salary_df.loc[ind, 'Wage'] = convert_wage_to_int(val)

age_salary_df = age_salary_df.sort_values( by = 'Age')

#Plot age with wage
sns.regplot(x="Age", y="Wage", data=age_salary_df)
plt.show()

#Analysis on Japanese Players
df2 = pd.DataFrame()
fifa_japanese = df[(df['Nationality'] == "Japan")]
fifa_japanese.sort_values(by = 'Age')

#How many players in fifa rankings in each club
club_count = fifa_japanese.groupby('Club')['Name']
club = list(club_count.groups.keys())
count = list(club_count.size())
df2['club'] = club
df2['player_count'] = count
print(df2.sort_values(by = 'player_count'))

#wages for japanese Players
df2 = fifa_japanese[['Name', 'Wage']]
print(df2)