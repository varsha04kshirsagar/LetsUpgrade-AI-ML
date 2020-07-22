# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:02:43 2020

@author: varsh
"""
#Step1 - Launching 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
dataset1=pd.read_csv("general_data.csv") 
print(dataset1.head() )
print(dataset1.columns)
#Step 2 - Data Treatment: 
print(dataset1.isnull()) 
print(dataset1.duplicated())
print(dataset1.drop_duplicates()) 

#Step 3 – Univariate Analysis: 
dataset3=dataset1[['Age','DistanceFromHome','Education','MonthlyIncome', 'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear', 'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].describe() 
print(dataset3)
dataset3=dataset1[['Age','DistanceFromHome','Education','MonthlyIncome', 'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear', 'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].median() 
print(dataset3)
dataset3=dataset1[['Age','DistanceFromHome','Education','MonthlyIncome', 'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear', 'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].mode() 
print(dataset3) 
dataset3=dataset1[['Age','DistanceFromHome','Education','MonthlyIncome', 'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear', 'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].var() 
print(dataset3)
dataset3=dataset1[['Age','DistanceFromHome','Education','MonthlyIncome', 'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear', 'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].skew() 
print(dataset3) 
dataset3=dataset1[['Age','DistanceFromHome','Education','MonthlyIncome', 'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear', 'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].kurt() 
print(dataset3) 

"""Inference from the analysis: 
• All the above variables show positive skewness; while Age & Mean_distance_from_home are leptokurtic and all other variables are platykurtic. 
• The Mean_Monthly_Income’s IQR is at 54K suggesting company wide attrition across all income bands 
• Mean age forms a near normal distribution with 13 years of IQR 
Outliers: 
There’s no regression found while plotting Age, MonthlyIncome, TotalWorkingYears, YearsAtCompany, etc., on a scatter plot 
"""
"""There’s no regression found while plotting Age, MonthlyIncome, TotalWorkingYears, YearsAtCompany, etc., on a scatter plot """
print("Outliers")

box_plot=dataset1.Age 
plt.boxplot(box_plot) 

#Age is normally distributed without any outliers 
box_plot=dataset1.MonthlyIncome 
plt.boxplot(box_plot) 

#Monthly Income is Right skewed with several outliers 
box_plot=dataset1.YearsAtCompany 
plt.boxplot(box_plot) 

#
 
