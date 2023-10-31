# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 13:09:32 2023

@author: hp
"""

import json
import requests
import pprint
import pandas as pd
url = "https://www.marinespecies.org/rest/AphiaRecordByAphiaID/138675"
r = requests.get(url)
#print(r.text)
print(type(r.json()))
data = r.json()
pprint.pprint(data)

df = pd.json_normalize(data) 

# Save to Excel
filepath = 'output.xlsx'  
df.to_excel(filepath, index=False)  
print(f"Data saved to {filepath}")
