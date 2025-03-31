from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
chrome_driver_path=r"C:\webdriver\chromedriver-win64\chromedriver.exe"
service=Service(executable_path=chrome_driver_path)
driver=webdriver.Chrome(service=service)
# driver.get("https://www.amazon.in/Nike-Royale-Leather-Sneaker-CQ9246-105/dp/B09MFSPSP4/ref=sr_1_37?crid=2D6K9SE6KIPHA&dib=eyJ2IjoiMSJ9._MWsfSR7gm2XnMgn6p1SZx413XOw_oMJYsobqhLpGQzMWUUVckFyOPy88cpsKs7z4rmSjcV82kLtmaKXJ4aUdLVBHuDVOAyR9y8cAvk72LpPi3EQ3F51vxsBzKqjmvjl6ZiWTGl8MffqpWCvup2YdB8H-IE0oKLYjpjLJYHy717Kmxiod4YCJHRkVsL4nzYOWpOCwNUCmOrv-YQxK77GfozN8t73JucBfiYAxLj4g8Hzn_813G7hd_BoilgVT44KF83nuWNHbhGnr0L1xry9K8sjN1QsAbqAa-QTUimk1EnJ7KIC6sh7A6k0PCDVRhRxQtN2GRPNAsYh6CNTrggBu0mdzcfJfSxkUrNZgPILihpsJbW5-8a8h1DNLIM_FQAsFpCJb_iu-5VRDiHQThLWyceyG9N7zzK0Ujc3L82UugB6AXthDYzzBz769s5dgB2q.CboVZtpJ6T9nXMnT2RXuuSNJK5kUUH53GMzRJzvee7M&dib_tag=se&keywords=shoes%2Bfor%2Bman%2Bstylish&qid=1743132283&sprefix=sh%2Caps%2C281&sr=8-37&th=1&psc=1")
# price=driver.find_element(By.CLASS_NAME,"a-price-whole")
# price=driver.find_element(By.CLASS_NAME,"a-price-whole")
# print(price.text)
driver.get("https://www.python.org/")

# logo=driver.find_element(By.CLASS_NAME,"python-logo")
# print(f"Logo size: {logo.size}")
# link=driver.find_element(By.CSS_SELECTOR,".download-buttons a")
# print(link.get_attribute("href"))

# bug_link=driver.find_element(By.XPATH,'//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_times=driver.find_elements(By.CSS_SELECTOR,".shrubbery li time")

event_names=driver.find_elements(By.CSS_SELECTOR,".shrubbery li a ")
events={}
for n in range(len(event_times)):
    events[n]={
        "time":event_times[n].text,
        "name":event_names[n].text,
    }
print(events)    
input("press Enter to close the browser...")
driver.quit()


 

