from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# create an instance of webdriver and specify the browser you want to use
driver = webdriver.Chrome()

# navigate to the login page
driver.get("https://example.com/login")

# enter the username and password and click the login button
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
username.send_keys("your_username")
password.send_keys("your_password")
login_button = driver.find_element_by_name("login")
login_button.click()

# wait for the page to load
time.sleep(2)

# navigate to the signup page
driver.get("https://example.com/signup")

# enter the signup details and click the signup button
first_name = driver.find_element_by_name("first_name")
last_name = driver.find_element_by_name("last_name")
email = driver.find_element_by_name("email")
password = driver.find_element_by_name("password")
confirm_password = driver.find_element_by_name("confirm_password")
first_name.send_keys("Your First Name")
last_name.send_keys("Your Last Name")
email.send_keys("you@example.com")
password.send_keys("your_password")
confirm_password.send_keys("your_password")
signup_button = driver.find_element_by_name("signup")
signup_button.click()

# wait for the page to load
time.sleep(2)

# close the browser
driver.close()




#FileUpload

from selenium import webdriver

# create an instance of webdriver and specify the browser you want to use
driver = webdriver.Chrome()

# navigate to the page where you want to upload the file
driver.get("https://example.com/upload")

# locate the file input element and send the file path to it
file_input = driver.find_element_by_xpath("//input[@type='file']")
file_input.send_keys("path/to/your/file")

# submit the form to upload the file
submit_button = driver.find_element_by_xpath("//input[@type='submit']")
submit_button.click()

# close the browser
driver.close()

