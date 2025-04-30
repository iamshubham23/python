from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = r"C:\webdriver\chromedriver-win64\chromedriver.exe"
# service=Service(executable_path=chrome_driver_path)
# driver=webdriver.Chrome(service=service)
instagram_email="dskdmm@gmail.com"   #write you gmail
instagram_password="random"   #write ur password
instagram_url="https://www.instagram.com/"
insta_account="python.hub"


class InstaFollowers():
    def __init__(self,driver_path):
        service=Service(executable_path=driver_path)
        self.driver=webdriver.Chrome(service=service)
        self.driver.get(instagram_url)
        time.sleep(5)
    
    def login(self):
        try:
            Email_login=WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[starts-with(@aria-label,'Phone number, username, or email')]"))
            )
            Email_login.click()
            Email_login.send_keys(instagram_email)
            print("email filled succesfully")
        except Exception as e:
            print(f"something went wrong during email field {e}")
        try:
            password_login=WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable((By.XPATH,"//input[starts-with(@aria-label,'Password')]"))
            )
            password_login.click()
            password_login.send_keys(instagram_password)
            password_login.send_keys(Keys.ENTER)
            print("password succesfully filled")
        except Exception as e:
            print(f"something goes wrong during password field")
       
        print("insta opened succesfully")  
        time.sleep(5)
        try:
            not_now = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((
                    By.XPATH, 
                    "//button[text()='Not Now']"
                ))
            )
            not_now.click()
            print("Handled save login popup")
        except :
            print("No save login popup found")  

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"{instagram_url}{insta_account}")
        print(f"trying to open {insta_account}")
        time.sleep(2)

        followers_button=WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'a[href*="/followers"]'))
        )
        followers_button.click()
        print("followers button clicked succesfully")
        time.sleep(2)
        modal=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                'div[role="dialog"]'
            ))
        )
        for _ in range(3):
            self.driver.execute_script("arguments[0].scrollTop=arguments[0].scrollHeight",modal)
            time.sleep(2)

        followers=modal.find_elements(By.XPATH,"//span[starts-with(@class,'_ap3a _aaco _aacw _aacx _aad7 _aade')]")
        print(f"total followers found is: {len(followers)}")

        for i,follower in enumerate(followers[:5]):
            try:
                print(f"follower {i+1}: {follower.text}")

            except Exception as e:
                print(f"error getting follower {i+1}:{e}")    
        

bot=InstaFollowers(chrome_driver_path)
bot.login()
bot.find_followers()
