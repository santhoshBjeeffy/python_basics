# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 20:12:47 2018

@author: santhob
"""

import requests
import bs4
res=requests.get('https://github.com/docker-library/python/issues/110 ')
type(res)
res.text
soup=bs4.BeautifulSoup(res.text,'lxml')
with open (r"C:\Users\santhob\test12.txt", "w") as oFile:
     oFile.write(str(soup.html))
     oFile.close()