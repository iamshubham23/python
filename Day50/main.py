# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# chrome_driver_path=r"C:\webdriver\chromedriver-win64\chromedriver.exe"
# service=Service(executable_path=chrome_driver_path)
# driver=webdriver.Chrome(service=service)

# My_Email="adhira720@gmail.com"
# My_password="7-QD4aq(2?gnpEw"

# driver.get("https://tinder.com/app/recs")

# try:
#     login=WebDriverWait(driver,10).until(
#         EC.element_to_be_clickable((By.XPATH,'//*[@id="q-22769943"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div'))
#     )
#     login.click()
# except Exception as e:
#     print(f"there is error :{e}")    



# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# chrome_driver_path = r"C:\webdriver\chromedriver-win64\chromedriver.exe"
# service = Service(executable_path=chrome_driver_path)

# # Create a new Chrome options instance
# chrome_options = Options()

# # Suppress the DevTools logs
# chrome_options.add_argument("--log-level=3")  # Only show errors

# driver = webdriver.Chrome(service=service, options=chrome_options)
# My_Email="adhira720@gmail.com"
# # fb_Email = "https://www.facebook.com/profile.php?id=100090951994952"
# My_password = "t32$&7fb"

# driver.get("https://tinder.com/app/recs")

# try:
#     login = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH,'//*[@id="c1438810056"]/div/div[1]/div/div/div/main/div/div[2]/div/div[3]/div/div/button[2]/div[2]/div[2]'))
#     )
#     login.click()

# except Exception as e:
#     print(f"first problem: {e}")

# try: 
#     more_opt=WebDriverWait(driver,10).until(
#         EC.element_to_be_clickable((By.XPATH,'//*[@id="c-289571020"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/button'))
#     )
#     more_opt.click()

# except Exception as e:
#     print(f"more option login problem: {e}") 

# try:
#     fb_login=WebDriverWait(driver,10).until(
#         EC.element_to_be_clickable(By.XPATH,'//*[@id="c-289571020"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
#     )
#     fb_login.click()
# except Exception as e:
#     print(f"fb login problem {e}")

# email_login=driver.find_element(By.NAME,"email")
# password_login=driver.find_element(By.NAME,"pass")

# email_login.send_keys(My_Email)
# password_login.send_keys(My_password)

# Log_in=driver.find_element(By.NAME,"login")
# Log_in.click()

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
#     login_button = driver.find_element(By.XPATH,'//*[@id="s-1223353241"]/div/div[1]/div/div/div/main/div/div[2]/div/div[3]/div/div/button[2]/div[2]/div[2]')
#     login_button.click()
#     print("Login page opened")

#     # Wait for the "More Options" button and click it
#     print("Waiting for 'More Options' button...")
#     # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='more-options-button']")))
#     more_options_button = driver.find_element(By.XPATH,'//*[@id="s1343232979"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/button')
#     more_options_button.click()
#     print("More options clicked")

#     # Wait for Facebook login option and click it
#     print("Waiting for Facebook login button...")
#     # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='facebook-login-button']")))
#     fb_login_button = driver.find_element(By.XPATH,'//*[@id="s1343232979"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Path to ChromeDriver
# chrome_driver_path = r"C:\webdriver\chromedriver-win64\chromedriver.exe"
# service = Service(executable_path=chrome_driver_path)
# driver = webdriver.Chrome(service=service)

# # Secure credentials using environment variables
My_email = os.getenv("TINDER_EMAIL", "adhira720@gmail.com")
My_password = os.getenv("TINDER_PASSWORD", "t32$&7fb")

# # Open Tinder
# driver.get("https://tinder.com/app/recs")

# try:
#     # Handle cookie banner
#     try:
#         cookie_banner = WebDriverWait(driver, 5).until(
#             EC.element_to_be_clickable((By.XPATH, '//*[@id="s-1223353241"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]'))
#         )
#         cookie_banner.click()
#         print("Cookie banner closed.")
#     except Exception as e:
#         print("No cookie banner found.")

#     # Wait for the login button and click it
#     print("Waiting for login button to appear...")
#     try:
#         login_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, '//*[@id="s-1223353241"]/div/div[1]/div/div/div/main/div/div[2]/div/div[3]/div/div/button[2]/div[2]'))
#         )
#         login_button.click()
#         print("Login page opened")
#     except Exception as e:
#         print(f"something error:{e}")
    







