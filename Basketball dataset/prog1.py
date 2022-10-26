import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('C:/Users/Joel John Joseph/Desktop/Python_Data_analytics/FOR_EXAM/basketball.csv')
pd.DataFrame(df)

#a) Find the number of values present in the dataset

print(" ")
print("\n\tA\t\n")
print("Number of attributes=",len(df.columns))
print("Number of samples=",len(df))
print("\n \t OR")
print(" ")
print("\n\tA\t\n")
lst=list(df.columns)
print("Number of attributes=",len(lst))
l=list(df.shape)
print("Number of samples=",l[0])

#b) Display all the columns in the dataset
print(" ")
print("\n\tB\t\n")
print(df.columns)
#c) How many different schools have participated?

print(" ")
print("\n\tC\t\n")
print(df.school.unique())

#d) What is the average winning percentage?

print(" ")
print("\n\tD\t\n")
print(df.wins.mean())

#e) Which school in which year has maximum winning percentage?

print(" ")
print("\n\tE\t\n")
c=df.groupby(['school','year'])['win_percentage'].max()
print(c)


#f) Use appropriate graph for showing the year_wise opponent_points of a school.

print(" ")
print("\n\tF\t\n")
import matplotlib.pyplot as plt






plt.bar(df.year, df.opponent_points, color ='maroon',width = 0.8)
 
plt.xlabel("year")
plt.ylabel("opponent_points")
plt.title("year VS opponent_points")
plt.show()



#g) Use histogram for presenting total number of participation of every school in
#games, its corresponding wins and losses.

print(" ")
print("\n\tG\t\n")



#h) Are there any null values present in the dataset? If yes, how will you deal with
#it? Explain with appropriate code.

print(" ")
print("\n\tH\t\n")

dict={'CIA1':[19,200,np.nan,15],
      'CIA2':[42,46,38,np.nan],
      'CIA3':[np.nan,18,19,17]}
data=pd.DataFrame(dict)
print(data)

import seaborn as sns

sns.heatmap(data.isnull(),cmap='OrRd_r')
plt.grid()
plt.title("Number of missing values")
plt.show()


g=data.isnull()
print(g)


h=data.fillna(101)
print(h)




df.salary.head(10).plot.pie(autopct='%.2f')
