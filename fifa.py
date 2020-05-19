#%%
""" organizes Fifa players information, random generator of clubs in fifa,
statistics on fifa players, quiz"""

import tkinter as tk
import os
import random
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

class Fifa(tk.Frame):
    def __init__(self, root):
        self.root= root
        super().__init__(root)
        root.title("")
        root.geometry("400x360")
        
        title= tk.Label(root, text="FIFA 2019 PLAYERS", bg="red", width="300",
                        height="2", font=("Calibri", 13))
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

        statistic= tk.Button(root, text="FIFA Quiz", height="2", width="30",
                             command= self.quiz)
        statistic.pack()    
        
        space2= tk.Label(root, text="")
        space2.pack() 
        
        bucketlist= tk.Button(root, text="Statistics on Fifa Players",
                              height="2", width="30",
                              command=self.graph_display)
        bucketlist.pack()
        
        space4= tk.Label(root, text="")
        space4.pack() 
        
        graph= tk.Button(root, text= "FIFA Anaylsis", height="2", width="30",
                         command= self.anaylsis)
        graph.pack()
        
        space5= tk.Label(root, text="")
        space5.pack() 
        
        self.question1_entry= tk.StringVar()
        self.question2_entry= tk.StringVar()
        self.question3_entry= tk.StringVar()
    
    
   # Page 1: Player Information
    def player_select(self):
        self.players= []
        self.packs= []
        page= tk.Toplevel(self.root)
        page.title("")
        page.geometry("400x300")
        
        title1= tk.Label(page, text="Player Information", bg="red", width="300", 
                         height="2", font=("Calibri", 13))
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
        
    
    #def player_label(self):
    def player_label(self):
        players["information"]["name"] = player_select("Please enter a player's"
                                            " name" + str(profile + 1) + ": ")
        print("Enter six(6) items to fill your pack with: ")
        
        for item in range(6):
            packs_item = player_selection("Item name: ")
            players[information]["packs"].append(packs_item)
        print (players[information]["packs"])
        val = self.player_select()
        self.var.set(val)

    #def player_surface(self):
        page= tk.Toplevel(self.root)
        page.title("")
        page.geometry("400x300")
        
        title1= tk.Label(page, text="PLAYER INFORMATION", bg="red", width="300",
                         height="2", font=("Calibri", 13))
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
    def random_select(self):
        """ Pulls a FIFA club name from a random generator of 500 FIFA clubs
        
            Returns:
                string: one FIFA club name from random selection of FIFA clubs. 
        """
        fifa = pd.read_csv('fifadata.csv') 
        fifa.dropna()
        club= fifa["Club"]
        rand= club[random.randint(0,501)]
        return rand
    
    def random_label(self):
        """ Gets the FIFA club name onto the Club Picker window"""
        val = self.random_select()
        self.var.set(val)

    def channel_surface(self):
        """ Window for Club Picker Program"""
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
    def quiz(self):
        """ Window for FIFA Quiz Program"""
        window= tk.Toplevel(self.root)
        window.title("")
        window.geometry("800x600")
        
        welcome_title= tk.Label(window, text="FIFA Quiz", bg="blue",
                                width="300", height="2", font=("Calibri", 13))
        welcome_title.pack()

        gap1= tk.Label("")
        gap1.pack()

        question1= tk.Label(window, text= "1.) How many FIFA clubs are there?"
                            "\n(a)700\n(b)500\n(c)1,000\n(d)100\n")
        question1.pack()

        question1_entry= tk.Entry(window)
        question1_entry.pack()

        question2= tk.Label(window, text= "2.) Who is the FIFA World's Best"
                            "Player in 2019?\n(a) Cristiano Ronaldo\n"
                            "(b)Mohamed Salah\n(c)Eden Hazard\n(d)Lionel Messi"
                            "\n")
        question2.pack()

        question2_entry= tk.Entry(window)
        question2_entry.pack()

        question3= tk.Label(window, text= "Which country has won the most world"
                            "cup wins?\n(a) Argentina\n(b)Italy\n(c)USA"
                            "\n(d)Brazil\n")
        question3.pack()

        question3_entry= tk.Entry(window)
        question3_entry.pack()

        submit= tk.Button(window, text= "Submit", command= self.score)
        submit.pack()
        
    def score(self):
        """ Grade Quiz based on users input for FIFA Quiz

            Returns:
                string: gives the total score of the quiz
        """
        question1_entry= self.question1_entry.get()
        question2_entry= self.question2_entry.get()
        question3_entry= self.question3_entry.get()
        score= 0
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
    
    def histgraph(self):
        """ Histogram on Overall Score of FIFA players"""
        df= pd.read_csv("fifadata.csv")
        df.dropna()
        bins= [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
        plt.hist(df.Overall, bins=bins, color= "#6d32a8")
        
        plt.xticks(bins)
        plt.ylabel("Number of FIFA players in 2019")
        plt.xlabel("Overall Skill Level")        
        plt.title("FIFA Players Overall Skills in 2019")
        
        plt.show()
        
    def piegraph(self):
        """ Pie Chart on FIFA players preferred foot for playing soccer"""
        df= pd.read_csv("fifadata.csv")
        df.dropna() 
        level = df["Preferred Foot"].value_counts()
        labels = ('Right', 'Left')
        colors = ['lightskyblue', 'red']

        plt.title("What is a fifa player's prefered foot: left or right?")
        plt.pie(level, labels=labels, colors=colors, autopct='%1.0f%%')
        plt.show()
        
    def scattgraph(self):
        """ Scatter plot of FIFA players Market Value"""
        df= pd.read_csv("fifadata.csv")
        df.dropna()
        y= df["ID"]
        z= df["Value"]

        plt.scatter(y, z, edgecolor="black", linewidth=1, alpha=.75)

        plt.xscale("log")
        plt.yscale("log")

        plt.title("FIFA Players Market Value")
        plt.xlabel("Number of FIFA players in 2019")
        plt.ylabel("Total Market Value of the FIFA player in 2019")   
        plt.show()
        
    def topclub(self):
        """ Sorted 30 FIFA clubs from greatest amount of players in 2019

            Returns:
                list: returns a list of FIFA clubs with their corresponding 
                numbers of FIFA players next to the FIFA club name
         """
        df= pd.read_csv("fifadata.csv")
        df.dropna()
        a= df.sort_values(by='Club', ascending= False)
        a= df["Club"].value_counts()
        return (a[:31])
        
    def top_label(self):
        """Gets the list of FIFA club names onto the window. """
        val = self.topclub()
        self.var.set(val)
        
    def topclub_display(self):
        """ Displays a new window of displaying the top 30 FIFA clubs with the
        most players"""
        top_page= tk.Toplevel(self.root)
        top_page.title("")
        top_page.geometry("800x600")
        label= tk.Label(top_page, text="Top 30 clubs that have the most FIFA"
                    " players in 2019. Click the button to see the results!")
        label.pack()
        click_me= tk.Button(top_page, text= "CLICK ME!", command=self.top_label)
        click_me.pack()
        self.var= tk.StringVar()
        
        text_top= tk.Label(top_page, textvariable= self.var)
        
        text_top.pack()
        
        add_info= tk.Label(top_page, text= "As you can see, the max amount of"
                           " FIFA players in a team/club are 33!")
        add_info.pack()
        
    #Page 4: Statistics on FIFA Players     
    def graph_display(self):
        """ Displays various buttons on the Statistics on FIFA Players window"""
        graph_page= tk.Toplevel(self.root)
        graph_page.title("")
        graph_page.geometry("400x300")
        
        title= tk.Label(graph_page, text="Statistics on Fifa Players",
                        bg="blue", width="300",
                        height="2", font=("Calibri", 13))
        title.pack()
        
        gap= tk.Label(graph_page, text="")
        gap.pack()
        
        name= tk.Label(graph_page, text="Welcome to our Statistic on FIFA 2019"
                       " players!")
        name.pack()
        
        name1= tk.Label(graph_page, text= "Select any button to explore"
                        " different aspect of the data!")
        name1.pack()
        
        button1= tk.Button(graph_page, text= "FIFA Players Overall Score",
                           command=self.histgraph)
        button1.pack()
        
        button2= tk.Button(graph_page, text= "FIFA Players Prefered Foot: Left"
                           " or Right", command= self.piegraph)
        button2.pack()
        
        button3= tk.Button(graph_page, text= "Market Value of the FIFA Players",
                           command=self.scattgraph)
        button3.pack()

        button4= tk.Button(graph_page, text= "Top 30 clubs that have the most"
                           " FIFA players in 2019",
                           command=self.topclub_display)
        button4.pack()
        
    #Page 5: FIFA Anaylsis
    def anaylsis(self):
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

def main():
    root = tk.Tk()
    f= Fifa(root)
    f.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
    

# %%
