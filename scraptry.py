from selenium import webdriver
import pandas as pd

# URL of the page with questions
url = 'https://leetcode.com/problemset/all/?page=1&topicSlugs=array'

# Initialize the Firefox WebDriver
driver = webdriver.Firefox(executable_path='/path/to/geckodriver')  # Replace with the actual path to GeckoDriver

# Navigate to the URL
driver.get(url)

# Find the question title elements using XPath
question_title_elements = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[2]/div[1]/div[1]/div[5]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/a')

# Extract titles and store them in a list
question_titles = [element.text for element in question_title_elements]

# Close the browser
driver.quit()

# Create a DataFrame from the list of titles
df = pd.DataFrame({'Title': question_titles})

# Save the DataFrame to a CSV file
csv_file = 'leetcode_questions.csv'
df.to_csv(csv_file, index=False)

print(f'Titles saved to {csv_file}')
