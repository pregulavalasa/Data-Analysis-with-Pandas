import pandas as pd

#collecting years from user
start_year_str = input("Enter the start year: (Between 1951 and 2017) \n")
end_year_str = input("Enter the end year: (After start year and before 2017) \n")
start_year = int(start_year_str)
end_year = int(end_year_str)

#initializing an empty dataframe
df = pd.DataFrame()

#initializing the list of the years
years = range(start_year, end_year+1, 1)

#loop for bringing all the files without the headers together in the year range requested by user
for i in years:
	data = pd.read_csv('total_precipitation_'+str(i)+'.txt', sep=";", header=None)
	data = data.transpose()
	data = data.iloc[1: , :]
	#print(data)
	df = df.append(data)

#converting the rain column to a float
rain = pd.to_numeric(df[1])

#printing the sum
print(rain.sum())
