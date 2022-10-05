import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('C:/Users/Python_Data_analytics/Salaries.csv')


#QUestion A
lst=list(data.columns)
print("Number of attributes=",len(lst))
l=list(data.shape)
print("Number of samples=",l[0])

#QUestion B
print("\nQUestion B\n")
print(data.iloc[:,:4])

print(data.iloc[:,:5])

print(data.iloc[11:16,[4,8]])


print(data.iloc[10,5])

#QUestion C
print("\nQUestion C\n")
a4=data.iloc[:,4]
a5=data.iloc[:,5]
newarr=np.array((a4,a5))
print(newarr[:10])

#QUestion D
print("\nQUestion D\n")
print(data.describe())

#QUestion E
print("\nQUestion E\n")
print("Job with max salary:",data.job_title.loc[data['salary_in_usd'].idxmax()])

#QUestion F
print("\nQUestion F\n")
print("Remote ratio average=",data['remote_ratio'].mean())

#QUestion G
print("\nQUestion G\n")
print("Number of unique jobs:",data.job_title.nunique())


#QUestion H
print("\nQUestion H\n")
print("Company location with min salary:",data.company_location.loc[data['salary_in_usd'].idxmin()])


#QUestion I
print("\nQUestion I\n")
print("Number of PT:",data.employment_type.value_counts()['PT'])


#QUestion J
print("\nQUestion J\n")
print("Number of company size categories:",data.company_size.nunique())


#QUESTION 2

import matplotlib.pyplot as plt


barpic=plt.figure(figsize=(10,5))
plt.bar(data.experience_level, data.employment_type, color ='maroon',width = 0.4)
 
plt.xlabel("experience_level")
plt.ylabel("employment_type")
plt.title("employment_type VS employment_type")
plt.show()

plt.hist(data.experience_level)
plt.title('Height Distribution of US presidents')
plt.xlabel('height(cm)')
plt.ylabel('number');
plt.show()

data.plot(kind='scatter',x='experience_level',y='employment_type',alpha=0.3)
plt.show()

piepic=plt.figure(figsize=(10,7))
plt.pie(data['employment_type'].value_counts(),labels=data['employment_type'].unique())
plt.legend()
plt.title("Categories of employment_type")
plt.show()


