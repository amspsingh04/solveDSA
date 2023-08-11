from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

# URL of the page with questions
url = 'https://leetcode.com/problemset/all/?page=1&topicSlugs=array'
gecko= 'C:/Users\spsin\Desktop\geckodriver-v0.33.0-win64\geckodriver'
# XPath expression for the elements containing the text
xpath_expression = '//*[@id="__next"]/div/div[2]/div[1]/div[1]/div[5]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/a'
firefox_path="C:/Program Files (x86)\Mozilla Firefox\firefox.exe"

options = Options()

# Initialize the Firefox WebDriver
service = Service(executable_path=gecko)
driver = webdriver.Firefox(service=service, options=options)


# Navigate to the URL
driver.get(url)

# Find elements using XPath
elements = driver.find_elements(By.XPATH, xpath_expression)

# Extract and print the text from each element, stripped of whitespace
element_text = elements.text.strip()
print(element_text)

# Close the browser
driver.quit()
