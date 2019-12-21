import gspread
import gspread_dataframe as gd
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

df = pd.DataFrame()

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]

#replace spreadsheetexample.json with actual json file which you downloaded
#the link for setting up and getting the json file is provided in the readme
credentials = ServiceAccountCredentials.from_json_keyfile_name("your_file_path_here", scope) 
gc = gspread.authorize(credentials)

#replace the name in between the gc.open parenthesis  with the name of your spreadsheet
ws = gc.open("name_of_your_google_spreadsheet").sheet1 #change "you can change it to desired worksheet name by replacing sheet1

#gspread
#existing = gd.get_as_dataframe(ws)
df = gd.get_as_dataframe(ws).dropna(axis=1,how="all").dropna(axis=0,how="all")

choice = input("Do u want to make changes to the Worksheet?").upper()[0]
if choice in "Y":
    gd.set_with_dataframe(ws, df)
    print("Datasheet Updated")
else:
    print("Restart")

df
