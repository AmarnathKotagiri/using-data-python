import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
import os


dir = r"F:\MIS-PDS\using-data-tha-AmarnathKotagiri\data"
os.chdir(dir)

HospData = pd.read_table(dir+r'\CaliforniaHospitalData.csv', sep=',')

PersData = pd.read_table(dir+r'\CaliforniaHospitalData_Personnel.txt', sep='\t')

# Merge hospital data and personnel data
MergedDF = pd.merge(PersData, HospData)

# Drop duplicates, some columns and perform some conditional statements 
MergedDF.T.drop_duplicates().T.drop(['Work_ID', 'PositionID', 'Website'], axis=1)[(MergedDF.Teaching=='Small/Rural')&(MergedDF.AvlBeds>=15)&(MergedDF.OperInc>=0)].to_csv(dir+r'\hospital_data_new.txt', sep='\t')

HospNewData = pd.read_table(dir+r'\hospital_data_new.txt', sep='\t').drop(['Unnamed: 0'], axis=1)

# Rename Column names
HospNewData.columns = ['HospitalID','LastName','FirstName','Gender','PositionTitle','Compensation','MaxTerm','StartDate','Phone','Email','Name','Zip','TypeControl','Teaching','DonorType','FullTimeCount','NetPatientRevenue','InpatientOperExp','OutpatientOperExp','Operating_Revenue','Operating_Income','AvlBeds']

# Generating new rows to append
appendRows = pd.DataFrame({'HospitalID':['17718','33251'],
'LastName':['Kotagiri','Kotagiri'],
'FirstName':['Amarnath','Amarnath'],
'Gender':['M','M'],
'PositionTitle':['Regional Representative','Acting Director'],
'Compensation':['46978','248904'],
'MaxTerm':['4','8'],
'StartDate':['9/19/2022','9/19/2022'],
'Phone':['405-662-1212','405-662-1212'],
'Email':['amarnath@okstate.edu','amarnath@okstate.edu'],
'Name':['Mercy Medical Center - Mount Shasta','Sutter Coast Hospital'],
'Zip':['96067','95531'],
'TypeControl':['Non Profit','Non Profit'],
'Teaching':['Small/Rural','Small/Rural'],
'DonorType':['Charity','Charity'],
'FullTimeCount':['350','150'],
'NetPatientRevenue':['937520.86','555078.21'],
'InpatientOperExp':['525245.40','2793458.15'],
'OutpatientOperExp':['916220.54','466220.78'],
'Operating_Revenue':['499337','93713'],
'Operating_Income':['5505','933'],
'AvlBeds':['20','30']},
index=[66,67])

# Saving the new rows into a data frame new_merge
new_merge = HospNewData.append(appendRows, ignore_index=True)
# new_merge.to_csv(dir+r'\merge_data_new.txt', sep='\t')

# Converting datatype of a coulmn to date time
new_merge['StartDate'] = pd.to_datetime(new_merge['StartDate'])
# Converting coulmns datatype to float
new_merge['FullTimeCount'] = new_merge.FullTimeCount.astype(float)
new_merge['NetPatientRevenue'] = new_merge.NetPatientRevenue.astype(float)
new_merge['Operating_Income'] = new_merge.Operating_Income.astype(float)
print(new_merge.dtypes)

# save the non profit data from new_merge to a new file
NonProfitHospData = new_merge[(new_merge.TypeControl=='Non Profit')&(new_merge.FullTimeCount>250)&(new_merge.NetPatientRevenue>=109000)].drop(['LastName','FirstName','Gender','PositionTitle','Compensation','MaxTerm','StartDate','Phone','Email'],axis=1)
NonProfitHospData.to_csv(dir+r'\non_profit_hospital_data.txt', sep='\t')

# save the regional representative data from new_merge to a new file
RegRepHospData = new_merge[(new_merge.PositionTitle=='Regional Representative')&(new_merge.Operating_Income>100000)]
RegRepHospData.to_csv(dir+r'\regional_repr_hospital_data.txt', sep='\t')
