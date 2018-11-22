import os #Required to change directory
os.chdir('GitHubLocation/VEC2018/scraper/set-up') #Set directory - you will need to set this manually!!!
import lxml
from lxml import etree
import xml.etree.ElementTree as ET #Will parse xml
import csv #To export
import requests #Requests will be used for the VEC site, not utilised at this stage
tree = ET.parse('State2018MediaFileCandidates.xml') #Loads file
root = tree.getroot() #Sets 'root' as the highest level of the XML file

TagSlug = '{urn:oasis:names:tc:evs:schema:eml}' #This is pre-appended all nodes so saves space

CandidateList = root.find(TagSlug+'CandidateList') #Goes from level 0 (root) to level 1 (CandidateList)
for Election in CandidateList.findall(TagSlug+'Election'):
    ElectionID = Election.find(TagSlug+'ElectionIdentifier')
    ElectionName = ElectionID.find(TagSlug+'ElectionName') 
    for Contest in Election.findall(TagSlug+'Contest'):
        ContestID = Contest.find(TagSlug+'ContestIdentifier')
        ContestName = ContestID.find(TagSlug+'ContestName')
        PollingDistrictID = Contest.find(TagSlug+'PollingDistrictIdentifier') #Basically, this block of code is used either to go a layer deeper to reach data we want, to define data we want, or both
        Enrolment = Contest.find(TagSlug+'Enrolment')
        for Candidate in Contest.findall(TagSlug+'Candidate'):
            CandidateID = Candidate.find(TagSlug+'CandidateIdentifier')
            CandidateName = CandidateID.find(TagSlug+'CandidateName')
            if Candidate.attrib['Independent'] == 'no':
                Affiliation = Candidate.find(TagSlug+'Affiliation')
                AffiliationID = Affiliation.find(TagSlug+'AffiliationIdentifier')
                Party = AffiliationID.find(TagSlug+'RegisteredName') 
            else:   #This is needed, otherwise the script would break on the first independent
                Party.text = 'INDEPENDENT'
            BallotPos = Candidate.find(TagSlug+'BallotPosition')
            Data = (ElectionName.text, ContestID.attrib['Id'], ContestName.text, Enrolment.text, CandidateID.attrib['Id'], CandidateName.text, Party.text, BallotPos.text)
            csvfile = 'candidatedata.csv'
            with open (csvfile, 'a', encoding='utf-8') as CandidateData:
                Print = csv.writer(CandidateData)
                Print.writerow(Data)
                #print(ElectionName.text, ContestID.attrib['Id'], ContestName.text, Enrolment.text, CandidateID.attrib['Id'], CandidateName.text, Party.text, BallotPos.text) #Prints out these values

