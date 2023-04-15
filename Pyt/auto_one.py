from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

search = input("Enter a word:")

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 30)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

# Navigate to url with video being appended to search_query
driver.get('https://www.youtube.com/results?search_query='+search)

# play the video
wait.until(visible((By.ID, "video-title")))
elementOpen = driver.find_element(By.ID, "video-title")
elementOpen.click()
