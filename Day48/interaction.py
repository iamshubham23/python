from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_driver_path=r"C:\webdriver\chromedriver-win64\chromedriver.exe"
service=Service(executable_path=chrome_driver_path)
driver=webdriver.Chrome(service=service)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# numbers=driver.find_element(By.CSS_SELECTOR,"#articlecount a ")
# print(number[0].text)
# article_count_element = driver.find_element(By.CSS_SELECTOR, "#articlecount")

# Find all links (or other elements) under the article count section
# numbers = article_count_element.find_elements(By.TAG_NAME, "a")

# Print the first number (active editors)
# article_cout1=numbers[0].text
# print(numbers[0].text)

# # Print the second number (articles in English)
# article_cout2= numbers[1].text
# #print(article_cout2)
# numbers[1].click()

# community_portal=driver.find_element(By.LINK_TEXT,"Community portal")
# community_portal.click()
# search_box=WebDriverWait(driver,10).until(
#     EC.element_to_be_clickable((By.NAME,"search"))
# )

# search_box.send_keys("python")
# search_box.send_keys(Keys.ENTER)
# input("Press Enter to close the browser...")
# driver.quit()

# search_box=WebDriverWait(driver,10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME,"cdx-text-input__input"))
# )

# search_box.send_keys("python")

# search_box.send_keys(Keys.ENTER)
# input("Press Enter to close the browser...")
# driver.quit()





driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name=driver.find_element(By.NAME,"fName")
last_name=driver.find_element(By.NAME,"lName")
email=driver.find_element(By.NAME,"email")
first_name.send_keys("shubham")
last_name.send_keys("kumar")
email.send_keys("adhira343@gmail.com")

submit=driver.find_element(By.CSS_SELECTOR,"form button")

submit.click()