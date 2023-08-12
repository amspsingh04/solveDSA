from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time


# URL of the page with questions
url = 'https://leetcode.com/problemset/all/?page=1&topicSlugs=array'
gecko= 'C:/Users\spsin\Desktop\geckodriver-v0.33.0-win64\geckodriver'

# XPath expression for the elements containing the text
options = Options()

# Initialize the Firefox WebDriver
service = Service(executable_path=gecko, log_path='geckodriver.log')
driver = webdriver.Chrome()

j=1
url = 'https://leetcode.com/problemset/all/?page={j}&topicSlugs=array'
# Navigate to the URL
driver.get(url)
time.sleep(5)
# Find elements using XPath
for i in range(2,52):
    xpath_expression = f'/html/body/div[1]/div/div[2]/div[1]/div[1]/div[5]/div[2]/div/div/div[2]/div[{i}]/div[2]/div/div/div/div/a'
    element = driver.find_element(By.XPATH, xpath_expression)

# Extract and print the text from each element, stripped of whitespace


# Close the browser
driver.quit()
