from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
page_link_list=[]
link_list=[]
type_list=[]
article_list=[]
article_title_list=[]

for i in range(2):
  page_link_list.append("https://lapresse.tn/category/actualites/page/"+str(i+1)+"/")

for i in page_link_list :   #extracing (link , type ) of each article
  # URl to web scrap from.
  # in this example we web scrap graphics cards from Newegg.com
 
  
  print(" connecting to : "+ str(i) )
  # opens the connection and downloads html page from url
  uClient = uReq(i)
  print('Scraping in progress ...')

  # parses html into a soup data structure to traverse html
  page_soup = soup(uClient.read(), "html.parser")
  uClient.close()
  #finds each Article 
  containers = page_soup.findAll("div", {"class": "bd-main"})
  container = containers[0].findAll("article")    #list contains the html code of each article
 
 
  for con in container:
    #con contains the code of  one article 
    
    link=con.h2.a["href"]
    link_list.append(link)     #fils link_list with all articles links
    article_title_list.append(con.h2.a.text)  




for i in range(len(link_list)):  
  #Scraping One Page Code    
  uClient = uReq(link_list[i])
  page_soup = soup(uClient.read(), "html.parser")
  uClient.close()
  article_date_list.append(page_soup.find("div" , {"class" : "bdaia-meta-info"}).find("span" , {"class" : "bdayh-date"}).text)
  ch=""
  for i in range(len(page_soup.find("div" , {"class" : "bdaia-post-content"}).findAll("p"))):
    ch+=page_soup.find("div" , {"class" : "bdaia-post-content"}).findAll("p")[i].text
  article_list.append(ch)
  print(str(i+1)+"of"+str(len(link_list)) +" :DONE")


 

import pandas as pd 
data={  'Title' : article_title_list , 'Article' : article_list ,'link'  : link_list  }
df = pd.DataFrame (data, columns = ['link','Title','Article'])


df.to_csv(r'C:\Users\User\Desktop\web scraping py\LaPresseFR.csv' ,encoding='utf-8-sig')
