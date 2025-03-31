import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

url=("https://www.amazon.in/Campus-First-Running-Shoes-India/dp/B08WPBXKNR/?_encoding=UTF8&pd_rd_w=KfjyC&content-id=amzn1.sym.0e03aefb-8b93-49f8-beeb-6d21836a1b3d&pf_rd_p=0e03aefb-8b93-49f8-beeb-6d21836a1b3d&pf_rd_r=794F6Z1CYJSQHZWT9JK1&pd_rd_wg=ljPBj&pd_rd_r=80d31b39-f4dd-4ea1-9793-2a24bf13fd57&ref_=pd_hp_d_atf_dealz_cs&th=1&psc=1")
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
    "Accept-Language":"en-US,en;q=0.9,en-IN;q=0.8"
}
response=requests.get(url,headers=header)

soup=BeautifulSoup(response.content,"lxml")
# print(soup.prettify())

price_element=soup.find(class_="a-price-whole")
if price_element:
    price=price_element.get_text().strip()
    try:
        price_as_float=float(price.replace(',',''))
        print(price_as_float)
    except ValueError:
        print("could not convert price to float")
else:
    print("price element not found")        

title=soup.find(id="title").get_text().strip()
print(title)
message=f"{title} is currently priced at {price}"
if price_as_float < 1100:
    message=f"{title} is now {price}"

my_email="adhira720@gmail.com"
password="vfpw gzbx erke fitg"
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(
    from_addr=my_email,to_addrs=my_email,
    msg=f"Subject:Amazon price alert!\n\n\n {message}\n{url}".encode("utf-8")
)
connection.close()
