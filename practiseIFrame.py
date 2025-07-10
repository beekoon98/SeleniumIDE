import time
from operator import truediv

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoIframe():
    def demo_frames(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        time.sleep(3)
        driver.implicitly_wait(100)

        #switch with iframe locator by name
        #external parent iframe
        iframe = driver.find_element(By.XPATH, '//iframe[@id="iframeResult"]')
        driver.switch_to.frame(iframe)
        print("Switched to external parent iframe")
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        #switch to inner iframe by xpath
        innerIFrame = driver.find_element(By.XPATH, '//body/iframe[1]')
        driver.switch_to.frame(innerIFrame)
        print("Switched to Inner iframe")

        #locate the Menu dropdown
        try:
            driver.find_element(By.XPATH, '//a[@aria-label="Menu"]').click()
            print("Clicked Menu dropdown button")
            time.sleep(5)

            try:
                #click on Academy from dropdown options
                academyOption = driver.find_element(By.XPATH, '//a[@title="W3Schools Academy"]')
                driver.execute_script("arguments[0].scrollIntoView(true)", academyOption)
                academyOption.click()
                print("Clicked Academy option")
                time.sleep(5)
                driver.implicitly_wait(200)

                try:
                    pythonButton = driver.find_element(By.XPATH, '//a[normalize-space()="PYTHON"]')
                    print("found PYTHON button")
                    try:
                        WebDriverWait(driver, 200).until(EC.element_to_be_clickable(pythonButton)).click()
                        print("Clicked PYTHON button")
                        time.sleep(5)

                        #click Next button
                        try:
                            nextBtn = driver.find_element(By.XPATH, '//body/div[@class="contentcontainer"]/div[@class="belowtopnavcontainer"]/div[@id="belowtopnav"]/div[@class="w3-row w3-white"]/div[@id="main"]/div[2]/a[2]')
                            print("found Next button")
                            try:
                                WebDriverWait(driver, 200).until(EC.element_to_be_clickable(nextBtn)).click()
                                print("Clicked Next button")
                                time.sleep(5)

                                try:
                                    # next switch back to external parent iframe
                                    driver.switch_to_default_content()
                                    print("Switched back to external parent iframe")
                                    time.sleep(2)
                                    #driver.implicitly_wait(100)

                                    try:
                                        # switch to inner iframe by xpath
                                        innerIFrame2 = driver.find_element(By.XPATH, '/html[1]/body[1]/iframe[2]')
                                        print("found Inner iframe2")
                                        try:
                                            driver.switch_to.frame(innerIFrame2)
                                            print("Switched to Inner iframe 2")
                                        except StaleElementReferenceException:
                                            print("Inner iframe2 Stale now")
                                            innerIFrame2 = driver.find_element(By.XPATH, '/html[1]/body[1]/iframe[2]')
                                            driver.switch_to.frame(innerIFrame2)
                                            print("Switched to Inner iframe 2 from Exception block")
                                        time.sleep(5)
                                        driver.implicitly_wait(100)
                                        try:
                                            pythonButton = driver.find_element(By.XPATH,'/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/input[1]')

                                            print("found search textbox")
                                            # driver.execute_script("arguments[0].scrollIntoView(true)", pythonButton)
                                            try:
                                                WebDriverWait(driver, 200).until(EC.element_to_be_clickable(pythonButton)).click()
                                                print("Clicked search textbox")
                                                time.sleep(5)
                                            except TimeoutException:
                                                print("Timeout to click search textbox")
                                        except NoSuchElementException:
                                            print("Can't find search textbox")

                                    except NoSuchElementException:
                                        print("Can't find Inner iframe 2")

                                except NoSuchElementException:
                                    print("Can't switch back to parent iframe")
                            except TimeoutException:
                                print("Timeout to click Next button")
                        except NoSuchElementException:
                            print("Can't find Next button")
                    except TimeoutException:
                        print("Timeout to click python button")
                except NoSuchElementException:
                    print("Can't find PYTHON button")
                time.sleep(5)
            except NoSuchElementException:
                print("Can't find Academy option")
        except NoSuchElementException:
            print("Can't find Menu dropdown button")

        driver.close()
        driver.quit()
        print(" DONE ")

diframe = DemoIframe()
diframe.demo_frames()


