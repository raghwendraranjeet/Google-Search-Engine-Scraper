# Google Search Engine Scraper

## Overview
This project is designed to automate the process of scraping details from Google search results based on specified keyword and locations. The scraper extracts key information such as company name, rating, reviews, working hours, phone number, address, and website, and saves the data into a CSV file for further analysis.

## Objective
The primary goal of this project is to create a tool that automates the extraction of keyword-related data from Google search results, providing a structured dataset for analysis. This can help job seekers, researchers, and businesses gain insights into the market for specific roles and locations.

## Features
- *Automated Scraping*: Automatically navigates Google search results to collect keyword listing data.
- *Configurable Parameters*: Allows users to specify keywords, locations, and the number of pages to scrape via a configuration file.
- *Data Extraction*: Extracts company name, rating, reviews, working hours, phone number, address, and website.
- *CSV Export*: Saves the extracted data into a CSV file for easy analysis and sharing.
- *Error Handling*: Includes basic error handling to manage issues during the scraping process.

## Technologies Used
- *Python*: Core programming language used for the script.
- *Selenium*: Used for web browser automation.
- *BeautifulSoup*: Utilized for parsing HTML and extracting data.
- *Pandas*: Employed for data manipulation and saving to CSV.
- *PyYAML*: Used for reading configuration parameters from a YAML file.

## How to Run
### Prerequisites
- Ensure you have Python installed on your system.
- Install the required Python packages using the following command:

  pip install selenium beautifulsoup4 pandas pyyaml


### Configuration
Create a config.yaml file in the same directory as your script with the following content:

..yaml
FILENAME: 'Google_Search_Engine'
JOB_PROFILE: 'keyword'
LOCATION: 'Bangalore'
NUM_PAGES: 4
...

### Running the Script
1. Ensure the config.yaml file is correctly set up with your desired parameters.
2. Download the Chrome WebDriver that matches your Chrome browser version from [here](https://sites.google.com/a/chromium.org/chromedriver/) and place it in the same directory as your script, or ensure it is in your system PATH.
3. Run the script using the command:

   python your_script_name.py

4. The script will open a headless Chrome browser, perform the search, and scrape the data, saving it into a CSV file named according to the FILENAME specified in the config.yaml.

## Future Use and Outcomes
### Future Enhancements
- *Support for Multiple Job Profiles and Locations*: Extend the script to handle given keyword profiles and locations in a single run.
- *Parallel Processing*: Implement parallel processing to speed up the data extraction process.
- *Enhanced Error Handling*: Improve error handling to make the script more robust against unexpected webpage changes.
- *Data Enrichment*: Integrate additional data sources to enrich the extracted kryword information.

### Expected Outcomes
- *Automated Data Collection*: Streamlined process for collecting keyword-related data from Google search results.
- *Comprehensive Data Listings*: A CSV file containing detailed of data listings for further analysis and research.
- *Insights into Job Market*: Useful insights into the job market for specific profiles and locations based on the collected data.

## Conclusion
This project provides a robust framework for scraping keyword listings data from Google search results. By leveraging Python, Selenium, and BeautifulSoup, the tool automates the data extraction process, making it efficient and scalable. The flexibility of using a configuration file allows users to easily customize their searches. Future enhancements can further improve the script's functionality and usability.


