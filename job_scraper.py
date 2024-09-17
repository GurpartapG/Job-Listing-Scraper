from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from bs4 import BeautifulSoup
import os
import time
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

linkedin_username = os.getenv('LINKEDIN_USERNAME')
linkedin_password = os.getenv('LINKEDIN_PASSWORD')

# Setup ChromeOptions
options = webdriver.ChromeOptions()
# Example: options.add_argument('--headless')

# Initialize the driver with Service and options
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# LinkedIn Login
driver.get('https://www.linkedin.com/login')
username = driver.find_element(By.ID, 'username')
username.send_keys(linkedin_username)
password = driver.find_element(By.ID, 'password')
password.send_keys(linkedin_password)
password.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(5)

# Navigate to Jobs section (modify this URL based on your specific job search criteria)
driver.get('https://www.linkedin.com/jobs/search/?keywords=Software%20Engineering')

# Scroll down to load more jobs
for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Scrape job listings
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Updated selectors based on LinkedIn's current structure
jobs = soup.find_all('div', {'class': 'base-card'})

# Parse job data
job_list = []
for job in jobs:
    try:
        title = job.find('h3', {'class': 'base-search-card__title'}).text.strip()
        company = job.find('h4', {'class': 'base-search-card__subtitle'}).text.strip()
        location = job.find('span', {'class': 'job-search-card__location'}).text.strip()
        job_list.append([title, company, location])
    except AttributeError:
        continue  # Skip if there is an error finding elements

# Save to CSV
df = pd.DataFrame(job_list, columns=['Job Title', 'Company', 'Location'])
df.to_csv('job_listings.csv', index=False)

# Close the driver
driver.quit()

print("Job listings scraped and saved to job_listings.csv")
