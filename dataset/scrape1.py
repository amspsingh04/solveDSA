from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time
import csv

def main():
    geckodriver_path = 'C:/Users\spsin\Desktop\geckodriver-v0.33.0-win64\geckodriver'  # Replace with the actual path
    firefox_path = "C:/Program Files (x86)\Mozilla Firefox\firefox"

    options = Options()
    options.binary_location = firefox_path

    service = Service(executable_path=geckodriver_path)
    browser = webdriver.Firefox(service=service, options=options)

    try:
        csv_filename = "leetcode_array_problems.csv"
        with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Problem Name", "Solution Description"])

            for page_num in range(1, 3):
                url = f"https://leetcode.com/problemset/all/?page={page_num}&topicSlugs=array"
                browser.get(url)
                time.sleep(5)

                for i in range(2, 4):
                    link_xpath = f"/html/body/div[1]/div/div[2]/div[1]/div[1]/div[5]/div[2]/div/div/div[2]/div[{i}]/div[2]/div/div/div/div/a"
                    try:
                        link_element = browser.find_element(By.XPATH, link_xpath)
                        problem_name = link_element.text.strip()
                        link_element.click()
                        time.sleep(5)

                        solution_xpath = "/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div[2]"
                        try:
                            solution_element = browser.find_element(By.XPATH, solution_xpath)
                            solution_description = solution_element.text.strip()

                            example_index = solution_description.find("Example 1")
                            if example_index != -1:
                                solution_description = solution_description[:example_index]

                        except Exception as e:
                            print(f"Error finding solution description: {e}")
                            solution_description = "N/A"

                        csv_writer.writerow([problem_name, solution_description])

                        browser.back()
                        time.sleep(3)
                    except Exception as e:
                        print(f"Error processing problem {i-1}: {e}")
        print("Data extraction complete.")

    finally:
        browser.quit()

if __name__ == "_main_":
    main()
