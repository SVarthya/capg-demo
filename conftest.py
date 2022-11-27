import pytest
from selenium import webdriver
from Library.config import Config
from selenium.webdriver.firefox.options import Options

#Cross Browsing
firefox_Driver_path = r"C:\Users\SRAVANI\Desktop\drivers.sel\geckodriver.exe"
@pytest.fixture(params=["Edge","Firefox","Chrome"])
def _driver(request):




    if request.param == "Firefox":
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=firefox_Driver_path, options=options)


    elif request.param == "Edge":
        driver = webdriver.Edge(Config.Edge_Driver_Path)



    elif request.param == "Chrome":
        driver = webdriver.Chrome(Config.ChromePath_Driver_Path)



    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(50)
    yield driver
    print(driver.title)
    # driver.save_screenshot("text_loginpage.png")
    driver.close()