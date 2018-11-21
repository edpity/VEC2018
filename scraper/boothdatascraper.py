import os #Required to change directory
os.chdir('GitHubLocation/VEC2018/scraper/set-up') #Set directory
import lxml
from lxml import etree
import xml.etree.ElementTree as ET #Will parse xml
import csv #To export
import requests #Requests will be used for the VEC site, not utilised at this stage
tree = ET.parse('State2018MediaFilePollingLocations.xml') #Loads file
root = tree.getroot()


TagSlug = '{http://www.aec.gov.au/xml/schema/mediafeed}' #This is pre-appended all nodes so saves space

PollingDistricts = root.findall(TagSlug+'PollingDistrict') #Goes from level 0 (root) to level 1 (PollingDistrict)
for PollingDistrict in PollingDistricts: #Required otherwise only the first district would display
    DistrictID = PollingDistrict.find(TagSlug+'PollingDistrictIdentifier') #Finds the district ID
    Name = DistrictID.find(TagSlug+'Name') #Finds the name of each electorate (as a child of DistrictID)
    PollingPlaces = PollingDistrict.find(TagSlug+'PollingPlaces') 
    PollingPlace = PollingPlaces.find(TagSlug+'PollingPlace') #These two lines are ONLY for navigating the XML file
    for PollingPlace in PollingPlaces: #Required otherwise it would only print the first booth in each electorate
        PPID = PollingPlace.find(TagSlug+'PollingPlaceIdentifier') #Finds both the booth ID and name
        Data = (PPID.attrib['Id'], PPID.attrib['Name'], DistrictID.attrib['Id'], Name.text)
        csvfile = 'boothdata.csv'
        with open (csvfile, 'a', encoding='utf-8') as CandidateData:
            Print = csv.writer(CandidateData)
            Print.writerow(Data)
        #print(PPID.attrib['Id'], PPID.attrib['Name'], DistrictID.attrib['Id'], Name.text) #Prints the text
