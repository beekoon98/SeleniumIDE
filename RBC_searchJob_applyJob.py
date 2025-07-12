import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException, \
    NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RBC():
    def rbc(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.rbcroyalbank.com/personal.html")
        driver.maximize_window()
        time.sleep(3)
        driver.implicitly_wait(100)

        driver.find_element(By.XPATH, '//button[@id="onetrust-accept-btn-handler"]').click()

        try:
            careerBtn = driver.find_element(By.XPATH, '//a[@id="footer-careers-at-rbc"]')
            driver.execute_script("arguments[0].scrollIntoView(true)", careerBtn)
            print("found Career button")
            careerBtn.click()
            print("clicked Career button")
            time.sleep(3)
            #driver.implicitly_wait(100)
            try:
                #scroll to bottom of page first
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(3)
                searchTxtbox = driver.find_element(By.XPATH, '//input[@placeholder="Search for Job title or location"]')
                driver.execute_script("arguments[0].scrollIntoView(true)", searchTxtbox)
                print("found search text box")
                searchTxtbox.send_keys("automation")
                time.sleep(3)
                print("keyed in search text box")
                time.sleep(3)

                try:
                    driver.find_element(By.XPATH, '(//span[contains(text(),"Search")])[2]').click()
                    print("Clicked search button")
                    time.sleep(3)

                    try:
                        pg2Btn = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Page 2"]')
                        driver.execute_script("arguments[0].scrollIntoView(true)", pg2Btn)
                        try:
                            pg2Btn.click()
                            time.sleep(3)
                            print("Clicked page 2 btn")

                            #click Next button
                            try:
                                nextBtn = driver.find_element(By.XPATH, '//ppc-content[normalize-space()="Next"]')
                                driver.execute_script("arguments[0].scrollIntoView(true)", nextBtn)
                                nextBtn.click()
                                time.sleep(3)
                                print("Clicked Next btn")

                                #select a job
                                try:
                                    jobSelection = driver.find_element(By.XPATH, '//span[contains(text(),"Associate Data Scientist, U.S. Data Strategy")]')
                                    driver.execute_script("arguments[0].scrollIntoView(true)", jobSelection)
                                    jobSelection.click()
                                    time.sleep(3)
                                    print("selected job")

                                    #Apply now btn click
                                    try:
                                        applyNowBtn = driver.find_element(By.XPATH, '//a[@title="Apply Now"]')
                                        driver.execute_script("arguments[0].scrollIntoView(true)", applyNowBtn)
                                        applyNowBtn.click()
                                        time.sleep(3)
                                        print("clicked Apply Now btn")
                                    except NoSuchElementException:
                                        print("can't Apply Now button")
                                except NoSuchElementException:
                                    print("can't find job")
                            except NoSuchElementException:
                                print("can't find Next button")
                        except TimeoutException:
                            print("timeout clicking pg 2 btn")
                    except NoSuchElementException:
                        print("can't find pg 2 button")
                except NoSuchElementException:
                    print("can't find search button")
            except NoSuchElementException:
                print("can't find search text box")
        except NoSuchElementException:
            print("can't find Career button")

        driver.close()
        driver.quit()
        print(" DONE ")
obj = RBC()
obj.rbc()