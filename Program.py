
# coding: utf-8

# In[ ]:


import gspread
import gspread_dataframe as gd
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("/home/future/Downloads/spreadsheetexample.json", scope) #replace spreadsheetexample.json with actual json file which you downloaded

gc = gspread.authorize(credentials)
ws = gc.open("Test").sheet1 #change "you can change it to desired worksheet name by replacing sheet1

#gspread
#existing = gd.get_as_dataframe(ws)
df = gd.get_as_dataframe(ws).dropna(axis=1,how="all").dropna(axis=0,how="all")

choice = input("Do u want to make changes to the Worksheet?").upper()[0]
if choice in "Y":
    gd.set_with_dataframe(ws, df)
    print("Datasheet Updated")
else:
    print("Restart")

