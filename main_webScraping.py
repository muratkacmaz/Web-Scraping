#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 17:21:49 2018

@author: muratkacmaz
"""

import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup




quote_page = 'https://yokatlas.yok.gov.tr/lisans-bolum.php?b=10024'




dataName = []
dataLink = []
dataKontenjan = []
 # query the website and return the html to the variable ‘page’
page = urlopen(quote_page)
# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
name_box = soup.find_all('div', attrs={'style': 'overflow: hidden; text-overflow: ellipsis; white-space: nowrap;width:80%'})
link_box = soup.find_all('a', attrs={'data-parent': '#'})
for a in link_box:
    dataLink.append(a['href'])
for i in name_box:
    name = i.text.strip() 
    dataName.append(name)
    
    
for i in range (259):
    quote_page = 'https://yokatlas.yok.gov.tr/' + dataLink[i]
    page = urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    div = soup.find_all('div',attrs = {'id':'icerik_1000_2'})
    td = soup.find_all('table')
    #td = soup.find('td',attrs= {'class':'tdr text-center'})
    for j in td:
        print(j)

    
    
        

    
    

