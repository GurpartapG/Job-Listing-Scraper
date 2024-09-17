# Job Listing Scraper
This project automates the process of scraping job listings from LinkedIn based on specified 
search criteria (e.g., job title, location). It uses Selenium for web automation and BeautifulSoup
for parsing job listings. The results, including job titles, company names, and locations, are 
stored in a CSV file for further analysis.

## Project Motivation
This scraper was created to automate the process of searching for job listings in bulk, 
particularly for roles related to software engineering, internships, co-ops, and data-related 
fields. Instead of manually sifting through job listings on LinkedIn, this tool automates the 
task and compiles the data into a CSV for ease of analysis.

## Features
- Automates LinkedIn login using environment variables for secure handling of credentials
- Scrapes job titles, companies, and locations based on specific search criteria on LinkedIn
- Saves the job listings into a CSV file for easy processing or analysis
- Utilizes Selenium WebDriver for automating the browser and BeautifulSoup for scraping the job data

## Installation
1. Clone the repository to your local machine
2. Navigate to the project directory
3. Install the required dependencies:  
```bash
    pip install selenium beautifulsoup4 pandas python-dotenv webdriver-manager
```

4. Create a .env file in the root directory to store your LinkedIn credentials:
```bash
LINKEDIN_USERNAME=your-linkedin-username
LINKEDIN_PASSWORD=your-linkedin-password
```

5. Run the script to start scraping job listings
