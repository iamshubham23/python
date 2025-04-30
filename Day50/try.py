# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os
# import time

# # Path to ChromeDriver
# chrome_driver_path = r"C:\webdriver\chromedriver-win64\chromedriver.exe"
# service = Service(executable_path=chrome_driver_path)
# driver = webdriver.Chrome(service=service)

# # Secure credentials using environment variables
# My_email = os.getenv("TINDER_EMAIL", "adhira720@gmail.com")
# My_password = os.getenv("TINDER_PASSWORD", "t32$&7fb")

# # Open Tinder
# driver.get("https://tinder.com/app/recs")

# try:
#     # Wait until the login button is clickable
#     print("Waiting for login button to appear...")
#     # login_button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"c9iqosj")))
#     login_button = driver.find_element(By.XPATH,"//div[text()='Log in']")
#     login_button.click()
#     print("Login page opened")

#     # Wait for the "More Options" button and click it
#     print("Waiting for 'More Options' button...")
#     more_options_button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[text()='More Options']")))
#     # more_options_button = driver.find_element(By.XPATH,"//button[text()='More Options']")
#     more_options_button.click()
#     print("More options clicked")

#     # Wait for Facebook login option and click it
#     print("Waiting for Facebook login button...")
#     fb_login_button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable(( By.XPATH,"//div[text()='Log in with Facebook']")))
#     # fb_login_button = driver.find_element(By.XPATH,"//div[text()='Log in with Facebook']")
#     fb_login_button.click()
#     print("Facebook login clicked")

#     # Additional handling here (pop-ups, iframes, etc.)

# except Exception as e:
#     print(f"Error occurred: {e}")
#     driver.save_screenshot('error_screenshot.png')  # Save screenshot to debug the state at failure

# # Optionally, add some sleep time to let the process complete
# time.sleep(5)

# # Cleanup
# driver.quit()



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import os
import time
from random import uniform


chrome_driver_path = r"C:\webdriver\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)


MY_EMAIL ="a"
MY_PASSWORD =""
try:
    driver.get("https://tinder.com")
    try:
        login_button=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//div[text()='Log in']"))
        )
        login_button.click()
        print("login button clicked")
    except Exception as e:
        print("error during login button clicked")


    try:
        more_option_clicked=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='More Options']"))
        )
        more_option_clicked.click()
        print("more option button is clicked")

    except Exception as e:
        print("error during clicke of more option button")
    try:
        fb_button_clicked=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//div[text()='Log in with Facebook']"))
        )
        fb_button_clicked.click()
        print("fb button clicked")
    except Exception as e:
        print("error during facebook login") 

    original_window=driver.current_window_handle
    WebDriverWait(driver,10).until(lambda d:len(d.window_handles)>1)
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    print("switched to facebook login ")    
    max_try=3
    for attempt in range(max_try):
        try:
            email_field=WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.ID,"email"))
            )
            email_field.send_keys(MY_EMAIL)
            password_field=driver.find_element(By.ID,"pass")
            password_field.send_keys(MY_PASSWORD)
            password_field.send_keys(Keys.RETURN)
            print("facebook login succesfull")
            break
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt+1==max_try:
                print("fail to login")
                time.sleep(2)

    driver.switch_to.window(original_window)
    print("you are backed to tinder")
    
    popup_handlers = [
        ("//button[text()='Allow']", "location"),
        ("//button[text()='Enable']", "location-enable"),
        ("//button[text()='I accept']", "cookies"),
        ("//button[text()='Not interested']", "notifications"),
        ("//button[text()='Maybe later']", "notifications-later")
    ]
    for xpath,popup_type in popup_handlers:
        try:
            element=WebDriverWait(driver,5).until(
                EC.element_to_be_clickable((By.XPATH,xpath))
            )
            driver.execute_script("arguments[0].click();", element)
            print(f"Handled {popup_type} popup")
            time.sleep(1)
        except TimeoutException:
            print(f"No {popup_type} popup found")

    # Improved dislike functionality
    print("Starting dislike sequence...")
    dislike_selectors = [
        "//span[text()='Nope']",
        "//button[@aria-label='Nope']",
        "//button[contains(@class, 'button--no')]"
    ]        
    
    for n in range(0,10):
        time.sleep(uniform(1.5,2.5))
        try:
            for selector in dislike_selectors:
                try:
                    dislike_button=WebDriverWait(driver,5).until(
                        EC.element_to_be_clickable((By.XPATH,"//span[text()='Nope']"))
                    )
                    driver.execute_script("arguments[0].click();", dislike_button)
                    print(f"Dislike {n+1}/10 clicked")
                    break
                except:
                    continue
            
            else:
                print(f"Could not find dislike button on attempt {n+1}")
        except Exception as e:
            print(f"Error during dislike {n+1}: {e}")
   
except Exception as e:
    print("oops something error")
finally:
    input("press Enter to close the browser...")
    driver.quit()

    

