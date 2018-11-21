import os #Required to change directory
os.chdir('GitHubLocation/VEC2018/scraper/set-up') #Set directory - you will need to set this manually!!!
import lxml
from lxml import etree
import xml.etree.ElementTree as ET #Will parse xml
import requests #Requests will be used for the VEC site, not utilised at this stage
tree = ET.parse('State2018MediaFileGroupsAndTickets.xml') #Loads file
root = tree.getroot() #Sets 'root' as the highest level of the XML file

TagSlug = '{http://www.aec.gov.au/xml/schema/mediafeed}'

Election = root.find(TagSlug+'Election') #Goes from level 0 (root) to level 1 (CandidateList)
Contests = Election.find(TagSlug+'Contests')
for Contest in Contests.findall(TagSlug+'Contest'):
    ContestNav = Contest.find(TagSlug+'eml:ContestIdentifier')
    ContestName = ContestNav.find(TagSlug+'eml:ContestName')
    for Group in Contest.findall(TagSlug+'Group'):
        GroupID = Group.find(TagSlug+'GroupIdentifier')
        PartyName = GroupID.find(TagSlug+'GroupName')
        Candidate = Group.find(TagSlug+'Candidate')
        NoOfCandidates = Candidate.find(TagSlug+'BallotPosition')
        print(NoOfCandidate.text)
