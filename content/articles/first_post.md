Title: Exploring Weather Trends
Tags: sql, excel, project
Slug: weather_trends
Summary:
Date: 2019-11-03
#Project 1: Exploring Weather Trends
### Step 1: Extract data
The data for this project was held within the `city_list` database. I chose to compare the average temperatures of Chicago compared to global averages. My SQL queries were quite simple:
```
	SELECT * FROM city_list
	SELECT * FROM city_data where city=’Chicago’
	SELECt * FROM global_data
```
I then uploaded the csv files [here](https://docs.google.com/spreadsheets/d/1X47j_FE1cy8g1UpGpGc_GJoBp3aPhkCRWGyTGW3VGNY/edit?usp=sharing "Exploring Weather Trends") and began my analysis.
### Step 2: Calculate moving averages
I decided to use a 10 year moving average for both Chicago and global temps, as this seemed to smooth out the "noise" without taking away major fluctuations.
### Step 3: Display data
I loaded the data into a line chart and added trend lines.
The result:  
![Chart]({filename}/images/temp.png)
