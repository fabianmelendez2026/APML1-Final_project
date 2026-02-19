#Steamflow Stat anaylysis

#install pandas, matplotlib, and seaborn for plots
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


datafile = pd.read_csv('Precip_and_Temp.csv')

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

#Convert 'DATE' column to datetime objects
datafile['DATE']=pd.to_datetime(datafile['DATE'])
print(datafile)


#Creater new columns for Year and Month 
datafile['year']=datafile['DATE'].dt.year
datafile['month']=datafile['DATE'].dt.month
print(datafile)

#group by year and sum the PRCP column
monthly_prcp=datafile.groupby(['year','month'])['PRCP'].sum().reset_index()
annual_prcp=datafile.groupby('year')['PRCP'].sum().reset_index()

#rename columns for report 
monthly_prcp.columns=['Year','Month','Total_Monthly_PRCP']
annual_prcp.columns = ['Year','Total Annual Precipation']
print(monthly_prcp)
print(annual_prcp)

yearly_summary_prcp=datafile.groupby('year').agg(
    Minimum_Value=('PRCP','min'),
    Maximum_Value=('PRCP','max'),
    Average_value=('PRCP', 'mean'), 
    Kurtosis_value=('PRCP','kurt'),
    Skewness_value=('PRCP','skew'), 
    Standard_value=('PRCP','std')   
).reset_index()
print("Yearly Precipation Metrics")
yearly_summary_prcp.rename(columns={'year':'Year'}, inplace=True)
print(yearly_summary_prcp)

#Save data to CSV file
yearly_summary_prcp.to_csv('yearly_PRCP_summary.csv',index=False)

#Historical Annual Statistics for Precipitation
##All years 

overall_summary = datafile.agg(
    Overall_Minimum=('PRCP','min'),
    Overall_Maximum=('PRCP','max'),
    Overall_Average=('PRCP','mean'),
    Overall_Kurtosis=('PRCP','kurt'),
    Overall_Skewness=('PRCP','skew'),
    Overall_Standard_Dev=('PRCP','std')
).T

print("Overall Historical Precipitation Statistics")
print(overall_summary)
overall_summary.to_csv('Overall_Precipitation_summary.csv',index=False)

#Save data to CSV file
overall_summary.to_csv('Historical_Summary_Precipitation.csv',index=False)



########################################################################################################

#Temp Data 

monthly_temp_extremes = datafile.groupby(['year','month']).agg(
    Monthly_max_temp=('TMAX','max'),
    Monthly_min_Temp=('TMIN','min')).reset_index()

print("Monthly Extremes")
print(monthly_temp_extremes.head())

yearly_temp_extremes =datafile.groupby('year').agg(
    Yearly_max_temp=('TMAX','max'),
    Yearly_min_Temp=('TMIN','min')
).reset_index()

print("Yearly Extremes")
print(yearly_temp_extremes)

yearly_summary_MaxTemp=datafile.groupby('year').agg(
    Minimum_Value=('TMAX','min'),
    Maximum_Value=('TMAX','max'),
    Average_value=('TMAX', 'mean'), 
    Kurtosis_value=('TMAX','kurt'),
    Skewness_value=('TMAX','skew'), 
    Standard_value=('TMAX','std')   
).reset_index()

print("Temp Metrics per year")
yearly_summary_MaxTemp.rename(columns={'year':'Year'}, inplace=True)
print(yearly_summary_MaxTemp)

#Save data to CSV file
yearly_summary_MaxTemp.to_csv('yearly_MaxTemp_summary.csv',index=False)

#Historical Annual Statistics for MaxTemp
##All years 

overall_summary = datafile.agg(
    Overall_Minimum=('TMAX','min'),
    Overall_Maximum=('TMAX','max'),
    Overall_Average=('TMAX','mean'),
    Overall_Kurtosis=('TMAX','kurt'),
    Overall_Skewness=('TMAX','skew'),
    Overall_Standard_Dev=('TMAX','std')
).T
print("Overall Historical TMAX Statistics")
print(overall_summary)
overall_summary.to_csv('Overall_TMAX_summary.csv',index=False)

#Save data to CSV file
overall_summary.to_csv('Historical_Summary_TMAX.csv',index=False)


#################################################################################################
print('TMIN Per Year Metrics')
yearly_summary_MinTemp=datafile.groupby('year').agg(
    Minimum_Value=('TMIN','min'),
    Maximum_Value=('TMIN','max'),
    Average_value=('TMIN', 'mean'), 
    Kurtosis_value=('TMIN','kurt'),
    Skewness_value=('TMIN','skew'), 
    Standard_value=('TMIN','std')   
).reset_index()

yearly_summary_MinTemp.rename(columns={'year':'Year'}, inplace=True)
print(yearly_summary_MaxTemp)

#Save data to CSV file
yearly_summary_MinTemp.to_csv('yearly_MinTemp_summary.csv',index=False)

#Historical Annual Statistics for MinTemp
##All years 
print("Historical Annual Statistics for MinTemp")
overall_summary = datafile.agg(
    Overall_Minimum=('TMIN','min'),
    Overall_Maximum=('TMIN','max'),
    Overall_Average=('TMIN','mean'),
    Overall_Kurtosis=('TMIN','kurt'),
    Overall_Skewness=('TMIN','skew'),
    Overall_Standard_Dev=('TMIN','std')
).T
print("Overall Historical TMIN Statistics")
print(overall_summary)
overall_summary.to_csv('Overall_TMIN_summary.csv',index=False)

#Save data to CSV file
overall_summary.to_csv('Historical_Summary_TMIN.csv',index=False)