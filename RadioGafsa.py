from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
page_link_list=[]
link_list=[]
type_list=[]
article_list=[]
article_title_list=[]

for i in range(3):
  page_link_list.append("http://www.radiogafsa.tn/all-news/"+str(i+1)+"/")

for i in page_link_list :   #extracing (link , type ) of each article
  # URl to web scrap from.
  # in this example we web scrap graphics cards from Newegg.com
 
  
  # opens the connection and downloads html page from url
  uClient = uReq(i)
  print('Scraping in progress ...')
  # parses html into a soup data structure to traverse html
  page_soup = soup(uClient.read(), "html.parser")
  uClient.close()
  #finds each Article 
  containers = page_soup.findAll("ul", {"class": "mediaHeadingList _M20"})
  container = containers[0].findAll("li")    #list contains the html code of each article
 
 
  for con in container:
    #con contains the code of  one article 
   
    link=con.a["href"]  
    link_list.append(link)     #fils link_list with all articles links
     
    article_title_list.append(con.h1.text)



for i in range(len(link_list)):  
  #Scraping One Page Code    
  uClient = uReq(link_list[i])
  page_soup = soup(uClient.read(), "html.parser")
  uClient.close()
  containers = page_soup.findAll("article")
  ch=containers[0].findAll("section")[0].p.text
  article_list.append(ch)
  print(str(i+1)+"of"+str(len(link_list)) +" :DONE")


import pandas as pd 
data={  'title' : article_title_list , 'article' : article_list ,'link'  : link_list  }
df = pd.DataFrame (data, columns = ['link','title','article'])
import numpy as np
df["type"]= np.nan


df.to_csv('RadioGafsaAR.csv' ,encoding='utf-8-sig')