from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
import os
import time


def wait_and_click(driver, by_type, selector, timeout=10, use_js=False):
    """Helper function to wait for and click elements"""
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by_type, selector))
        )
        if use_js:
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(1)  # Short pause after scrolling
            driver.execute_script("arguments[0].click();", element)
        else:
            element.click()
        return True
    except Exception as e:
        print(f"Error clicking element {selector}: {e}")
        return False

# Initialize Chrome with options
chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--disable-notifications")
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_driver_path = r"C:\webdriver\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Credentials
MY_EMAIL = os.getenv("TINDER_EMAIL", "fjjfwo")
MY_PASSWORD = os.getenv("TINDER_PASSWORD", "fnjjee")

try:
    # Open Tinder
    driver.get("https://tinder.com")
    print("Opened Tinder website")

    # Wait for initial page load
    time.sleep(3)

    # Try multiple selectors for the login button
    login_selectors = [
        (By.XPATH, "//div[text()='Log in']"),
        # (By.XPATH, "//button[contains(@class, 'button')]//span[text()='Log in']"),
        # (By.XPATH, "//a[contains(@href, '/login')]"),
        
    ]

    login_clicked = False
    for selector in login_selectors:
        try:
            if wait_and_click(driver, selector[0], selector[1], use_js=True):
                login_clicked = True
                print("Login page opened")
                break
        except Exception:
            continue

    if not login_clicked:
        raise Exception("Could not click login button")

    # Wait for and click More Options
    time.sleep(2)  # Wait for animation
    more_options_clicked = wait_and_click(
        driver,
        By.XPATH,
        "//button[text()='More Options']",
        use_js=True
    )
    if not more_options_clicked:
        raise Exception("Could not click More Options button")
    print("More options clicked")

    # Wait for and click Facebook login
    time.sleep(2)  # Wait for animation
    fb_button_clicked = wait_and_click(
        driver,
        By.XPATH,
        "//div[text()='Log in with Facebook']",
        use_js=True
    )
    if not fb_button_clicked:
        raise Exception("Could not click Facebook login button")
    print("Facebook login button clicked")

    # Switch to Facebook popup
    original_window = driver.current_window_handle
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    print("Switched to Facebook login window")

    # Handle Facebook login with retry
    max_retries = 3
    for attempt in range(max_retries):
        try:
            email_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
            email_field.send_keys(MY_EMAIL)
            
            password_field = driver.find_element(By.ID, "pass")
            password_field.send_keys(MY_PASSWORD)
            password_field.send_keys(Keys.RETURN)
            print("Entered Facebook credentials")
            break
        except Exception as e:
            if attempt == max_retries - 1:
                raise Exception(f"Failed to login to Facebook after {max_retries} attempts: {e}")
            print(f"Retry {attempt + 1}/{max_retries} for Facebook login")
            time.sleep(2)

    # Switch back to Tinder and handle popups
    driver.switch_to.window(original_window)
    print("Switched back to Tinder window")

    # Handle popups with retry logic
    popup_handlers = [
        ("//button[contains(., 'Allow')]", "location"),
        ("//button[contains(., 'Not interested')]", "notification"),
        ("//button[contains(., 'Accept')]", "cookies")
    ]

    for xpath, popup_type in popup_handlers:
        try:
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            ).click()
            print(f"Handled {popup_type} popup")
        except TimeoutException:
            print(f"No {popup_type} popup found")


#     print("Starting dislike sequence...")
#     for i in range(10):
#         try:
#             dislike_button = WebDriverWait(driver, 5).until(
#                 EC.element_to_be_clickable((By.XPATH, "//span[text()='Nope']"))
#             )
#             driver.execute_script("arguments[0].click();", dislike_button)
#             print(f"Dislike {i+1}/10 clicked")
#             time.sleep(2)  # Random delay between actions
#         except Exception as e:
#             print(f"Error during dislike {i+1}: {e}")
#             driver.save_screenshot(f"dislike_error_{i+1}.png")
except Exception as e:
    print(f"An error occurred: {e}")
    driver.save_screenshot(f"error_{time.strftime('%Y%m%d_%H%M%S')}.png")

finally:
    input("Press Enter to close the browser...")
    driver.quit()
