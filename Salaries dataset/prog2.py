#1. Import the given “Salaries.csv” file as dataframe using pandas and perform the
#following:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('C:/Users/Joel John Joseph/Desktop/Python_Data_analytics/FOR_EXAM/Salaries.csv')

df=pd.DataFrame(df)




#a) Find the number of attributes and samples in the given dataset
print(" ")
print("\n\t\tA\n")

#print(df)

print("No of attributes is= ",len(df.columns))
print("No of sample is= ",len(df))


#b) Select and display the following
# All rows of first four attributes

print(" ")
print("\n\t\tB1\n")

print(df.head(4))
print(df.iloc[:,:4])

# First 5 attributes and all samples
print(" ")
print("\n\t\tB2\n")
print(df.head(5))
print(df.iloc[:,:4])

# 11 to 15 samples from attribute-4 and attribute-8
print(" ")
print("\n\t\tB3\n")
print(df.iloc[11:16,[4,9]])



# 10 sample and 5 th attribute

print(" ")
print("\n\t\tB4\n")
print(df.iloc[:10,[5]])
print(df.iloc[10,5])

#c) Extract attribute 4 and 5 and create a new array
print(" ")
print("\n\t\tC\n")
a=df.iloc[:,4]
b=df.iloc[:,5]
newarr=np.array(a,b)
print(newarr[:10])


#d) Give the summary of the Salaries dataset using any statistical / aggregation
#functions
print(" ")
print("\n\t\tD\n")
print(df.describe())


#e) Which job has the maximum Salary?
print(" ")
print("\n\t\tE\n")

g=df.groupby(['job_title','salary'])['salary'].max()

h=dict(g)
print(max(h))





#f) What is the average of the remote ratio?
print(" ")
print("\n\t\tF\n")
g=df.groupby('remote_ratio').mean()
print(g)



#g) How many unique jobs are available?
print(" ")
print("\n\t\tG\n")
f=df.job_title.unique()
print(f)



#h) Which company location has the minimum salary in USD?
print(" ")
print("\n\t\tH\n")


i=df.groupby(['company_location','salary'])['salary'].min()

j=dict(i)
print(min(j))



#i) How many members employment type is PT?
print(" ")
print("\n\t\tI\n")

print("Number of PT:",df.employment_type.value_counts()['PT'])




#j) How many different categories of company size you can find in the dataset?
print(" ")
print("\n\t\tJ\n")
dg=(df.company_size)
print(len(dg.unique()))
print("Number of company size categories:",df.company_size.nunique())



#2. Identify suitable attributes and plot using any 4 charts (Bar, Pie, Histogram, Scatter,
#Line, violin)
print(" ")
print("\n\t\t2\n")

plt.bar(df.experience_level, df.employment_type, color ='purple',width = 0.4)
 
plt.xlabel("experience_level")
plt.ylabel("employment_type")
plt.title("employment_type VS employment_type")
plt.show()



x=df.experience_level
y=df.employment_type
plt.scatter(x,y,alpha=0.3)
plt.show()


v=df.experience_level
plt.hist(v,bins=3)
plt.show()


plt.pie(df['employment_type'].value_counts(),labels=df['employment_type'].unique())
plt.legend()
plt.title("Categories of employment_type")
plt.show()



ex=df.salary
et=df.salary_in_usd
vi=[ex,et]
plt.violinplot(vi)
plt.show()




pieee=df["salary"].head(10).plot.pie(autopct='%.2f')
print(pieee)







