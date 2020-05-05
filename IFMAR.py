#AR version


page_link_list=[]
link_list=[]
article_list=[]
article_title_list=[]


for i in range(2):
  page_link_list.append("https://www.ifm.tn/ar/articles?page="+str(i+1))

for i in page_link_list :   #extracing (link , type ) of each article
  # URl to web scrap from.
  # in this example we web scrap graphics cards from Newegg.com
  print('Scraping ifm.tn/ar in progress ...')
  
 
  # opens the connection and downloads html page from url
  uClient = uReq(i)

  # parses html into a soup data structure to traverse html
  page_soup = soup(uClient.read(), "html.parser")
  uClient.close()
  #finds each Article 
   
  containers = page_soup.findAll("div", {"class": "col-md-8 col-sm-7 dual-posts padding-bottom-30"})
  container = containers[0].findAll("div", {"class": "row"})    #list contains the html code of each article
 
 
  for con in container:
    #con contains the code of  one article 
    link=con.findAll("a")[0]["href"]  
    link_list.append(link)     #fils link_list with all articles links
    

    
for i in range(len(link_list)):  
  #Scraping One Page Code    
  uClient = uReq(link_list[i])
  page_soup = soup(uClient.read(), "html.parser")
  uClient.close()
  containers = page_soup.findAll("div", {"class": "blog-excerpt"})
  article_title_list.append(containers[0].find("h2").text)
  
  ch=containers[0].findAll("div" , {"class": "intro"})[0].text

  for j in range(len(containers[0].findAll("div" , {"class": "coprs"})[0].findAll('p'))):

    
    ch+=containers[0].findAll("div" , {"class": "coprs"})[0].findAll('p')[j].get_text()
  article_list.append(ch)
  print(str(i)+"of"+str(len(link_list)) +" :DONE")


import pandas as pd 
data={  'title' : article_title_list , 'article' : article_list ,'link'  : link_list  }
df = pd.DataFrame (data, columns = ['link','title','article'])
import numpy as np
df["type"]= np.nan

df.to_csv('ifmAR.csv' ,encoding='utf-8-sig')
