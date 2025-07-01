import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.devtools.v135.fed_cm import click_dialog_button
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://qa-mtw-web.azurewebsites.net/staff/events")
driver.set_window_size(1500, 1000)
driver.maximize_window()

driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys("bee-koon.tan@qornerstone.com")
driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").send_keys("qornerstoneBK9988!!")
driver.find_element(By.ID, "btnlogin").click()

driver.implicitly_wait(100)
driver.find_element(By.CSS_SELECTOR, ".d-inline-block").click()
time.sleep(5)

#left panel close
WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '// *[ @ class = "fa fa-angle-left"]'))).click()

#driver.find_element(By.XPATH, '// *[ @ class = "fa fa-angle-left"]').click()
time.sleep(5)

#Feedback card button click
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/section[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/a").click()

driver.implicitly_wait(100)
try:
    #finally can find the element with this line, after studying Inspect and youtube a million times!!

    dropdownDiv = driver.find_element(By.XPATH, '// *[ @ class = "btn-group bootstrap-select"]')
    time.sleep(10)
    print("dropdown div found")
    driver.implicitly_wait(1000)
    try:
        # click on Block dropdown to show all options
        WebDriverWait(driver, 1000).until(EC.element_to_be_clickable(dropdownDiv)).click()
        print("dropdown clicked")
        try:
            option = driver.find_element(By.CSS_SELECTOR, 'li[data-original-index="45"]')
            WebDriverWait(driver, 500).until(EC.element_to_be_clickable(option)).click()
            print("Block 37 selected")
            time.sleep(10)
            driver.implicitly_wait(500)
            try:
                #select Feedback record to open
                feedbackRecord = driver.find_element(By.XPATH, '(//td[@class ="whitespacenowrap print-no-one-line no-print"])[1]')

                WebDriverWait(driver, 500).until(EC.element_to_be_clickable(feedbackRecord)).click()
                print("Feedback record opened")
                time.sleep(10)
                driver.implicitly_wait(800)
                try:
                    # post reply on Feedback record
                    #find the textbox
                    replyTextbox = driver.find_element(By.XPATH, '//textarea[@placeholder="Your feedback"]')

                    #scroll page to show the textbox
                    driver.execute_script('arguments[0].scrollIntoView(true)', replyTextbox)

                    replyTextbox.send_keys("ok great!!")
                    print("Reply posted on Feedback record")

                    time.sleep(10)
                    driver.implicitly_wait(200)

                    postButton = driver.find_element(By.XPATH, '//button[@class ="btn btn-theme-orange btn-small postrpl-btn"]')
                    WebDriverWait(driver, 500).until(EC.element_to_be_clickable(postButton)).click()
                    print("Post button clicked!")


                    yesButton = driver.find_element(By.XPATH, '/html[1]/body[1]/div[21]/div[1]/div[1]/div[2]/div[5]/button[2]')
                    WebDriverWait(driver, 500).until(EC.element_to_be_clickable(yesButton)).click()
                    print("Yes button clicked!")
                except Exception as e:
                    print(f"Error waiting for textbox: {e}")
            except TimeoutException:
                print("Timed out to open Feedback record")
        except TimeoutException:
            print("Timed out to select Block 37")
    except TimeoutException:
        print("Timed out to click dropdown")
except NoSuchElementException:
    print("dropdown not found")

time.sleep(5)
driver.implicitly_wait(500)

try:
    #click logout button
    logoutButton = driver.find_element(By.XPATH, '//a[@id="leftmenulogout"]')
    WebDriverWait(driver, 500).until(EC.element_to_be_clickable(logoutButton)).click()
    print("logout button clicked")

    driver.implicitly_wait(500)
    confirmLogoutButton = driver.find_element(By.XPATH, '//button[@id="buttonlogoutconfirm"]')
    WebDriverWait(driver, 500).until(EC.element_to_be_clickable(confirmLogoutButton)).click()
    print("Yes, confirm logout button clicked")
except Exception as e:
    print(f"Error waiting for logout button: {e}")

time.sleep(5)
driver.close()
driver.quit()
print(" DONE ")