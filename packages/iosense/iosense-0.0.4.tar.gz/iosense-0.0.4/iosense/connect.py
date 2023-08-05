"""
This module implements the main data access functionalities of I/O Sense
Author: Rishi Sharma from Faclon Labs
"""

__author__ = "Rishi Sharma, Faclon Labs Private Limited"
__email__ = "rishi.sharma@faclon.com"
__status__ = "development"


import pandas as pd
import requests
import json
import time
import datetime


class dataAccess:
    
    def __init__(self, apikey, url):
        self.apikey= apikey
        self.url= url
        
    def getDP(self, device_id, sensors=None, n = 1, cal = None):
        url = "https://"+self.url+"/api/apiLayer/lastDP?device="+device_id+"&sensor="+sensors
        header = {'apikey': self.apikey}
        payload = {}
        response = requests.request('GET', url, headers=header, data=payload, verify=False)
        return response.text
    
    def query_time(self, device_id, start_time, end_time = time.time(), sensors = None , cal = None):
      s_time = pd.to_datetime(start_time)
      st_time = int(round(s_time.timestamp())) * 1000000000
      e_time = pd.to_datetime(end_time)
      en_time = int(round(e_time.timestamp())) * 1000000000

      header = {'apikey': self.apikey}
      payload = {}
      qq = pd.DataFrame()
      count = 0
      if sensors is None:
        url = "https://"+self.url+"/api/apiLayer/getDataByStEt?device="
        # url = "https://data.iosense.io/api/apiLayer/getDataByStEt?device="
      else:
        for i in sensors:
          if i == ",":
            count += 1
        if count == 0:
          url = "https://"+self.url+"/api/apiLayer/getData?device="
          # url = "https://data.iosense.io/api/apiLayer/getData?device="
        else:
          url = "https://"+self.url+"/api/apiLayer/getAllData?device="
          # url = "https://data.iosense.io/api/apiLayer/getAllData?device="
      a = 0 
      cursor = {'start': st_time, 'end': en_time}
      while True:
        if sensors is None:
          if a == 0:
            temp = url +device_id+"&sTime="+str(st_time)+"&eTime="+str(en_time)+"&cursor=true"
          else:
            temp= url+device_id+"&sTime="+str(cursor['start'])+"&eTime="+str(cursor['end'])+"&cursor=true"
        elif a == 0 and sensors != None:
          temp = url+device_id+"&sensor="+sensors+"&sTime="+str(st_time)+"&eTime="+str(en_time)+"&cursor=true"
        else:
          temp = url+device_id+"&sensor="+sensors+"&sTime="+str(cursor['start'])+"&eTime="+str(cursor['end'])+"&cursor=true"
        response = requests.request("GET", temp, headers=header, data=payload)
        rawData = json.loads(response.text)['data']
        cursor = json.loads(response.text)['cursor']
        a += 1
        qq = pd.DataFrame(rawData)
        if cursor['start'] == None or cursor['end'] == None:
          return qq
          break

     



