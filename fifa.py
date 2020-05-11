""" organizes Fifa players information, random generator of clubs in fifa, statistics on fifa players, quiz"""

import tkinter as tk
import os
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
        
        channel= tk.Button(root, text= "Player Information", height="2",
                           width="30")
        channel.pack()

        space1= tk.Label(root, text="")
        space1.pack()

        bucketlist= tk.Button(root, text="Club Picker", height="2", width="30",
                              command= self.channel_surface)
        bucketlist.pack()
        
        space3= tk.Label(root, text="")
        space3.pack() 

        statistic= tk.Button(root, text="FIFA Quiz", height="2", width="30", command= self.quiz)
        statistic.pack()    
        
        space2= tk.Label(root, text="")
        space2.pack() 
        
        bucketlist= tk.Button(root, text="Statistics on Fifa Players",
                              height="2", width="30")
        bucketlist.pack()
        
        space4= tk.Label(root, text="")
        space4.pack() 
        
        self.question1_entry= tk.StringVar()
        self.question2_entry= tk.StringVar()
        self.question3_entry= tk.StringVar()
    
   # Page 1: Player Information
    #def player_select(self):
      #   page= tk.Toplevel(self.root)
        # page.title("")
      #   page.geometry("400x300")

        # title1= tk.Label(page, text="Player Information", bg="red", width="300", height="2", font=("Calibri", 13))
        # title1.pack()

       #  gap= tk.Label(page, text="")
       #  gap.pack()

       #  name= tk.Label(page, text="Welcome to our Player Information Page!")
        # name.pack()

       #  shuffle= tk.Button(page, text="Shuffle", command=self.player_label)
       #  shuffle.pack()

       #  gap1= tk.Label(page, text="")
       #  gap1.pack()
        
       #  fifa = pd.read_csv('fifadata.csv') 
       #  fifa.dropna()
       #  club= fifa["Name"]
       #  rand= club[random.randint(0,101)]
       #  return rand
        
    
    #def player_label(self):
        #val = self.player_select()
       # self.var.set(val)

    #def player_surface(self):
       # page= tk.Toplevel(self.root)
       # page.title("")
       # page.geometry("400x300")
        
      #  title1= tk.Label(page, text="PLAYER INFORMATION", bg="red", width="300", height="2", font=("Calibri", 13))
        #title1.pack()
        
        #gap= tk.Label(page, text="")
       # gap.pack()
        
        #name= tk.Label(page, text="Welcome to our Player Information!")
        #name.pack()
        
        #self.var= tk.StringVar()
        
       # text_shuffle= tk.Label(page, textvariable= self.var)
        #text_shuffle.pack()
        
       # shuffle= tk.Button(page, text="Shuffle", command=self.player_label)
       # shuffle.pack()
        
       # gap1= tk.Label(page, text="")
       # gap1.pack()

    # Page 2: Club Channel Picker
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
        
        title1= tk.Label(page, text="Club Picker", bg="blue", width="300",
                         height="2", font=("Calibri", 13))
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
    
    #Page 3: FIFA Quiz 
    def quiz_label(self):
        lbl = self.score()
        self.var.set(lbl)
    
    def quiz(self):
        window= tk.Toplevel(self.root)
        window.title("")
        window.geometry("800x600")
        
        welcome_title= tk.Label(window, text="FIFA Quiz", bg="blue", width="300", height="2", font=("Calibri", 13))
        welcome_title.pack()

        gap1= tk.Label("")
        gap1.pack()

        question1= tk.Label(window, text= "1.) How many FIFA clubs are there?\n(a)700\n(b)500\n(c)1,000\n(d)100\n")
        question1.pack()

        question1_entry= tk.Entry(window, textvariable= self.question1_entry)
        question1_entry.pack()

        question2= tk.Label(window, text= "2.) Who is the FIFA World's Best Player in 2019?\n(a) Cristiano Ronaldo\n(b)Mohamed Salah\n(c)Eden Hazard\n(d)Lionel Messi\n")
        question2.pack()

        question2_entry= tk.Entry(window, textvariable= self.question2_entry)
        question2_entry.pack()

        question3= tk.Label(window, text= "Which country has won the most world cup wins?\n(a) Argentina\n(b)Italy\n(c)USA\n(d)Brazil\n")
        question3.pack()

        question3_entry= tk.Entry(window, textvariable= self.question3_entry)
        question3_entry.pack()

        submit= tk.Button(window, text= "Submit", command= self.score)
        submit.pack()
        
        self.var= tk.StringVar()
        
    def score(self):
        question1_entry= self.question1_entry.get()
        question2_entry= self.question2_entry.get()
        question3_entry= self.question3_entry.get()
        score = 0
        if question1_entry == "a" or question1_entry == "A":
            print("Number 1: correct!")
            score += 1
        else:
            print("Number 1:incorrect")
        if question2_entry == "d" or question2_entry == "D":
            print("Number 2: correct!")
            score += 1
        else:
            print("Number 2:incorrect")
        if question3_entry == "d" or question3_entry == "D":
            print("Number 3: correct!")
            score += 1
        else:
            print("Number 3:incorrect")
        print("Score: " + str(score) + "/3")
        return (score)

    
# class Stat:
#     df = pd.read_csv("fifadata.csv")  #fix this: sys argsv (add to command line)
#     print(df)

#     #average_age of all players
#     average_age = df.Age.mean()
#     print(average_age)

#     #average_age of players by nationality
#     avg_age_Bynationality = df.groupby('Nationality').Age.mean()
#     print(avg_age_Bynationality.sort_values())

#     #convert the wages from string to integer value
#     #For example 5k = 5000
#     def convert_wage_to_int(wage_str):
#         res = wage_str.replace('€', '').replace('K', '')
#         res = int(res)*1000
#         return res

#     age_salary_df = df[['Age', 'Wage']].copy()

#     #convert wage into numerical values
#     for ind, val in enumerate(list(age_salary_df['Wage'])):
#         age_salary_df.loc[ind, 'Wage'] = convert_wage_to_int(val)

#     age_salary_df = age_salary_df.sort_values( by = 'Age')

#     #Plot age with wage
#     sns.regplot(x="Age", y="Wage", data=age_salary_df)
#     plt.show()

#     #Analysis on Japanese Players
#     df2 = pd.DataFrame()
#     fifa_japanese = df[(df['Nationality'] == "Japan")]
#     fifa_japanese.sort_values(by = 'Age')

#     #How many players in fifa rankings in each club
#     club_count = fifa_japanese.groupby('Club')['Name']
#     club = list(club_count.groups.keys())
#     count = list(club_count.size())
#     df2['club'] = club
#     df2['player_count'] = count
#     print(df2.sort_values(by = 'player_count'))

#     #wages for japanese Players
#     df2 = fifa_japanese[['Name', 'Wage']]
#     print(df2)

def main():
    root = tk.Tk()
    f= Fifa(root)
    f.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
    