#package import statement
from smartapi import SmartConnect
from smartapi import WebSocket
import pandas as pd
import csv
#create object of call
try:
    obj=SmartConnect(api_key="")
    #login api call
    data = obj.generateSession("","")
    refreshToken= data['data']['refreshToken']
    #fetch the feedtoken
    feedToken=obj.getfeedToken()
    #fetch User Profile
    userProfile= obj.getProfile(refreshToken)
except Exception as e:
    print("Login Failed: {}".format(e.message))
#symboltoken : check your instrument on this site. "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
try:
    historicParam={
    "exchange": "NSE",
    "symboltoken": "3045",
    "interval": "ONE_MINUTE",
    "fromdate": "2021-03-01 09:15", 
    "todate": "2021-03-31 15:30"
    }
    data_csv = obj.getCandleData(historicParam)
    arr = data_csv['data'].split("\n")
    with open("data.csv","w",newline='') as file:
        writer = csv.writer(file)
        for i in arr:
            i = i.split(",")
            writer.writerow(i)
except Exception as e:
    print("Historic Api failed: {}".format(e.message))
    
try:
    logout=obj.terminateSession('')
    print("Logout Successfull")
except Exception as e:
    print("Logout failed: {}".format(e.message))    
