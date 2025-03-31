# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# chrome_driver_path=r"C:\webdriver\chromedriver-win64\chromedriver.exe"
# service=Service(executable_path=chrome_driver_path)
# driver=webdriver.Chrome(service=Service)
# ACCOUNT_EMAIL="adhira720@gmail.com"
# ACCOUNT_PASSWORD="vfpw gzbx erke fitg"
# driver.get("https://www.linkedin.com/jobs/collections/recommended/?currentJobId=4140854068&discover=recommended&discoveryOrigin=JOBS_HOME_JYMBII")

# sign_in_button = driver.find_element(By.LINK_TEXT,"Sign in")
# sign_in_button.click()

# #Wait for the next page to load.
# time.sleep(5)

# email_field = driver.find_element(By.ID,"username")
# email_field.send_keys(ACCOUNT_EMAIL)
# password_field = driver.find_element(By.ID,"password")
# password_field.send_keys(ACCOUNT_PASSWORD)
# password_field.send_keys(Keys.ENTER)
# # form_filling1=driver.find_element(By.CSS_SELECTOR,"#text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4140854068-13222298170-multipleChoice")
# # form_filling1.send_keys("adhira720@gmail.com")
# # form_filling2=driver.find_element(By.CSS_SELECTOR,"#text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4140854068-13222298162-phoneNumber-country")
# # form_filling2.send_keys("+91")
# # form_filling3=driver.find_element(By.CSS_SELECTOR," artdeco-text-input--input")
# # form_filling3.send_keys("99331956133")
# # submit=driver.find_element(By.CSS_SELECTOR,"artdeco-button__text")
# # submit.click()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your chromedriver
chrome_driver_path = r"C:\webdriver\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)

# Start the Chrome WebDriver
driver = webdriver.Chrome(service=service)

# LinkedIn login credentials
ACCOUNT_EMAIL = "adhira720@gmail.com"
ACCOUNT_PASSWORD = "7-QD4aq(2?gnpEw"

# Navigate to LinkedIn jobs page
driver.get("https://www.linkedin.com/jobs/collections/recommended/?currentJobId=4140854068&discover=recommended&discoveryOrigin=JOBS_HOME_JYMBII")

# Wait until 'Sign in' button is clickable and click it
sign_in_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
)
sign_in_button.click()

# Wait for the login page to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)

# Enter the email and password
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)

# Press Enter to log in
password_field.send_keys(Keys.ENTER)
