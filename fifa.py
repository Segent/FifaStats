""" organizes Fifa players information, random generator of clubs in fifa, statistics on fifa players, quiz"""

import tkinter as tk
import os
import random
import pandas as pd
import numpy as np
import seaborn as sns
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
        
        channel= tk.Button(root, text= "Player Information", height="2", width="30")
        channel.pack()

        space1= tk.Label(root, text="")
        space1.pack()

        bucketlist= tk.Button(root, text="Club Picker", height="2", width="30", command= self.channel_surface)
        bucketlist.pack()
        
        space3= tk.Label(root, text="")
        space3.pack() 

        statistic= tk.Button(root, text="FIFA Quiz", height="2", width="30", command= self.quiz)
        statistic.pack()    
        
        space2= tk.Label(root, text="")
        space2.pack() 
        
        analysis_channel= tk.Button(root, text="Statistics on Fifa Players", height="2", width="30", command=self.analysis_page)
        analysis_channel.pack()
        
        space4= tk.Label(root, text="")
        space4.pack() 
    
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


    #Page 3: Fifa Quiz
    def quiz(self, window):
        window= tk.Toplevel(self.root)
        window.title("")
        window.geometry("800x600")

        welcome_title= tk.Label(window, text="Club Picker", bg="blue", width="300", height="2", font=("Calibri", 13))
        welcome_title.pack()

        gap1= tk.Label("")
        gap1.pack()

        question1= tk.Label(window, text= "1.) How many FIFA clubs are there?\n(a)700\n(b)500\n(c)1,000\n(d)100\n")
        question1.pack()

        question1_entry= tk.Entry(window)
        question1_entry.pack()

        question2= tk.Label(window, text= "2.) Who is the FIFA World's Best Player in 2019?\n(a) Cristiano Ronaldo\n(b)Mohamed Salah\n(c)Eden Hazard\n(d)Lionel Messi\n")
        question2.pack()

        question2_entry= tk.Entry(window)
        question2_entry.pack()

        question3= tk.Label(window, text= "Which country has won the most world cup wins?\n(a) Argentina\n(b)Italy\n(c)USA\n(d)Brazil\n")
        question3.pack()

        question3_entry= tk.Entry(window)
        question3_entry.pack()

        submit= tk.Button(window, text= "Submit", command= self.total_score)
        submit.pack()
        
        self.var= tk.StringVar()
        
    def total_score(self, answer, question, question1, question2, question3):
        self.quiz(self, window)
        score = 0
        for answer in question:
            if input(self.question1) == "a" or "A":
                print("Number 1 is correct!")
                score += 1
            elif input(self.question2) == "d" or "D":
                print("Number 2 is correct!")
                score += 1
            elif input(self.question3) == "d" or "D":
                print("Number 3 is correct!")
                score += 1
        print("Nice try, you have gotten " + int(score) + "/3 correct!")
        
class FifaAnalysis():   
    # df = pd.read_csv("fifadata.csv")

    def avg_age(self, df):
        average_age = df.Age.mean()
        print(average_age)

    def avg_age_by_nationality(self, df):
        avg_age_by_nationality = df.groupby('Nationality').Age.mean()
        print(avg_age_by_nationality.sort_values())

    def age_salary(self, df):
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
        return age_salary_df

    #Plot age with wage
    def plot_display(self, age_salary_df):
        sns.regplot(x="Age", y="Wage", data=age_salary_df)
        return plt.show()

    def japanese_player_analysis(self, df):
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
    def wages_for_japanese_player(self, df):
        fifa_japanese = df[(df['Nationality'] == "Japan")]
        fifa_japanese.sort_values(by = 'Age')
        df2 = fifa_japanese[['Name', 'Wage']]
        print(df2)

def analysis_page():
    df = pd.read_csv("fifadata.csv")
    root = tk.Tk()
    f= FifaAnalysis()


    title= tk.Label(root)
    title.pack()

    btnl= tk.Button(root, text= "Average Age of Players", height="2", width="30", command=f.avg_age(df))
    btnl.pack()

    btn2= tk.Button(root, text= "Average Age of Players by Nationality", height="2", width="30", command=f.avg_age_by_nationality(df))
    btn2.pack()

    age_salary_df = f.age_salary(df)
    btn3= tk.Button(root, text= "Wage by age plot", height="2", width="30", command=f.plot_display(age_salary_df))
    btn3.pack()

    btn4= tk.Button(root, text= "Japanese players and thier clubs in Fifa ranking", height="2", width="30", command=f.japanese_player_analysis(df))
    btn4.pack()

    btn5= tk.Button(root, text= "Wages for Japanese players", height="2", width="30", command=f.wages_for_japanese_player(df))
    btn5.pack()

    root.mainloop()


def main():
    root = tk.Tk()
    f= Fifa(root)
    f.pack()
    root.mainloop()
    analysis_page()

if __name__ == "__main__":
    main()
    