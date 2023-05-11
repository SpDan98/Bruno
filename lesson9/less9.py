import requests
import xml.etree.ElementTree as et
import bs4
responce=requests.get('https://www.cbr.ru/scripts/XML_daily.asp?date_req=09/05.2023')
# print(responce.text)
# soap=bs4.BeautifulSoup(responce.text,'html.parser')

# # print(soap.body.h2)

# data=soup.find('table',{})
root=et.fromstring(responce.text)
for i in root.findall('Valute'):
    print(i.findtext('Value'))


