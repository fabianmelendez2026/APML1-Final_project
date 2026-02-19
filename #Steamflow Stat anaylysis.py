#Steamflow Stat anaylysis

#install pandas, matplotlib, and seaborn for plots
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


datafile = pd.read_csv('streamflow.csv')

#Change display to show all data files and confirm data displays correctly
#pd.set_option('display.max_rows',None)
#pd.set_option('display.max_columns', None)

#Prints complete data file to confirm it correctly loaded.  
print(datafile)
print()

#Task 2- Calculate and print the number of rows and columns that this dataset contains
rows, columns = datafile.shape
print(f"Number of rows: {rows}")
print(f"Number of columns: {columns}")
print()

#Convert 'time' column to datetime objects
datafile['time']=pd.to_datetime(datafile['time'])
print(datafile)


#Creater new columns for Year and Month 
datafile['year']=datafile['time'].dt.year
datafile['month']=datafile['time'].dt.month
print(datafile)


yearly_view=datafile.groupby('year')['value'].sum().reset_index()

yearly_view.column=['Year','Total_value']
print(yearly_view)

#Month/per year 
monthly_totals = datafile.groupby(['year','month'])['value'].sum().reset_index()
monthly_totals.columns=['Year','Month','Total_value']
print(monthly_totals)

#Change display to show all data files and confirm data displays correctly
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns', None)

#Save data to CSV file
monthly_totals.to_csv('monthly_streamflow_totals_per_year.csv',index=False)

yearly_summary_streamflow=datafile.groupby(datafile['time'].dt.year).agg(
    Minimum_Value=('value','min'),
    Maximum_Value=('value','max'),
    Average_value=('value', 'mean'), 
    Kurtosis_value=('value','kurt'),
    Skewness_value=('value','skew'), 
    Standard_value=('value','std')   
).reset_index()

yearly_summary_streamflow.rename(columns={'time':'Year'}, inplace=True)
print(yearly_summary_streamflow)

#Save data to CSV file
yearly_summary_streamflow.to_csv('yearly_streamflow_summary.csv',index=False)

#print(datafile[['time','year','month','year_month']])

############################################################################################
##All years 

overall_summary = datafile.agg(
    Overall_Minimum=('value','min'),
    Overall_Maximum=('value','max'),
    Overall_Average=('value','mean'),
    Overall_Kurtosis=('value','kurt'),
    Overall_Skewness=('value','skew'),
    Overall_Standard_Dev=('value','std')
).T

print("Overall Historical Statistics")
print(overall_summary)

#Save data to CSV file
overall_summary.to_csv('Historical_Summary_Streamflow.csv',index=False)