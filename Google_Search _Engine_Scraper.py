import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd
import yaml

def selenium_job_extractor(browser, num_pages, records, wait):
    time.sleep(2)
    count = 0  # Counter for the number of jobs
    page_count = 0  # Counter for the number of pages
    clicked_urls = set()  # Set to store URLs of clicked search results
    
    while page_count < num_pages:
        # Wait for search results to load
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "VkpGBb")))
        
        # Find all search results
        search_results = browser.find_elements(By.XPATH, "//div[@class='VkpGBb']")
        
        for result in search_results:
            result_url = result.find_element(By.XPATH, ".//a").get_attribute("href")
            
            if result_url in clicked_urls:
                continue
                
            webdriver.ActionChains(browser).move_to_element(result).perform()
            time.sleep(0.5)  # Wait for scrolling
            
            try:
                result.click()
                time.sleep(2)
                source = browser.page_source
                soup = BeautifulSoup(source, 'html.parser')
                try:
                    company_html = soup.find('div', class_="SPZz6b")
                    company = company_html.text.strip() if company_html else "Not available"

                    rating_html = soup.find('span', class_="fzTgPe Aq14fc")
                    rating = rating_html.text.strip() if rating_html else "Not available"

                    reviews_html = soup.find('span', class_="z5jxId")
                    reviews = reviews_html.text.strip() if reviews_html else "Not available"
                    
                    hours_html = soup.find('span', class_="JjSWRd")
                    hours = hours_html.text.strip() if hours_html else "Not available"

                    phone_html = soup.find('span', class_="LrzXr zdqRlf kno-fv")
                    phone = phone_html.text.strip() if phone_html else "Not available"
                    
                    address_html = soup.find('span', class_="LrzXr")
                    address = address_html.text.strip() if address_html else "Not available"

                    website_html = soup.find('a', class_="n1obkb")
                    website = website_html['href'] if website_html else "Not available"

                    records.append((company, rating, reviews, hours, phone, address, website))
                    
                    count += 1
                except Exception as e:
                    print("Error:", e)
                    continue
            except Exception as e:
                print("Error clicking on search result:", e)
                continue
        
        page_count += 1
        if page_count >= num_pages:
            break
             
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.ID, 'pnnext')))
            next_button.click()
            time.sleep(5)  # Adding a delay to ensure the next page loads completely
        except Exception as e:
            print("Error occurred while clicking next button:", e)
            break

def main():
    # Main function to execute the job scraping process
    
    # Load configuration from YAML file
    with open("config.yaml") as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
        filename = cfg['FILENAME']
        job_profile = cfg['JOB_PROFILE']
        location = cfg['LOCATION']
        num_pages = int(cfg['NUM_PAGES'])

    # Initialize the Chrome WebDriver and set up wait
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 20)
    records = []  # List to store job records
    
    # Construct the Google search URL based on job profile and location
    url = f"https://www.google.com/search?sca_esv=1d62dda5da21c497&rlz=1C1UEAD_enIN1055IN1055&tbs=lf:1,lf_ui:2&tbm=lcl&sxsrf=ACQVn090sAY-KmSz4JDz0eWxXHcAPCN9-w:1714331688279&q={job_profile}+in+{location}&rflfq=1&num=10&sa=X&ved=2ahUKEwjIiLqaz-WFAxUJoGMGHcNxCvcQjGp6BAgiEAE&biw=767&bih=730&dpr=1.25#rlfi=hd:;si:;mv:[[28.732290299999995,77.2392357],[28.546695099999997,77.0153844]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2"
    browser.get(url)
    time.sleep(10)  # Adding a short delay for the page to load completely
    
    # Call the function to extract job information
    selenium_job_extractor(browser, num_pages, records, wait)

    # Create a DataFrame from the records list
    df = pd.DataFrame(records, columns=['Company', 'Rating', 'Reviews', 'Hours', 'Phone', 'Address', 'Website'])
    
    # Define the CSV file path based on the filename and location
    csv_file_path = f"{filename}.csv"
    
    # Save the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False, encoding='utf-8')

    # Quit the WebDriver
    browser.quit()

if __name__ == "__main__":
    main()
