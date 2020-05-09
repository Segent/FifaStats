""" organizes Fifa players information, random generator of clubs in fifa, statistics on fifa players, quiz"""

import tkinter as tk
import os
import random
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns

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

        statistic= tk.Button(root, text="FIFA Quiz", height="2", width="30", command= self.pagequiz)
        statistic.pack()    
        
        space2= tk.Label(root, text="")
        space2.pack() 
        
        bucketlist= tk.Button(root, text="Statistics on Fifa Players", height="2", width="30")
        bucketlist.pack()
        
        space4= tk.Label(root, text="")
        space4.pack() 
    
   # Page 1: Player Information
    def player_select(self):
         page= tk.Toplevel(self.root)
         page.title("")
         page.geometry("400x300")

         title1= tk.Label(page, text="Player Information", bg="red", width="300", height="2", font=("Calibri", 13))
         title1.pack()

         gap= tk.Label(page, text="")
         gap.pack()

         name= tk.Label(page, text="Welcome to our Player Information Page!")
         name.pack()

         shuffle= tk.Button(page, text="Shuffle", command=self.player_label)
         shuffle.pack()

         gap1= tk.Label(page, text="")
         gap1.pack()
        
         fifa = pd.read_csv('fifadata.csv') 
         fifa.dropna()
         club= fifa["Name"]
         rand= club[random.randint(0,101)]
         return rand
        
    
    def player_label(self):
        val = self.player_select()
        self.var.set(val)

    def player_surface(self):
        page= tk.Toplevel(self.root)
        page.title("")
        page.geometry("400x300")
        
        title1= tk.Label(page, text="PLAYER INFORMATION", bg="red", width="300", height="2", font=("Calibri", 13))
        title1.pack()
        
        gap= tk.Label(page, text="")
        gap.pack()
        
        name= tk.Label(page, text="Welcome to our Player Information!")
        name.pack()
        
        self.var= tk.StringVar()
        
        text_shuffle= tk.Label(page, textvariable= self.var)
        text_shuffle.pack()
        
        shuffle= tk.Button(page, text="Shuffle", command=self.player_label)
        shuffle.pack()
        
        gap1= tk.Label(page, text="")
        gap1.pack()

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


    # Analysis page
    def analysis_page(self):
        page= tk.Toplevel(self.root)
        page.title("")
        page.geometry("400x300")
        
        title1= tk.Label(page, text="Fifa Player Analysis", bg="blue", width="300", height="2", font=("Calibri", 13))
        title1.pack()
        
        gap= tk.Label(page, text="")
        gap.pack()
        
        button1= tk.Button(root, text= "Average age of players", height="2", width="30")
        channel.pack()

        button2= tk.Button(root, text= "Average ages of players by nationality", height="2", width="30")
        channel.pack()

        button3= tk.Button(root, text= "Plot", height="2", width="30")
        channel.pack()

        button4= tk.Button(root, text= "Analysis of Japanese players", height="2", width="30")
        channel.pack()
        
        
        def read_file(self):
            self.df = pd.read_csv("fifadata.csv")
            return self.df

        #average_age of all players
        def avg_age(self, df):
            average_age = df.Age.mean()
            return average_age


        #average_age of players by nationality
        def avg_age_by_nationality(self, df):
            avg_age_by_nationality = df.groupby('Nationality').Age.mean()
            return avg_age_by_nationality.sort_values()

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
            plt.show()

        #Analysis on Japanese Players
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
            return df2.sort_values(by = 'player_count')

        #wages for japanese Players
        def wages_for_japanese_player(self, df):
            fifa_japanese = df[(df['Nationality'] == "Japan")]
            fifa_japanese.sort_values(by = 'Age')
            df2 = fifa_japanese[['Name', 'Wage']]
            return df2

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
    