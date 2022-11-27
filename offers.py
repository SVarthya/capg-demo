# from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Data import reading_objects
offers_object = reading_objects.read_locators()
print(offers_object)
# path = r'C:\Users\SRAVANI\Desktop\drivers.sel\chromedriver.exe'
# driver = webdriver.Chrome(path)
# driver.get('https://www.makemytrip.com/')
# driver.maximize_window()
# driver.implicitly_wait(30)
# driver.maximize_window()
time.sleep(2)
class Offers_module:
    def __init__(self,driver):
        self.driver = driver

    ##HOLIDAYS##

    def holidays(self):
        self.driver.find_element(*offers_object['click_button1']).click()
    def button_Holidays(self):
        self.driver.find_element(*offers_object['click_button2']).click()
        time.sleep(5)
    def button_Holidays_offer(self):
        self.driver.find_element(*offers_object['click_button3']).click()
        time.sleep(5)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        time.sleep(5)
    def Holidays_booknow_button(self):
        self.driver.find_element(*offers_object['click_button4']).click()
        time.sleep(5)
    def Holidays_skip1(self):
        self.driver.find_element(*offers_object['click_button5']).click()
        time.sleep(5)
    def Holidays_skip2(self):
        self.driver.find_element(*offers_object['click_button6']).click()
        time.sleep(5)
    def Holidays_skip3(self):
        self.driver.find_element(*offers_object['click_button7']).click()
        time.sleep(5)
    def Holidays_skip4(self):
        self.driver.find_element(*offers_object['click_button8']).click()
        time.sleep(1)
    def Holidays_close(self):
        self.driver.find_element(*offers_object['click_button9']).click()
        time.sleep(1)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        time.sleep(10)

    def trains(self):

        self.driver.find_element(*offers_object['click_button10']).click()
        time.sleep(3)
    def trains_Offer(self):
        self.driver.find_element(*offers_object['click_button11']).click()
        time.sleep(3)
        # ac_obj = ActionChains(self.driver)
        # ac_obj.send_keys(Keys.PAGE_DOWN).perform()

    def trains_booknow_button(self):
        ac_obj = ActionChains(self.driver)
        ac_obj.send_keys(Keys.PAGE_DOWN).perform()
        self.driver.find_element(*offers_object['click_button10']).click()
        time.sleep(3)



# offers = Offers_module(driver)
# offers.holidays()
# offers.trains()
