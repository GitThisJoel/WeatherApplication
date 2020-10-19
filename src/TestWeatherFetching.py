import os
import json
import requests

# variables for the get operation
cat = 'pmp3g'
ver = 2
long = 13
lat = 56

# where the data is comming from
getAddress = '/api/category/{category}/version/{version}/geotype/point/lon/{longitude}/lat/{latitude}/data.json'.format(category = cat, version = ver, longitude = long, latitude = lat)
url = 'https://opendata-download-metfcst.smhi.se' + getAddress

def filepath():
    # the wheter data is stored (json format)
    filepath = os.path.dirname(os.path.realpath(__file__))
    return filepath + '/data.json'

def fetchWeatherData():
    r = requests.get(url)
    return json.loads(r.text)
    # print(json.dumps(allData['timeSeries'][1]['parameters'][0]['values'][0], indent=2))

# index of relevant information from the fetched weather data
# 1 = temp
# 3 = were the wind is blowing
# 4 = wind speed
# 18 = weather icon
infoIndex = [1, 3, 4, 18]
tempAndWind = [1,4]

def showWeatherNow():
    allData = fetchWeatherData()
    weatherInfo = allData['timeSeries'][1]['parameters']
    for i in tempAndWind:
        param = weatherInfo[i]
        print("{} {}".format(param['values'][0], param['unit']))

# 2020-10-19T20:00:00Z
def showWeatherTenHours():
    allData = fetchWeatherData()
    for i in range(10):
        weatherInfo = allData['timeSeries'][i+1]['parameters']
        validTime = allData['timeSeries'][i+1]['validTime']
        print(validTime[11:19])
        for j in tempAndWind:
            param = weatherInfo[j]
            print("{} {}".format(param['values'][0], param['unit']))
        print('')
