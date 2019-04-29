# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 08:19:41 2018

@author: Home
"""

import matplotlib.pyplot as plt
import requests as r

#import json

distanceList = []
stepList = [] 
#Your ThingSpeak channel API key and channel number
url = 'https://api.thingspeak.com/channels/XXXXXX/feeds.json?api_key=XXXXXXXXXXXXXXXX&results=16'

r = r.get(url)

print("Status: ", r.status_code)

rDict = r.json()

for data in rDict["feeds"]:
    distanceList.append(float(data["field1"]))
    stepList.append(int(data["field2"]))


#with open('UltralydData.json', 'w') as filObjekt:
#    json.dump(rDict, filObjekt, indent=4)
#
#
#with open('UltralydData', 'r') as filObjekt:
#    UltralydDataDict = json.load(filObjekt)
    
plt.plot(stepList, distanceList)
plt.ylabel('Distance')
plt.xlabel("Steps")
plt.show()
    
    
    
    
