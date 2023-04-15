from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# initialize the Chrome driver
driver = webdriver.Chrome()

# open YouTube
driver.get("https://www.youtube.com/")

# find the search bar and input the query
# search_bar = driver.find_element_by_name("search_query")
search_bar = driver.find_element(By.NAME, "search_query")
search_bar.send_keys("your search query" + Keys.RETURN)

# wait for the page to load
time.sleep(5)

# find the first video in the search results and click on it
# first_video = driver.find_element_by_css_selector("a#video-title")
first_video = driver.find_elements(By.CSS_SELECTOR, ".text-wrapper.style-scope.ytd-video-renderer")
# first_video.click()
first_video = driver.find_element(By.ID, "video-title")

first_video.click()
# for video in videos[:10]:
#     print(video.get_attribute("title"))

# Close the web driver
driver.quit()

# # wait for the video to load and start playing
# time.sleep(5)

# # close the browser
# driver.quit()
