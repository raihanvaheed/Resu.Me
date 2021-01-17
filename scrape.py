import os
import selenium
from selenium import webdriver
from time import sleep
from PIL import Image
import io
import requests
from selenium.common.exceptions import *
import csv
import atexit

def save():
    # Anounce finish and write to csv
    print()
    print('Aggregated {0} job descriptions and titles'.format(len(JobTitles)))
    
    if (filename := input('Data file name (saved as csv): ')) != '':
        with open(filename + '.csv', 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            for i in range(len(JobTitles)):
                try:
                    writer.writerow([i, JobTitles[i].replace('\n', '\\n'), JobDescriptions[i].replace('\n', '\\n'), URLs[i]])
                except Exception as err:
                    print('Error with element {0}'.format(i))
                    print(err)

atexit.register(save)

# Selenium webdriver
driver = webdriver.Chrome('C:/Users/jacob/Downloads/chromedriver_win32/chromedriver.exe')
search_url = "https://{country}indeed.com/jobs?q={job}&l={location}&start={num}"

# Variables
job_number = 0
job_type = 'software developer'.replace(' ', '+')
city = 'Toronto'.replace(' ', '+')
country_code = 'ca'
page_count = 20
total_jobs = 0

# Get correct domain
if (domain := country_code + '.') == 'us.':
    domain = ''

# Job description aggregate
JobDescriptions = []
JobTitles = []
URLs = []

try :
    while True:
        driver.switch_to.window(driver.window_handles[0])
        # Goto page
        driver.get(search_url.format(country=domain, job=job_type, location=city, num=str(job_number)))
        sleep(1)

        # Captcha handling
        if 'solve' in driver.title:
            print('Please complete the captcha :(')
        while 'solve' in driver.title:
            sleep(1)

        while 'Jobs' not in driver.title:
            driver.get(search_url.format(country=domain, job=job_type, location=city, num=str(job_number)))
            sleep(5)

        # Popup handling
        try:
            close_button = driver.find_element_by_id('popover-x')
            close_button.click()
        except NoSuchElementException:
            nothing = None

        sleep(1)

        # Get job elements
        JobResults = driver.find_elements_by_xpath("//a[contains(@class,'jobtitle turnstileLink ')]")
        # Click each job element
        for i in  range(0,len(JobResults)):
            job_item = JobResults[i]
            # Prevent losing focus
            driver.switch_to.window(driver.window_handles[0])
            try:
                job_item.click()
                sleep(0.25)

                if domain:
                    description = driver.find_element_by_id('vjs-desc').text
                    title = driver.find_element_by_id('vjs-jobtitle').text
                else:
                    driver.switch_to.frame(driver.find_element_by_id('vjs-container-iframe'))
                    description = driver.find_element_by_id('jobDescriptionText').text
                    title = driver.find_element_by_class_name('jobsearch-JobInfoHeader-title').text.replace('\n- job post', '')
                
                JobDescriptions.append(description)
                JobTitles.append(title)
                URLs.append(driver.current_url)
                total_jobs += 1
                print('Job {0}: {1}'.format(total_jobs, title))
            except Exception as err:
                print('Job {0}: ERROR!'.format(total_jobs))
                print(err)
            finally:
                sleep(0.25)

        # Increase page count
        page_count -= 1
        if page_count > 0:
            job_number += 10
        else:
            break
except KeyboardInterrupt:
    print('Program stopped!')
finally:
    save()

