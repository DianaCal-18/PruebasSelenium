import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_username_by_id():
    driver = webdriver.Chrome()
    driver.get("https://dianacal-18.github.io/StoreProject/login.html")
    driver.find_element(By.ID,"username").send_keys("Diana")
    time.sleep(3)

def test_password_by_id():
    driver = webdriver.Chrome()
    driver.get("https://dianacal-18.github.io/StoreProject/login.html")
    driver.find_element(By.ID, "password").send_keys("jaydbeuioq338*")

    time.sleep(3)

def test_btn_home():
    driver = webdriver.Chrome()
    driver.get("https://dianacal-18.github.io/StoreProject/index.html")
    driver.find_element(By.NAME, "login").click()

    time.sleep(3)

def test_element_co():
    driver = webdriver.Chrome()
    driver.get("https://dianacal-18.github.io/StoreProject/")
    driver.find_element(By.NAME, "carrito").click()
    time.sleep(3)


def test_menu_element():
    driver = webdriver.Chrome()
    driver.get("https://dianacal-18.github.io/StoreProject/")
    driver.find_element(By.NAME, "menu").click()
    time.sleep(3)
