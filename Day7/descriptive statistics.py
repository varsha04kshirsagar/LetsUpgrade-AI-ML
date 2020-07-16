# -*- coding: utf-8 -*-
import pandas as pd
#load file sheets by number 
dataset = pd.read_excel("3. Descriptive Statistics.xlsx",sheet_name=0)
#load file sheet by name
dataset2 = pd.read_excel("3. Descriptive Statistics.xlsx",sheet_name="DescriptiveStatistics1")
#load first five records
dataset.head()
print(dataset.head())
#load coloumn
#dataset.columns()
#find mean of particular coloumn
mean_CS = dataset['CurrentSalary'].mean()
print(mean_CS)
#find meadian of particular coloumn
median_CS = dataset['CurrentSalary'].median()
print(median_CS)
#find median of multiple coloumn
median_CSMultiple = dataset[['CurrentSalary','After6Months','SalBegin']].median()
print(median_CSMultiple)
#variance
variance_CSMultiple = dataset[['CurrentSalary','After6Months','SalBegin']].var()
print(variance_CSMultiple)
#find standard deviation
standard_CSMultiple = dataset[['CurrentSalary','After6Months','SalBegin']].std()
print(standard_CSMultiple)
#find describe variables
describe_CSMultiple = dataset[['CurrentSalary','After6Months','SalBegin']].describe()
print(describe_CSMultiple)
#find sum
sum_CSMultiple = dataset[['CurrentSalary','After6Months','SalBegin']].sum()
print(sum)
#find skew
skew_CSMultiple = dataset[['CurrentSalary','After6Months','SalBegin']].skew()
print(skew_CSMultiple)

#kurt
krut_CSMultiple = dataset[['CurrentSalary','After6Months','SalBegin']].kurt()
print(krut_CSMultiple)
#find outline using box plot

import matplotlib.pyplot as plt
plt.boxplot(dataset.CurrentSalary)
# drow scatter plot
plt.scatter(dataset.CurrentSalary,dataset.After6Months)
#in pictoroial form using histrogram
plt.hist(dataset.CurrentSalary)