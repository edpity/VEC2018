import os #Required to change directory
os.chdir('GitHubLocation/VEC2018/scraper/data/xml') #Set directory - you will need to set this manually!!!
import lxml
from lxml import etree
import xml.etree.ElementTree as ET #Will parse xml
import csv #To export
import requests #Requests will be used for the VEC site, not utilised at this stage
tree = ET.parse('Data.xml') #Loads file
root = tree.getroot() #Sets 'root' as the highest level of the XML file

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
            print(PollingDistrictName.text, PollingPlaceID.attrib['Id'], FirstPrefs.attrib['Updated'], CandidateID.attrib['Id'], Votes.text)

        
