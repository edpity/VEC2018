import os #Required to change directory
os.chdir('GitHubLocation/VEC2018/scraper/data/xml') #Set directory - you will need to set this manually!!!
import lxml
from lxml import etree
import xml.etree.ElementTree as ET #Will parse xml
import csv #To export
import requests #Requests will be used for the VEC site, not utilised at this stage
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
tree = ET.parse('Data.xml') #Loads file
root = tree.getroot() #Sets 'root' as the highest level of the XML file

scope = ['https://spreadsheets.google.com/feeds'+ ' ' +'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope) #Requires a json file with Google permissions
client = gspread.authorize(creds)

Spreadsheet = client.open('') #Need to set the name of the Google Sheet
Worksheet = Spreadsheet.worksheet('') #Need to set name of the active tab in the Google Sheet
SpreadsheetID = '' #Need to set the ID of the sheet (found in the URL)

if os.path.exists('Data.csv'):
    os.remove('Data.csv')


TagSlug = '{http://www.vec.vic.gov.au}'
EMLTag = '{urn:oasis:names:tc:evs:schema:eml}'

Election = root.find(TagSlug+'Election')
House = Election.find(TagSlug+'House')
Contests = House.find(TagSlug+'Contests')
for Contest in Contests.findall(TagSlug+'Contest'):
    PollingDistrictID = Contest.find(TagSlug+'PollingDistrictIdentifier')
    PollingDistrictName = PollingDistrictID.find(TagSlug+'Name')
    PollingPlaces = Contest.find(TagSlug+'PollingPlaces')
    for PollingPlace in PollingPlaces.findall(TagSlug+'PollingPlace'):
        PollingPlaceID = PollingPlace.find(TagSlug+'PollingPlaceIdentifier')
        FirstPrefs = PollingPlace.find(TagSlug+'FirstPreferences')
        for Candidate in FirstPrefs.findall(TagSlug+'Candidate'):
            CandidateID = Candidate.find(EMLTag+'CandidateIdentifier')
            Votes = Candidate.find(TagSlug+'Votes')
            Data = (PollingDistrictName.text, PollingPlaceID.attrib['Id'], FirstPrefs.attrib['Updated'], CandidateID.attrib['Id'], Votes.text)
            os.chdir('GitHubLocation/VEC2018/scraper/output')
            csvfile = 'Data.csv'
            with open (csvfile, 'a', encoding='utf-8') as PrintData:
                Print = csv.writer(PrintData)
                Print.writerow(Data)

time.sleep(10)
csv = open('Data.csv', 'r').read()
client.import_csv(SpreadsheetID, csv)
print('Done')

            #print(PollingDistrictName.text, PollingPlaceID.attrib['Id'], FirstPrefs.attrib['Updated'], CandidateID.attrib['Id'], Votes.text)

        
