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
driver.maximize_window()

driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys("bee-koon.tan@qornerstone.com")
driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").send_keys("qornerstoneBK9988!!")
driver.find_element(By.ID, "btnlogin").click()

driver.implicitly_wait(100)
driver.find_element(By.CSS_SELECTOR, ".d-inline-block").click()

#left panel close
#explicit wait,only wait for this element
WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '// *[ @ class = "fa fa-angle-left"]'))).click()

#Booking card button click
try:
    card = driver.find_element(By.XPATH, '//a[@href="https://qa-mtw-web.azurewebsites.net/staff/booking/today"]')
    time.sleep(10)
    print("Booking card found")
    driver.implicitly_wait(500)
    try:
        # scroll page to show the card
        driver.execute_script("arguments[0].scrollIntoView(true)", card)
        WebDriverWait(driver, 500).until(EC.element_to_be_clickable(card)).click()
        print("Booking card clicked")
        time.sleep(10)
        driver.implicitly_wait(500)
        '''
        # left panel close
        # explicit wait,only wait for this element
        WebDriverWait(driver, 300).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="fa fa-angle-left"]'))).click()
        '''
        try:
            bookNewButton = driver.find_element(By.XPATH,'//a[text()="Book New"]')
            print("Book New button found")
            time.sleep(10)
            driver.implicitly_wait(100)

            try:
                WebDriverWait(driver, 500).until(EC.element_to_be_clickable(bookNewButton)).click()
                print("Book New button clicked")
                driver.implicitly_wait(200)

                try:
                    blockDropdown = driver.find_element(By.XPATH, '//button[@title="Select Block"]')
                    print("Select Block dropdown found")

                    try:
                        WebDriverWait(driver, 500).until(EC.element_to_be_clickable(blockDropdown)).click()
                        print("Select Block dropdown clicked")

                        block37 = driver.find_element(By.XPATH, '//li[@data-original-index="45"]')
                        print("Block 37 found")
                        driver.execute_script("arguments[0].scrollIntoView(true)", block37)
                        WebDriverWait(driver, 100).until(EC.element_to_be_clickable(block37)).click()
                        print("Block 37 clicked")

                        resident = driver.find_element(By.XPATH, '//button[@title="Select Resident"]')
                        print("Resident dropdown found")
                        time.sleep(10)
                        driver.implicitly_wait(200)
                        WebDriverWait(driver, 300).until(EC.element_to_be_clickable(resident)).click()
                        print("Resident dropdown clicked")

                        topResident = driver.find_element(By.XPATH, '//span[normalize-space()="bkNewOccupier"]')
                        print("top Resident found")
                        try:
                            WebDriverWait(driver, 200).until(EC.element_to_be_clickable(topResident)).click()
                            print("top Resident selected")
                        except TimeoutException as eResidentSelect:
                            print(f"Timed out to Select Resident: {eResidentSelect}")

                        facility = driver.find_element(By.XPATH, '//div[@data-facilityname="abkSwimming Pool"]')
                        print("Facility found")
                        try:
                            # scrol page to show the Facility
                            driver.execute_script("arguments[0].scrollIntoView(true)", facility)
                            WebDriverWait(driver, 500).until(EC.element_to_be_clickable(facility)).click()
                            print("Facility selected")

                            #select date
                            #select hardcoded date first
                            date = driver.find_element(By.XPATH, '// td[ @ id = "Jul-11-2025"]')
                            print("Date 11 Jul found")
                            try:
                                # scroll page to show the textbox
                                driver.execute_script("arguments[0].scrollIntoView(true)", date)
                                WebDriverWait(driver, 200).until(EC.element_to_be_clickable(date)).click()
                                print("Date selected")

                                #select time slot
                                timeslot = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[2]/section[2]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]')
                                print("1st time slot found")

                                try:
                                    #scroll to show top of page
                                    driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
                                    time.sleep(2)
                                    WebDriverWait(driver, 500).until(EC.element_to_be_clickable(timeslot)).click()
                                    print("1st Time slot selected")
                                    time.sleep(2)

                                    continueButton = driver.find_element(By.CSS_SELECTOR, "#buttonbookslot")
                                    print("Continue button found")

                                    try:
                                        driver.execute_script("arguments[0].scrollIntoView(true)", continueButton)
                                        time.sleep(2)
                                        WebDriverWait(driver, 500).until(EC.element_to_be_clickable(continueButton)).click()
                                        print("Continue button clicked")
                                    except NoSuchElementException as econtinueButton:
                                        print(f"No such element-Continue Button: {econtinueButton}")

                                except NoSuchElementException as eSlot:
                                    print(f"No such element-Time slot: {eSlot}")
                            except NoSuchElementException as eDateException:
                                print(f"No such element-Date: {eDateException}")
                        except TimeoutException as eFacilitySelect:
                                print(f"Timed out to Select Facility: {eFacilitySelect}")

                    except TimeoutException as eBlockClick:
                        print(f"Timed out to click Select Block dropdown: {eBlockClick}")
                except TimeoutException as eBlock:
                    print(f"Timed out to find Block dropdown: {eBlock}")
            except TimeoutException as e4:
                print(f"Timed out to click Book New button: {e4}")
        except NoSuchElementException as e3:
            print(f"No such element-Book New button: {e3}")
    except TimeoutException as e2:
        print(f"Timed out to click Booking card: {e2}")
