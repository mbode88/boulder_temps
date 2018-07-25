import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Import data, grab only data points from years 1900-2018
print('importing the data')
df_precip=pd.read_excel('/Users/marcbode/github/boulder_temps/data/precip_data.xlsx',index_col=0,header=0)
df_precip=df_precip.loc[1900:2018]
df_min=pd.read_excel('/Users/marcbode/github/boulder_temps/data/min_temp.xlsx',index_col=0)
df_min=df_min.loc[1900:2018]
df_max=pd.read_excel('/Users/marcbode/github/boulder_temps/data/max_data.xlsx',index_col=0)
df_max=df_max.loc[1900:2018]

#Clean up the data a bit...
df_precip.loc[1990,'JAN']=1.4
df_max.replace('X',np.nan,inplace=True)
df_min.replace('Miss',np.nan,inplace=True)
df_precip.replace('Tr',np.nan,inplace=True)

#Calculate a mean parameter for max and min dataframes
df_max['Mean']=df_max.mean(axis=1)
df_min['Mean']=df_min.mean(axis=1)

#Plot the data
print('Plotting the data')
fig,ax = plt.subplots(figsize=(15,10))
ax.plot(df_max.index,df_max['Mean'],label='Annual Average High')

#Create logistic fits for each dataset (max and min)
print('Creating fit for max')
fit_max = np.polyfit(df_max.Mean.dropna().index, df_max['Mean'].dropna(), deg=1)
print('...done')
ax.plot(df_max.index, fit_max[0] * df_max.index + fit_max[1], color='red',label='Trending High, slope = {:04.3f}'.format(fit_max[0]))
ax.plot(df_min.index,df_min['Mean'],label='Annual Average Low')
print('Creating fit for min')
fit_min = np.polyfit(df_min.Mean.dropna().index, df_min['Mean'].dropna(), deg=1)
print('...done')

#Plot the remaining plot features including titles and legends
print('More plotting....')
ax.plot(df_min.index, fit_min[0] * df_min.index + fit_min[1], color='blue',label = 'Trending Low, slope = {:04.3f}'.format(fit_min[0]))
print('Creating legend')
ax.legend(frameon=False)
print('Creating titles')
ax.set_title('Effects of Global Warming on Temperature Divergence (Boulder, Colorado)',fontweight='bold')
ax.titlesize='large'
ax.set_xlabel('Year')
ax.set_ylabel('Temperature (Deg F)')
plt.show()
print('done')
