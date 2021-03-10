import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

#loading the data set

match = pd.read_csv('gamesdataset.csv')

#taking look at first five records 

match.head()

match.shape

#want to know which player has wo how many man of the matches 
#value_counts helps to get frequency in a categorical manner

match['player_of_match'].value_counts()

#getting top 20 man of the matches 

match['player_of_match'].value_counts()[0:20]

list(match['player_of_match'].value_counts()[0:5].keys())

#bar graph of nost matches of top 5 players
plt.figure(figsize =(10, 7))
plt.bar(list(match['player_of_match'].value_counts()[0:5].keys()), list(match['player_of_match'].value_counts()[0:5]), color = 'green',width = 0.5)
plt.xlabel('Player Name')
plt.ylabel('Number of man of the matches')
plt.show()

#To calculate results of the matches 

match['result'].value_counts()

#Calculating number of tosses won by each team 
match['toss_winner'].value_counts()

#looking for results where a team won batting first 

batting_first = match[match['win_by_runs']!=0]
batting_first.head(10)

batting_first.shape

#looking for results where team won batting second

batting_second = match[match['win_by_wickets']!= 0 ]
batting_second.head(10)

batting_second.shape

#Now checking who wins most games team batting first or team batting second 

if(batting_second.shape < batting_first.shape):
    print("Team batting first wins most of the games")
else:
    print("Team batting second wins most of the games ")


# Graph for general view that by how many runs team batting first wins 

plt.figure(figsize=(8,5))
plt.hist(batting_first['win_by_runs'])
plt.title("Distribution of Runs")
plt.xlabel("Runs")
plt.ylabel("Wins")
plt.show()

# Graph to know by how many wickets does team batting second wins

plt.figure(figsize = (8,5))
plt.hist(batting_second['win_by_wickets'])
plt.title("Distribution of wins by wickets")
plt.xlabel("Wickets")
plt.ylabel("Wins")
plt.show()

# A Bar graph to knnow by how many times team batting second has won by how many wickets 

plt.figure(figsize = (8,5))
plt.bar(list(batting_second['win_by_wickets'].value_counts().keys()), list(batting_second['win_by_wickets'].value_counts()), color = 'blue',width = 0.5)
plt.xlabel("Wickets")
plt.ylabel("Wins")
plt.show()

# Just to know teams which has won how many games batting first

batting_first['winner'].value_counts().sort_values(ascending = True)

#Similarly to know teams which has won how many number of games batting second

batting_second['winner'].value_counts().sort_values(ascending=True)

#bar graph of teams vs no of wins batting second

plt.figure(figsize=(10,7))
plt.bar(list(batting_second['winner'].value_counts().sort_values().keys()), list(batting_second['winner'].value_counts().sort_values()))
plt.xlabel('Teams')
plt.ylabel("No of Wins")
plt.show()

#pie graph to know percentage of total wins by a specific team batting first

plt.figure(figsize = (10,7))
plt.pie(list(batting_first['winner'].value_counts()), labels = list(batting_first['winner'].value_counts().keys()), autopct ='%0.1f%%' )
plt.show()

#Total number of matches played each season 

match['season'].value_counts() 

#Number of matches in a particular city
match['city'].value_counts()


#find out how many times has a team won after winning the toss

import numpy as np 

won = np.sum(match['toss_winner'] == match['winner'])
won

#how many times team losing the toss has won the game

lost = np.sum(match['toss_winner']!= match['winner'])
lost

#Calculating total  

total = won + lost 
total

# Calculating win percentage after losing toss

winningafterlosingtoss = (lost/total)*100
winningafterlosingtoss

# Calculating win percentage after winning toss

winningafterwinningtoss = (won/total)*100
winningafterwinningtoss

#the umpires with most matches experience in the ipl

ump1 = match['umpire1'].value_counts()
ump1

ump2 = match['umpire2'].value_counts()
ump2

                                                
                                                
                                                #Thank you 