except NoSuchElementException as e1:
    print(f"No such element-Booking card: {e1}")

time.sleep(5)
driver.implicitly_wait(100)

#Facility, date, time slot selected
#Pay by Cash & Confirm booking
try:
    #select Cash radio button
    cashRadio = driver.find_element(By.CSS_SELECTOR, "label[for='paymentmethod3']")
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable(cashRadio)).click()
    print("Cash radio button clicked")

    driver.implicitly_wait(100)
    try:
        confirmButton = driver.find_element(By.CSS_SELECTOR, "#buttonbookingconfirm")
        # scroll page to show the Confirm button
        driver.execute_script("arguments[0].scrollIntoView(true)", confirmButton)
        try:
            WebDriverWait(driver, 100).until(EC.element_to_be_clickable(confirmButton)).click()
            print("Confirm booking button clicked")

            #dialog box pop up
            # click Ok on confirmation dialog
            try:
                okDialog = driver.find_element(By.XPATH, "//button[@id='modalbookingconfirmyes']")
                print("OK button in confirmation dialog found")
                try:
                    WebDriverWait(driver, 200).until(EC.element_to_be_clickable(okDialog)).click()
                    print("OK button in confirmation dialog clicked")
                    time.sleep(10)
                except Exception as eOKClick:
                    print(f"Error clicking for OK button in confirmation dialog: {eOKClick}")
            except Exception as eOK:
                print(f"Error looking for OK button in confirmation dialog: {eOK}")
        except Exception as eConfirm:
            print(f"Error clicking for OK button in confirmation dialog: {eConfirm}")
        driver.implicitly_wait(200)
    except Exception as e:
        print(f"Error waiting for Confirm booking button: {e}")
except Exception as e:
    print(f"Error waiting for Cash radio button: {e}")

time.sleep(30)
driver.implicitly_wait(2000)
#Logout
try:
    #click logout button
    logoutButton = driver.find_element(By.XPATH, '//a[@id="leftmenulogout"]')
    WebDriverWait(driver, 2000).until(EC.element_to_be_clickable(logoutButton)).click()
    print("logout button clicked")

    driver.implicitly_wait(1000)
    try:
        confirmLogoutButton = driver.find_element(By.XPATH, '//button[@id="buttonlogoutconfirm"]')
        WebDriverWait(driver, 2000).until(EC.element_to_be_clickable(confirmLogoutButton)).click()
        print("Yes, confirm logout button clicked")
    except Exception as e1:
        print(f"Error waiting to click on logout button: {e1}")
except Exception as e:
    print(f"Error looking for logout button: {e}")

time.sleep(5)
driver.close()
driver.quit()
print(" DONE ")