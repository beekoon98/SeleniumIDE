import time
from tokenize import String

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException, \
    NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class javascript_ButtonAlert():
    def js_buttonAlertCall(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
        driver.maximize_window()
        time.sleep(3)
        driver.implicitly_wait(100)

        script = "return document.title;"
        title = driver.execute_script("arguments[0]", script)
        print("Title is: ", title)

        #switch to iframe
        iframe = driver.find_element(By.XPATH, '//iframe[@id="iframeResult"]')
        driver.switch_to.frame(iframe)
        print("Switched to iframe")

        #click button=call function directly
        driver.execute_script("myFunction();")
        time.sleep(5)
        print("clicked button = called function to pop up Alert")

        try:
            WebDriverWait(driver, 100).until(EC.alert_is_present())
            try:
                driver.switch_to.alert.accept()
                print("Accepted Alert")
                time.sleep(3)
            except NoAlertPresentException:
                print("No Alert shown")
        except TimeoutException:
            print("Time out waiting for alert")

        #highlight button in green
        try:
            button = driver.find_element(By.XPATH, '/html[1]/body[1]/button[1]')
            print("found button")
            time.sleep(2)
            try:
                driver.execute_script("arguments[0].style.border='5px solid green';", button)
                time.sleep(5)
                print("highlighted button in green")
            except TimeoutException:
                print("can't highlight button in green")
        except NoAlertPresentException:
            print("Can't find button")

        #open new window
        try:
            #open new empty tab first
            driver.execute_script("window.open();")

            #switch to newly opened tab
            driver.switch_to.window(driver.window_handles[1])

            #navigate to new url in new tab
            driver.get("https://google.com")

            print("Google opened")
            time.sleep(5)

            #get the Search textbox, and keyword to search
            try:
                driver.execute_script("return document.getElementsByName('q')[0].value='Selenium Automation';")

                print("keyed in search textbox")
                time.sleep(3)

                try:
                    #find & click Search button
                    searchButton = driver.find_element(By.XPATH, '//div[@class="FPdoLc lJ9FBc"]//input[@name="btnK"]')
                    print("found Search button")
                    try:
                        searchButton.click()
                        print("Search button clicked!")
                        time.sleep(4)
                    except TimeoutException:
                        print("Timeout to click Search button")
                except NoSuchElementException:
                    print("can't find Search button")

            except TimeoutException:
                print("Timeout to key in search textbox")
        except TimeoutException:
            print("can't open Google")

        driver.close()
        driver.quit()
        print(" DONE ")

js = javascript_ButtonAlert()
js.js_buttonAlertCall()