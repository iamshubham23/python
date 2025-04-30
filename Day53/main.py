from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback

chrome_driver_path = r"C:\Users\shubh\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

google_form = "https://docs.google.com/forms/d/e/1FAIpQLScdY7Wm1A-rNv4HSlr1zmSZ_9sLXjArb3_XbLSfsrSYgne79w/viewform?usp=header"
appartment_url = "https://www.nobroker.in/property/rent/hyderabad/Gachibowli/?searchParam=W3sibGF0IjoxNy40NDAwODAyLCJsb24iOjc4LjM0ODkxNjgsInBsYWNlSWQiOiJDaElKMzg3ZWRxS1R5enNSNGtTVGI1N25FaXciLCJwbGFjZU5hbWUiOiJHYWNoaWJvd2xpIn1d&city=hyderabad"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
    "Accept-Language": "en-US,en;q=0.9,en-IN;q=0.8"
}
response = requests.get(appartment_url, headers=header)
data = response.text
soup = BeautifulSoup(data, "html.parser")


def rental_data():
    try:  
        links = [a["href"] for a in soup.find_all("a", href=True)]
        driver.get(appartment_url)
        WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.XPATH,"//div[starts-with(@id,'minimumRent')]"))
        )
        all_price=driver.find_elements(By.XPATH,"//div[starts-with(@id,'minimumRent')]")
        prices=[price.text for price in all_price]
        print(prices)

        
        address_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//h2[starts-with(@class,'flex items-center m-0 heading-6 font-semi-bold')]"))
        )
        addresses = [addr.text.strip() for addr in address_elements if addr.text.strip()]
        print(f"\nFound {len(addresses)} addresses")
        print(addresses)

        return links,prices,addresses
    except Exception as e:
        print("Error while fetching addresses", e)
        traceback.print_exc()
        return [],[],[]


def fill_google_form(links,prices,addresses):
    for n in range(min(len(links),len(prices),len(addresses))):
        driver.get(google_form)
        time.sleep(2)
        address=WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//input[starts-with(@aria-labelledby,'i1 i4')]"))
        )
        price_per_month=driver.find_element(By.XPATH,"//input[starts-with(@aria-labelledby,'i6 i9')]")
        property_link=driver.find_element(By.XPATH,"//input[starts-with(@aria-labelledby,'i11 i14')]")
        submit_button=driver.find_element(By.XPATH,"//span[text()='Submit']")

        address.clear()
        address.send_keys(addresses[n])
        price_per_month.clear()
        price_per_month.send_keys(prices[n])
        property_link.clear()
        property_link.send_keys(links[n])
        submit_button.click()
        time.sleep(2)

# def fill_google_form(links,prices,addresses):
#     for i in range(min(len(links),len(prices),len(addresses))):

def main():
    links, prices, addresses = rental_data()
    if links and prices and addresses:
        fill_google_form(links, prices, addresses)
    else:
        print("No data to submit to form")

if __name__ == "__main__":
    main()
    driver.quit()
