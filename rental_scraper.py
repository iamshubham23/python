from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

chrome_driver_path = r"C:\Users\shubh\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLScdY7Wm1A-rNv4HSlr1zmSZ_9sLXjArb3_XbLSfsrSYgne79w/viewform?usp=header"
apartment_url = "https://www.nobroker.in/property/rent/hyderabad/Gachibowli/?searchParam=W3sibGF0IjoxNy40NDAwODAyLCJsb24iOjc4LjM0ODkxNjgsInBsYWNlSWQiOiJDaElKMzg3ZWRxS1R5enNSNGtTVGI1N25FaXciLCJwbGFjZU5hbWUiOiJHYWNoaWJvd2xpIn1d&city=hyderabad"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
    "Accept-Language": "en-US,en;q=0.9,en-IN;q=0.8"
}

def scrape_rental_data():
    logging.info("Starting rental data scraping")
    try:
        response = requests.get(apartment_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract property links
        links = [a["href"] for a in soup.find_all("a", href=True)]
        logging.info(f"Found {len(links)} links")

        # Use Selenium to get dynamic content
        driver.get(apartment_url)

        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[starts-with(@id,'minimumRent')]"))
        )
        all_price_elements = driver.find_elements(By.XPATH, "//div[starts-with(@id,'minimumRent')]")
        prices = [price.text for price in all_price_elements]
        logging.info(f"Found {len(prices)} prices")

        address_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//h2[starts-with(@class,'flex items-center m-0 heading-6 font-semi-bold')]"))
        )
        addresses = [addr.text.strip() for addr in address_elements if addr.text.strip()]
        logging.info(f"Found {len(addresses)} addresses")

        return links, prices, addresses

    except Exception as e:
        logging.error("Error during scraping rental data")
        logging.error(traceback.format_exc())
        return [], [], []

def fill_google_form(links, prices, addresses):
    logging.info("Starting to fill Google Form")
    for i in range(min(len(links), len(prices), len(addresses))):
        try:
            driver.get(google_form_url)
            time.sleep(2)  # Wait for form to load

            address_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[starts-with(@aria-labelledby,'i1 i4')]"))
            )
            price_input = driver.find_element(By.XPATH, "//input[starts-with(@aria-labelledby,'i6 i9')]")
            link_input = driver.find_element(By.XPATH, "//input[starts-with(@aria-labelledby,'i11 i14')]")
            submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")

            address_input.clear()
            address_input.send_keys(addresses[i])
            price_input.clear()
            price_input.send_keys(prices[i])
            link_input.clear()
            link_input.send_keys(links[i])

            submit_button.click()
            logging.info(f"Submitted form for entry {i+1}")

            time.sleep(2)  # Wait before next submission

        except Exception as e:
            logging.error(f"Error filling form for entry {i+1}")
            logging.error(traceback.format_exc())

def main():
    links, prices, addresses = scrape_rental_data()
    if links and prices and addresses:
        fill_google_form(links, prices, addresses)
    else:
        logging.error("No data to submit to form")

if __name__ == "__main__":
    main()
    driver.quit()
