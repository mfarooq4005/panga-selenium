import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time as t
from selenium.webdriver.common.by import By


def setup_function():
    global driver
    #hub_url = "http://192.168.10.9:4444/wd/hub"
    #driver = webdriver.Remote(command_executor=hub_url, desired_capabilities={"browserName": "chrome"})
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get(("https://apps.eduportal-pk.com/EduPortal/Production/"))
    driver.maximize_window()
    driver.implicitly_wait(10)


def teardown_function():
    driver.quit()


@pytest.mark.parametrize("username,password",
                         [('ambreen2015@gmail.com', 'azam@iqbal.')])
def test_login_details(username, password):
    print("My pytest login")
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/section/form/div[1]/input').send_keys(username)
    # driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/section/form/div[2]/input').send_keys(password)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/section/form/div[4]/input').click()
    allure.attach(driver.get_screenshot_as_png(), name="justme is here", attachment_type=AttachmentType.PNG)
    time.sleep(.1)