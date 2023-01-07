
# پیدا کردن ماشین های زیر 100 میلیون در صفحه اول دیوار

from bs4 import BeautifulSoup as bs
import requests as req

page_req=req.get('https://divar.ir/s/tehran/car?price=-100000000')
page_bs=bs(page_req.text,'html.parser')

data=page_bs.find_all('div',attrs={'class':'kt-post-card__body'})
print(len(data))
list_cars=[]
count=0
for i in data:
    name=i.find('h2')
    karkard_and_price=i.find_all('div',attrs={'class':'kt-post-card__description'})
    address=i.find('div',attrs={'class':'kt-post-card__bottom'})
    list_cars.append({
                        'name':name.text,
                        'price':karkard_and_price[1].text,
                        'karkard':karkard_and_price[0].text
                        ,'address':address.text })
                        
for i in list_cars:
    print('name: %s \nkarkard: %s\nprice: %s\naddress: %s'%(i['name'],i['karkard'],i['price'],i['address']))
    print('---------------------------')    


