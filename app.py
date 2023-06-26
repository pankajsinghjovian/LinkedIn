import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep
import os 
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# importing webdriver

from selenium import webdriver

# Waiting  for an element to be visible before performing an action

# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15'
user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37'


# Setting up the chromium options 
def set_chrome() -> Options:
    # setting up the options for the chromium 
    chrome_options = Options()
    # chrome_options.headless = True
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
    chrome_options.add_argument('--disable-usb-discovery')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_prefs={}
    chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument('--disable-features=InterestCohort')
    chrome_options.experimental_options["prefs"]= chrome_prefs
    chrome_prefs["profile.default_content_settings"]={"images":2}
    return chrome_options

def scrape_jobs():
        driver =webdriver.Chrome(options=set_chrome())
        load_dotenv()
        email= os.getenv('user_name')
        password= os.getenv('password')

        
        link ='https://www.linkedin.com/login'
        driver.get(link)
        sleep(2)
        # wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds

        #locate email form by_class name

        driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(email)
        sleep(4)

        #locate password form by_class name

        driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
        sleep(4)

        # Taking the screenshot of the login page
        driver.get_screenshot_as_file("image1.png")
        sleep(2)

        image1= Image.open("image1.png")
        image_path1="image1.png"
        
        #locate submit button by_xpath
        sign_in_button=driver.find_element(By.XPATH,'//*[@type="submit"]')

        #.click() to open sign_in through gmail
        sign_in_button.click()
        sleep(30)    

        # url1= 'hhttps://www.linkedin.com/jobs/search/?currentJobId=3641532812&f_E=1%2C2&geoId=102713980&keywords=Data%20Analyst&location=India&refresh=true'
        url1= 'https://www.linkedin.com/jobs/search/?currentJobId=3646759097&f_E=1%2C2&f_TPR=r86400&geoId=102713980&keywords=Data%20Analyst&location=India&refresh=true'
        driver.get(url1)
        sleep(5)

        driver.get_screenshot_as_file("image.png")
        sleep(2)
        
        # Loading the image
        image = Image.open("image.png")
        
        # # Showing the images
        # image.show()
        image_path='.image.png'




        # # Creating a for- loop to get the details of each job posted on the page 
        details= [] 
        elements = driver.find_elements(By.CLASS_NAME,'jobs-search-results__list-item')
       
        print (len (elements))
        #listings = element.find_elements(By.CLASS_NAME, 'ember-view')
        for element in elements[:10]:
            element.click()
            sleep(2)

            # Job title 
            job_name = driver.find_element(By.CLASS_NAME,'t-24.t-bold.jobs-unified-top-card__job-title').text
            # Find Name of the company 
            name = driver.find_element(By.CLASS_NAME,'jobs-unified-top-card__company-name').text
            print(name)
            # Find the location of the JOb
            try:
                Location= driver.find_element(By.CLASS_NAME,'jobs-unified-top-card__bullet').text
                print(Location)
            except:
                Location='NA'
                print(Location)
            # Find the work- type 
            try:
                Work_type= driver.find_element(By.CLASS_NAME, 'jobs-unified-top-card__workplace-type').text
            
            except:
                Work_type='NA'
                # Find the Job- Type
            try:
                Job_type= driver.find_element(By.CLASS_NAME, 'jobs-unified-top-card__job-insight').text
            except:
                Job_type='NA'
            try:
                posted=driver.find_element(By.CLASS_NAME,'jobs-unified-top-card__posted-date').text
                print(posted)
            except:
                posted='NA' 
                   
            try:
                about_jobs = driver.find_element(By.CLASS_NAME, 'jobs-box--fadein.jobs-box--full-width.jobs-box--with-cta-large.jobs-description').text
                # print(about_jobs)
                # Years_of_exp = years_of_exp(about_jobs)
                # print(Years_of_exp)
                #numbers = min([re.findall(r"\d+", i)[0] if len(re.findall(r"\d+", i)) else '0' for i in Years_of_exp])    
            except:
                about_jobs ='NA'
            try:
                job_link_class= driver.find_element(By.CLASS_NAME, 'jobs-unified-top-card__content--two-pane')
                job_link= job_link_class.find_element(By.TAG_NAME,'a').get_attribute('href')
                print(job_link)
            except:
                job_link="NA"
                print(job_link)
            try:
                Hiring= driver.find_element(By.CLASS_NAME,'jobs-poster__name.t-14.t-black.mb0').text
            except:
                Hiring="NA"
            # try:
            #     skill = driver.find_element(By.CLASS_NAME, 'app-aware-link.job-details-how-you-match__skills-item-subtitle.t-14.overflow-hidden').text
            # except:
            #     skill="NA"
                

            details.append({
                        'Job Title': job_name,
                        'Company Name':name,
                        'Job Link':job_link,
                        'Location': Location,
                        #'Work Method': Work_type,
                        'Posted On': posted,
                        'Job Description': about_jobs.replace('\n', ' ')

                        })
            # Get the body element and send the PAGE_DOWN key
            body = driver.find_element(By.TAG_NAME,"body")
            body.send_keys(Keys.PAGE_DOWN)
            sleep(0.8)
                

        
        df=pd.DataFrame.from_dict(details)
        df.to_csv('LinkedIn_jobs.csv', index=None)
        df.to_excel('LinkedIn_jobs.xlsx',index= None )
        driver.quit()

if __name__=="__main__":
        
        scrape_jobs()
        import file_sharing
        file_sharing.send_message()
        file_sharing.send_file()
       

      



    