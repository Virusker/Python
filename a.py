import requests
from bs4 import BeautifulSoup

url = 'https://www.tienganh123.com/1000-tu-vung-tieng-anh-co-ban/1268-bai-1.html'
response = requests.get(url)

#print(response)
soup = BeautifulSoup(response.content, "html.parser")
#print(soup)
titles = soup.findAll('tr')
print(titles)

#<td class="vcab_first">about</td>