import requests
import xml.etree.ElementTree as et
import aiohttp
import datetime
import asyncio

def getdate(format,cur:datetime.date):
    delta=datetime.timedelta(1)
    yesterday=datetime.date.today()-delta
    dates=[]
    while cur <= yesterday:
        dates.append(cur.strftime(format))
        cur+=delta
    return dates
# print(getdate('%d-%m-%Y',datetime.date(2023,2,10)))

async def source1(dates):
    values=[]
    async with aiohttp.ClientSession() as session:
        for i in dates:
            async with session.get(f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={i}') as response:
                result=await response.text()
                root=et.fromstring(result)
                for j in root.findall('Valute'):
                    if j.findtext('CharCode') =='USD':
                        values.append(float(j.findtext('Value').replace(',','.')))
    return values

async def main():
    dates1=getdate('%d/%m/%Y',datetime.date(2023,2,10))

    t1=asyncio.create_task(source1(dates1))
    result = await t1
    print(result)
asyncio.get_event_loop().run_until_complete(main())