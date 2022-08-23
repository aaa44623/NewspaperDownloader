'''
Ahmed Mohammed AL Balushi
Oman and Al-Watan Newspaper downloader application
أحمد بن محمد البلوشي
برنامج يقوم بتنزيل جريدة الوطن وجريدة عمان بتاريخ اليوم   
'''

# Import the necessary libraries need to execute this tool
from ast import And, Try
from asyncio.windows_events import NULL
from cgi import print_exception
from logging import exception
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import urllib.request
import sys
import urllib.request 
import datetime
import wget

## Two Urls for Two different Newspapers
url = 'https://www.omandaily.om/%D8%A7%D9%84%D8%B5%D9%81%D8%AD%D8%A7%D8%AA-%D8%A7%D9%84%D9%83%D8%A7%D9%85%D9%84%D8%A9'
urlTwo = 'https://epaper.alwatan.com/'

## Method to check if the provided URL is valid
## Unnecessary Since Website is Unchanged
def check_validity(url):
    try:
        urllib.request.urlopen(url)
        print("Valid URL ")
    except IOError:
        print ("Invalid URL")
        sys.exit()

#First Method to Get Grab and Download Oman NewsPaper 
# The Designated Method for Url One
def get_pdfs(url):
    html = urllib.request.urlopen(url).read()
    html_page = BeautifulSoup(html, features="lxml") 
    base = urlparse(url)
    print("base",base)                  #print the Specs of the Parsed Website

    d = datetime.date.today()           #Grab todays Date format YYYY/MM/DD
    dateStr = d.strftime("%Y/%m/%d")    #Cast the Date into String 
    current_link = None                 #Set the Current_Link to None initially to Avoid the TypeError When Checking 

    for link in html_page.find_all('a'): #Find all the links in the parsed page
        current_link = link.get('href')

        #check if the href link has both 'pdf' and today's date
        if current_link != None and ('pdf/'+ dateStr) in current_link: 
        
            try:
                wget.download("https://www.omandaily.om"+current_link) #Download The link if it is valid
            except:
                print_exception         #Exception incase trouble getting the link

####################### BREAK LINE BETWEEN 2 METHODS #########################

#Second Method to grab Toays Al-Watan Newspaper
def get_pdfsTwo(urlTwo):
    html = urllib.request.urlopen(urlTwo).read()
    html_page = BeautifulSoup(html, features="lxml") 
    base = urlparse(urlTwo)
    print("base",base)                  #print the Specs of the Parsed Website

    for link in html_page.find_all('a'): #Find all the links in the parsed page
        current_link = link.get('href') 
        
        if ('/index/download-publication/id/') in current_link:
        #check if the href link has the above text in it and verify
            try:
                wget.download('https://epaper.alwatan.com'+current_link) #Download The link if it is valid
            
            except: 
                print_exception         #Exception incase trouble getting the link



## Main Method
def main():
    print("Goooood Morning \nStarting To Download todays Newspaper")

    # Checking Both Url Validity
    check_validity(urlTwo)
    check_validity(url)

    #Starting to Download pdfs
    get_pdfsTwo(urlTwo)
    get_pdfs(url)

    #Downlaod Complete
    print("\nOperation Complete \n Have a Wonderful Day")
    text = "يومك سعيد".encode("utf-8")
    
#Call Main Method
main()