'''from weather import Weather, Unit
weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('bengaluru')
condition = location.condition
print(condition.text)'''


from weather import Weather, Unit
import pandas as pd 

weather = Weather(unit=Unit.CELSIUS)

location = weather.lookup_by_location('bengaluru')
forecasts = location.forecast
for forecast in forecasts:
    print(forecast.text)
    for i in range(forecast.date,(0,3))	
    	print(forecast.date)
    	print("maximum temp",forecast.high,"C")
    	print("minimum temp",forecast.low,"C")

'''import calendar 
yy=2019
print(calendar.calendar(yy))''' 


'''from datetime import date 
import holidays

India_holidays = holidays.India() 
  

for ptr in holidays.India(years = 2019).items(): 

    print(ptr) '''

