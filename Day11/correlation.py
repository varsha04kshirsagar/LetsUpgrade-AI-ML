# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 21:50:25 2020

@author: varsha
"""

import pandas as pd
dataset = pd.read_excel("general_data1.xlsx",sheet_name = 'general_data')
print(dataset)

import matplotlib.pyplot as plt
from scipy.stats import pearsonr
print("####################################################")
dataset['Attrition'] = dataset['Attrition'].map({"Yes":1, "No":0})
dataset['Gender'] = dataset['Gender'].map({"Male":1, "Female":0})
dataset['EducationField'] = dataset['EducationField'].map({"Life Sciences":1, "Other":0, "Medical":2,"Marketing":3,"Technical Degree":4,"Human Resources":5})
#print(dataset["Attrition"])
dataset['BusinessTravel'] = dataset['BusinessTravel'].map({"Travel_Rarely":1, "Non-Travel":0, "Travel_Frequently":2})
dataset['MaritalStatus'] = dataset['MaritalStatus'].map({"Married":1, "Single":0, "Divorced":2})
dataset['Department'] = dataset['Department'].map({"Sales":1, "Research & Development":0,"Human Resources":2})
#####################################################
print("####################################################")
print("Ho - there is correlation between Attrition and MonthlyIncome and Ha - there is correlation between Attrition and MonthlyIncome" )
stats,p=pearsonr(dataset.Attrition,dataset.MonthlyIncome)
print(stats,p) #r value,p for probabiliti for hypothesis
#if p is less than 0.05 means null hypothesis rejected
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between Attrition and MonthlyIncome")
else:
    print("Reject Hypothesis Ho and there is no correlation between Attrition and MonthlyIncome")
    

plt.scatter(dataset.Attrition,dataset.MonthlyIncome)
#############################################################
print(dataset.corr())
#############################################################
print("####################################################")
print("Ho - there is correlation between Attrition and EducationField and Ha - there is correlation between Attrition and EducationField" )
stats,p=pearsonr(dataset.Attrition,dataset.EducationField)
print(stats,p) #r value,p for probabiliti for hypothesis
#if p is less than 0.05 means null hypothesis rejected
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between Attrition and EducationField")
else:
    print("Reject Hypothesis Ho and there is no correlation between Attrition and EducationField")
    

plt.scatter(dataset.Attrition,dataset.EducationField)
############################################################
print("####################################################")
print("Ho - there is correlation between Attrition and BusinessTravel and Ha - there is correlation between Attrition and BusinessTravel" )
stats,p=pearsonr(dataset.Attrition,dataset.BusinessTravel)
print(stats,p) #r value,p for probabiliti for hypothesis
#if p is less than 0.05 means null hypothesis rejected
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between Attrition and BusinessTravel")
else:
    print("Reject Hypothesis Ho and there is no correlation between Attrition and BusinessTravel")    
plt.scatter(dataset.Attrition,dataset.BusinessTravel)

####################################################
print("####################################################")
print("Ho - there is correlation between Attrition and MaritalStatus and Ha - there is correlation between Attrition and MonthlyIncome" )
stats,p=pearsonr(dataset.Attrition,dataset.MaritalStatus)
print(stats,p) #r value,p for probabiliti for hypothesis
#if p is less than 0.05 means null hypothesis rejected
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between Attrition and MaritalStatus")
else:
    print("Reject Hypothesis Ho and there is no correlation between Attrition and MaritalStatus")
plt.scatter(dataset.Attrition,dataset.MaritalStatus)
######################################################
print("####################################################")
print("Ho - there is correlation between Attrition and DistanceFromHome and Ha - there is correlation between Attrition and DistanceFromHome" )
stats,p=pearsonr(dataset.Attrition,dataset.DistanceFromHome)
print(stats,p) #r value,p for probabiliti for hypothesis
#if p is less than 0.05 means null hypothesis rejected
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between Attrition and DistanceFromHome")
else:
    print("Reject Hypothesis Ho and there is no correlation between Attrition and DistanceFromHome")   
plt.scatter(dataset.Attrition,dataset.DistanceFromHome)
#######################################################       
print("####################################################")
print("Ho - there is correlation between Attrition and Education and Ha - there is correlation between Attrition and Education" )
stats,p=pearsonr(dataset.Attrition,dataset.Education)
print(stats,p) #r value,p for probabiliti for hypothesis
#if p is less than 0.05 means null hypothesis rejected
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between Attrition and Education")
else:
    print("Reject Hypothesis Ho and there is no correlation between Attrition and Education")   
plt.scatter(dataset.Attrition,dataset.Education)    
#####################################################
print("####################################################")
print("Ho - there is correlation between Attrition and Gender and Ha - there is correlation between Attrition and Gender" )
stats,p=pearsonr(dataset.Attrition,dataset.Gender)
print(stats,p) #r value,p for probabiliti for hypothesis
#if p is less than 0.05 means null hypothesis rejected
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between Attrition and Gender")
else:
    print("Reject Hypothesis Ho and there is no correlation between Attrition and Gender")   
plt.scatter(dataset.Attrition,dataset.Gender)       
#######################################################
print("####################################################")
print("Ho - there is correlation between Attrition and JobLevel and Ha - there is correlation between Attrition and JobLevel" )
stats,p=pearsonr(dataset.Attrition,dataset.JobLevel)
print(stats,p) #r value,p for probabiliti for hypothesis
#if p is less than 0.05 means null hypothesis rejected
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between Attrition and JobLevel")
else:
    print("Reject Hypothesis Ho and there is no correlation between Attrition and JobLevel")   
plt.scatter(dataset.Attrition,dataset.JobLevel)       
######################################################
print("####################################################")
print("Ho - there is correlation between Attrition and NumCompaniesWorked and Ha - there is correlation between Attrition and NumCompaniesWorked" )
stats,p=pearsonr(dataset.Attrition,dataset.NumCompaniesWorked)
print(stats,p) #r value,p for probabiliti for hypothesis
#if p is less than 0.05 means null hypothesis rejected
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between Attrition and NumCompaniesWorked")
else:
    print("Reject Hypothesis Ho and there is no correlation between Attrition and NumCompaniesWorked")   
plt.scatter(dataset.Attrition,dataset.NumCompaniesWorked)     
###########################################################
print("####################################################")
print("Ho - there is correlation between Attrition and PercentSalaryHike and Ha - there is correlation between Attrition and NumCompaniesWorked" )
stats,p=pearsonr(dataset.Attrition,dataset.PercentSalaryHike)
print(stats,p) #r value,p for probabiliti for hypothesis
#if p is less than 0.05 means null hypothesis rejected
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between Attrition and PercentSalaryHike")
else:
    print("Reject Hypothesis Ho and there is no correlation between Attrition and PercentSalaryHike")   
plt.scatter(dataset.Attrition,dataset.PercentSalaryHike)   
#########################################################
print("####################################################")
print("Ho - there is correlation between Attrition and StandardHours and Ha - there is correlation between Attrition and NumCompaniesWorked" )
stats,p=pearsonr(dataset.Attrition,dataset.StandardHours)
print(stats,p) #r value,p for probabiliti for hypothesis
#if p is less than 0.05 means null hypothesis rejected
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between Attrition and StandardHours")
else:
    print("Reject Hypothesis Ho and there is no correlation between Attrition and StandardHours")   
plt.scatter(dataset.Attrition,dataset.StandardHours)   
########################################################
print("####################################################")
print("Ho - there is correlation between Attrition and TotalWorkingYears and Ha - there is correlation between Attrition and NumCompaniesWorked" )
stats,p=pearsonr(dataset.Attrition,dataset.TotalWorkingYears)
print(stats,p) #r value,p for probabiliti for hypothesis
#if p is less than 0.05 means null hypothesis rejected
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between Attrition and TotalWorkingYears")
else:
    print("Reject Hypothesis Ho and there is no correlation between Attrition and TotalWorkingYears")   
plt.scatter(dataset.Attrition,dataset.TotalWorkingYears)   
####################################################
print("####################################################")
print("Ho - there is correlation between Attrition and YearsAtCompany and Ha - there is correlation between Attrition and NumCompaniesWorked" )
stats,p=pearsonr(dataset.Attrition,dataset.YearsAtCompany)
print(stats,p) #r value,p for probabiliti for hypothesis
#if p is less than 0.05 means null hypothesis rejected
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between Attrition and YearsAtCompany")
else:
    print("Reject Hypothesis Ho and there is no correlation between Attrition and YearsAtCompany")   
plt.scatter(dataset.Attrition,dataset.YearsAtCompany)   
###################################################################
print("####################################################")
print("Ho - there is correlation between Attrition and YearsSinceLastPromotion and Ha - there is correlation between Attrition and NumCompaniesWorked" )
stats,p=pearsonr(dataset.Attrition,dataset.YearsSinceLastPromotion)
print(stats,p) #r value,p for probabiliti for hypothesis
#if p is less than 0.05 means null hypothesis rejected
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between Attrition and YearsSinceLastPromotion")
else:
    print("Reject Hypothesis Ho and there is no correlation between Attrition and YearsSinceLastPromotion")   
plt.scatter(dataset.Attrition,dataset.YearsSinceLastPromotion)  
###########################################################
print("####################################################")
print("Ho - there is correlation between Attrition and YearsWithCurrManagerv and Ha - there is correlation between Attrition and NumCompaniesWorked" )
stats,p=pearsonr(dataset.Attrition,dataset.YearsWithCurrManager)
print(stats,p) #r value,p for probabiliti for hypothesis
#if p is less than 0.05 means null hypothesis rejected
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between Attrition and YearsWithCurrManager")
else:
    print("Reject Hypothesis Ho and there is no correlation between Attrition and YearsWithCurrManager")   
plt.scatter(dataset.Attrition,dataset.YearsWithCurrManager)
#################################################################   
print("####################################################")
print("Ho - there is correlation between Attrition and YearsWithCurrManagerv and Ha - there is correlation between Attrition and NumCompaniesWorked" )
stats,p=pearsonr(dataset.Attrition,dataset.Department)
print(stats,p) #r value,p for probabiliti for hypothesis
#if p is less than 0.05 means null hypothesis rejected
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between Attrition and Department")
else:
    print("Reject Hypothesis Ho and there is no correlation between Attrition and Department")   
plt.scatter(dataset.Attrition,dataset.Department) 
 
######################################################
print("####################################################")
print("Ho - there is correlation between Attrition and EmployeeID and Ha - there is correlation between Attrition and EmployeeID" )
stats,p=pearsonr(dataset.Attrition,dataset.EmployeeID)
print(stats,p) #r value,p for probabiliti for hypothesis
#if p is less than 0.05 means null hypothesis rejected
if p >=0.05:
    print("accept Hypothesis Ho and there is correlation between Attrition and EmployeeID")
else:
    print("Reject Hypothesis Ho and there is no correlation between Attrition and EmployeeID")   
plt.scatter(dataset.Attrition,dataset.EmployeeID) 