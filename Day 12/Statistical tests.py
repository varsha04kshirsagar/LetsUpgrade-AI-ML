# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 17:08:06 2020

@author: varsh
"""

import pandas as pd
dataset = pd.read_excel("general_data1.xlsx",sheet_name = 'general_data')
print(dataset)
#dataset.head()
dataset['Attrition'] = dataset['Attrition'].map({"Yes":1, "No":0})
dataset['EducationField'] = dataset['EducationField'].map({"Life Sciences":1, "Other":0, "Medical":2,"Marketing":3,"Technical Degree":4,"Human Resources":5})
#dataset['Gender'] = dataset['Gender'].map({"Male":1, "Female":0})
#dataset['BusinessTravel'] = dataset['BusinessTravel'].map({"Travel_Rarely":1, "Non-Travel":0, "Travel_Frequently":2})
from scipy.stats import wilcoxon
print("Two Paired  samples are EducationField and MonthlyIncome for Attrition")
print("H0 is Two samples are significantly related and H1 is two samples are significantly not  related")
print("####################################################")
stats,p=wilcoxon(dataset.MonthlyIncome,dataset.EducationField)
print(stats,p) #r value,p for probabiliti for hypothesis
#if p is less than 0.05 means null hypothesis rejected
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between EducationField and MonthlyIncome")
else:
    print("Reject Hypothesis Ho and there is no correlation between EducationField and MonthlyIncome")
print("####################################################")
####################################################
stats,p=wilcoxon(dataset.MonthlyIncome,dataset.Education)
print(stats,p) #r value,p for probabiliti for hypothesis
#if p is less than 0.05 means null hypothesis rejected
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between MonthlyIncome and Education")
else:
    print("Reject Hypothesis Ho and there is no correlation between MonthlyIncome and Education")
###########################################
print("####################################################")    
from scipy.stats import friedmanchisquare  
stats,p=friedmanchisquare(dataset.MonthlyIncome,dataset.EducationField,dataset.Education)
print(stats,p) #r value,p for probabiliti for hypothesis 
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between MonthlyIncome and Education and EducationField")
else:
    print("Reject Hypothesis Ho and there is no correlation between MonthlyIncome and Education and EducationField")
print("####################################################")   
#################################################
from scipy.stats  import mannwhitneyu 
stats,p=mannwhitneyu(dataset.MonthlyIncome,dataset.Education)
print(stats,p) 
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between MonthlyIncome and Education")
else:
    print("Reject Hypothesis Ho and there is no correlation between MonthlyIncome and Education")
#####################################
print("####################################################")   
from scipy.stats import kruskal
stats,p=kruskal(dataset.MonthlyIncome,dataset.EducationField,dataset.Education)
print(stats,p) #r value,p for probabiliti for hypothesis 
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between MonthlyIncome and Education and EducationField")
else:
    print("Reject Hypothesis Ho and there is no correlation between MonthlyIncome and Education and EducationField")
##################################################
print("####################################################")
#Both variables are catagarical
from scipy.stats import chi2_contingency
chitable = pd.crosstab(dataset.Gender,dataset.BusinessTravel) 
print(chitable)    
stats,p,dof,expected = chi2_contingency(chitable)
print(stats,p)
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between BusinessTravel and Gender")
else:
    print("Reject Hypothesis Ho and there is no correlation between BusinessTravel and Gender")
    