from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
import os
from random import uniform
chrome_driver_path = r"C:\webdriver\chromedriver-win64\chromedriver.exe"
PROMISED_DOWN=150
PROMISED_UP=10
TWITTER_EMAIL="a"
TWITTER_PASSWORD="bj"
TWITTER_USERNAME="@hv5"

class InternetSpeedTwitterBot:
    def __init__(self,driver_path):
        chrome_options=Options()
        service=Service(driver_path)
       
        self.driver=webdriver.Chrome(service=service,options=chrome_options)
        
        self.up=0
        self.down=0

    def get_internet_speed(self):
    
        self.driver.get("https://www.speedtest.net/")
        print("speed test opened")
        time.sleep(2)
        pop_handlers=WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//button[starts-with(@id,'onetrust-accept-btn-handler')]"))
        )
        pop_handlers.click()
        print("poped button clicked")
        time.sleep(2)
        
        go_buton=WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//span[text()='Go']"))
        )
        go_buton.click()
        print("go button clicked")
        time.sleep(60)
        print("speed test start")
        
        self.down=float(self.driver.find_element(
            By.XPATH,
            "//span[starts-with(@class,'result-data-large number result-data-value download-speed')]"
            ).text)
        print(f"download speed is {self.down}MBPS")
         
        self.up=float(self.driver.find_element(
            By.XPATH,
            "//span[starts-with(@class,'result-data-large number result-data-value upload-speed')]"
            ).text)
        print(f"upload speed is {self.up}MBPS")

    def tweet_at_provider(self):
        self.driver.get("https://x.com/")
        try:
            sign_in=WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable((By.XPATH,"//span[text()='Sign in']"))
            )   
            
            sign_in.click() 
            print("sign in button clicked")
        except Exception as e:
            print(f"something wrong during sigin {e}")    

        time.sleep(2)
        input_email=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//input[starts-with(@autocomplete,'username')]"))
        )
        input_email.send_keys(TWITTER_EMAIL)
        time.sleep(2)
        try:
            next=WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable((By.XPATH,"//span[text()='Next']"))
            )
            next.click()
            print("next button clicked")
        except Exception as e:
            print(f"something worng during clicking next {e}")    
        time.sleep(2)
        try:
            user_name=WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH,"//input[starts-with(@autocapitalize,'none')]"))
            )
            user_name.send_keys(TWITTER_USERNAME)  
            user_name.send_keys(Keys.ENTER)
            print("username entered")
            time.sleep(2)
        except Exception as e:
            print("username does not required")
            time.sleep(2)
        except Exception as e:
            print("something went wrong during clicking of username {e}")
        time.sleep(4)        

        input_pass=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]'))
        )
        input_pass.send_keys(TWITTER_PASSWORD)
        input_pass.send_keys(Keys.ENTER)
        print("password input")

        time.sleep(10)    

        print("trying to find twitter_post button")
        try:
            twitter_post=WebDriverWait(self.driver).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "//div[starts-with(@class,'css-175oi2r r-xoduu5 r-xyw6el r-13qz1uu r-1e084wi')]"))
            ) 
            twitter_post.click()
            print("twitter post_button is find")
        except Exception as e:
            print(f"couldn't find twitter_post button")

           
        time.sleep(2)
        print("twitter_post  button clicked")
        twitter_message=f"hey @bsnl router,my internet download speed is {self.down} and upload speed is{self.up}"
        
        compose_message=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//div[starts-with(@aria-autocomplete,'list')]"))
        )
        compose_message.send_keys(twitter_message)
        compose_message.send_keys(Keys.ENTER)

        print("trying to click message post")
        try:
            post_message=WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable((By.XPATH,"//span[text()='Post']"))
            )
            post_message.click()
            print("message post succesufully")
        except Exception as e:
            print("could't post message")    

bot=InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweet_at_provider()


#//'a[data-testid="SideNav_NewTweet_Button"]'

