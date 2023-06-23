# importing webdriver from selenium
from selenium import webdriver
from time import sleep
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

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

# Setting up the chromium options 
def set_chrome() -> Options:
    # setting up the options for the chromium 
    chrome_options = Options()
    chrome_options.headless = True
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

 
# Here Chrome  will be used
driver = webdriver.Chrome(options=set_chrome())
 
# URL of website
url1= 'https://www.linkedin.com/jobs/search/?currentJobId=3638102771&f_E=1%2C2&f_TPR=r86400&keywords=%20Data%20Analyst'

 
# Opening the website
driver.get(url1)
 
driver.get_screenshot_as_file("image.png")
sleep(2)
 
# Loading the image
image = Image.open("image.png")
 
# # Showing the images
# image.show()
image_path='./image.png'
image.save(image_path)
import file_sharing
file_sharing.send_message()
file_sharing.send_file()