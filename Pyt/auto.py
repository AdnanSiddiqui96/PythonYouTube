from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

search = input("Enter a word:")
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.youtube.com/results?search_query='+search)
search_box = driver.find_element(By.NAME, "search_query")  # Find the search box
search_box.send_keys(Keys.RETURN)

time.sleep(5)

presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located
wait = WebDriverWait(driver, 10)

# find the second video title element and click on it
video_titles = driver.find_elements(By.ID, "video-title")
if len(video_titles) > 1:
    second_video_title = video_titles[1]
    second_video_title.click()


# wait for the Skip Ad button to appear and then click it
skip_ad_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ytp-ad-skip-button-container")))
skip_ad_button.click()

time.sleep(60)  # Play vedio for one minut.

driver.quit()
