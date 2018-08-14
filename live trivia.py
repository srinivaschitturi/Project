# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 21:50:57 2018

@author: srini
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 17:11:07 2018

@author: srini
"""

from PIL import Image
import pytesseract
import webbrowser
#import robobrowser
from bs4 import BeautifulSoup, SoupStrainer
import urllib.request  as urllib2 
from lxml import html
import httplib2
import os
#import re
path='C:\\Users\\srini\\Documents\\AirDroid\\ScreenShot\\MotoG3_ScreenShot_20180711.jpg'
img=Image.open(path)
#img=Image.open('C:\\Users\\srini\\Downloads\\bigmac.png')
question=img.crop((50,430,650,637))
option1=img.crop((120,640,600,790))
option2=img.crop((120,790,600,940))
option3=img.crop((120,940,600,1090))

#question=img.crop((50,460,650,667))
#option1=img.crop((120,670,600,820))
#option2=img.crop((120,820,600,970))
#option3=img.crop((120,970,600,1120))
#img.save('C:\\Users\\srini\\Documents\\AirDroid\\ScreenShot\\MotoG3_ScreenShot_20180612.jpg', dpi=(600,600))

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
questiontext=pytesseract.image_to_string(question)
option1text=pytesseract.image_to_string(option1)
option2text=pytesseract.image_to_string(option2)
option3text=pytesseract.image_to_string(option3)
url1='http://www.google.com/search?q=';
url2='http://www.bing.com/search?q=';
url1=url1+questiontext
url2=url2+questiontext
webbrowser.open_new_tab(url1)
#url1='https://www.bing.com/search?q=what?Federalist%20Papers&gws_rd=ssl'
##rawdata=re.findall('<body>(.*?)</body>', url1, re.DOTALL)

count1=0
count2=0
count3=0

http=httplib2.Http()
status, response = http.request(url2)

soup = BeautifulSoup(response,"lxml")
links = soup.find_all('div',attrs={'class': 'b_attribution'})
for link in links:
    useful_link = link.get_text()
    status, response1 = http.request(useful_link)
    soups = BeautifulSoup(response1,"lxml")
    count1 = count1 + soups.body.findAll(text=option1text)
    count2 = count2 + soups.body.findAll(text=option2text)
    count3 = count3 + soups.body.findAll(text=option3text)

print(count1)
print(count2)
print(count3)
os.remove(path)
#for link in links:
#    if 'http' or 'https' in link:
#        useful_link.append(link)
#print(useful_link)
#tree=html.fromstring(page.content)
#data = tree.xpath('//body')
#print("My blog title is: '{}'".format(data[0].text.strip()))
##rawData=bs4.BeautifulSoup(page,"html.parser").find('body')