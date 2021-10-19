
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_language(browser):
    browser.get(link)
   
    input1 = browser.find_elements_by_class_name("btn-add-to-basket")
    assert input1, "Элемет не найден"
