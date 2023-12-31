from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time
import csv


# URL of the page with questions
gecko= 'C:/Users\spsin\Desktop\geckodriver-v0.33.0-win64\geckodriver'

# XPath expression for the elements containing the text
options = Options()
arr_tags=['biconnected-component']
for name in arr_tags:
    csv_filename = f'source_dataset/leetcode_questions_{name}.csv'
    csv_file = open(csv_filename, 'w', newline='', encoding='utf-8')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Question','Tag'])
    
    # Initialize the Firefox WebDriver
    service = Service(executable_path=gecko, log_path='geckodriver.log')
    driver = webdriver.Chrome()
    for j in range(1,2):
        url = f'https://leetcode.com/problemset/all/?page=1&topicSlugs={name}'
            # Navigate to the URL
        driver.get(url)
        time.sleep(6)
                # Find elements using XPath
        for i in range(1,5):
            xpath_expression = f'/html/body/div[1]/div/div[2]/div[1]/div[1]/div[5]/div[2]/div/div/div[2]/div[{i}]/div[2]/div/div/div/div/a'
            element = driver.find_element(By.XPATH, xpath_expression).text
            question_title = ' '.join(element.split('.')[1:]).strip()  # Stripping the numbering
            csv_writer.writerow([question_title, f'{name}'])
    # Extract and print the text from each element, stripped of whitespace


    # Close the browser
    driver.quit()
