from bs4 import BeautifulSoup
import requests

#NYT search results for "Hate Crime"
url= "https://www.nytimes.com/search?dropmab=true&endDate=20211201&query=anti%20asian&sort=best&startDate=20201201"
#using result 
result = requests.get(url)
soup = BeautifulSoup(result.content, 'html.parser')
title = soup.title.text
page_body = soup.body
page_head = soup.head
#collecting the titles for Page 1 Search
title_names = soup.select('h4')
for tag in title_names:
    print(tag.text.strip())

