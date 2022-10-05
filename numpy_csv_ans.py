
import numpy as np
import pandas as pd
data=pd.read_csv('/content/Salaries.csv')

data['job_title']

data['work_year']

"""a) Create structured array of Salaries"""

wy=np.array(data['work_year'])
el=np.array(data['experience_level'])
et=np.array(data['employment_type'])
jt=np.array(data['job_title'])
s=np.array(data['salary'])


str_arr=np.zeros(607,dtype={'names':('work year','experience_level','employment_type','job_title','salary'),'formats':('i4','U10','U10','U10','i4')})

str_arr['work year']=wy
str_arr['experience_level']=el
str_arr['employment_type']=et
str_arr['job_title']=jt
str_arr['salary']=s
print(str_arr)

"""b) Find the structure of the array created"""

str_arr.shape

"""c) Find the number of attributes and samples in the given dataset"""

lst=list(data.columns)
print("Number of attributes=",len(lst))
l=list(data.shape)
print("Number of samples=",l[0])

"""d) 
    a) All rows of first four attributes

"""

print(data.iloc[:,:4])

"""b. First 5 attributes and all samples

"""

print(data.iloc[:,:5])

"""c. 11 to 15 samples from attribute-4 and attribute-8

"""

print(data.iloc[11:16,[4,8]])

"""d. 10 sample and 5 th attribute"""

print(data.iloc[10,5])

"""e) Extract attribute 4 and 5 and create a new array"""

a4=data.iloc[:,4]
a5=data.iloc[:,5]
newa=np.array((a4,a5))
print(newa[:10])

"""f) Give the summary of the Salaries dataset using any statistical / aggregation functions"""

data.describe()

"""g) Which job has the maximum Salary?"""

print("Job with max salary:",data.job_title.loc[data['salary_in_usd'].idxmax()])

"""h) What is the average of the remote ratio?"""

print("Remote ratio average=",data['remote_ratio'].mean())

"""j) How many unique jobs are available?"""

print("Number of unique jobs:",data.job_title.nunique())

"""k) Which company location has the minimum salary in USD?"""

print("Company location with min salary:",data.company_location.loc[data['salary_in_usd'].idxmin()])

"""l) How many members employment type is PT?"""

print("Number of PT:",data.employment_type.value_counts()['PT'])

"""m) How many different categories of company size you can find in the dataset?"""

print("Number of company size categories:",data.company_size.nunique())

