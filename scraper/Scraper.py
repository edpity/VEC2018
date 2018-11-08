import os ###Required to change directory
os.chdir('C:/Users/eggy2/Documents/GitHub/VEC2018/scraper/set-up') ###Set directory
import lxml
from lxml import etree
import xml.etree.ElementTree as ET ###Will parse xml
import requests ###Requests will be used for the VEC site, not utilised at this stage
tree = ET.ElementTree(file='State2018MediaFilePollingLocations.xml') ###Loads file
root = tree.getroot()

TagSlug = '{http://www.aec.gov.au/xml/schema/mediafeed}' ###Required to append root name

PollingDistricts = root.findall(TagSlug+'PollingDistrict')
for PollingDistrict in PollingDistricts:
    DistrictID = PollingDistrict.find(TagSlug+'PollingDistrictIdentifier')
    Name = DistrictID.find(TagSlug+'Name')
    print(DistrictID.attrib['Id'], Name.text)
    
    ###Should print electorates and their IDs


