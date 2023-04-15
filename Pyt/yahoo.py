from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://www.youtube.com/')





search_box = browser.find_element(By.NAME, 'search_query')  # Find the search box
search_box.send_keys("Python Programming")
search_box.send_keys('seleniumhq' + Keys.RETURN)

# browser.quit()
