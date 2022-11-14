from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r"C:\Users\Krishna C Hadapad\PycharmProjects\PythonTesting\driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.implicitly_wait(4)

driver.get(r"https://rahulshettyacademy.com/angularpractice/")

#  //a[contains(@href, 'shop')]    XPATH

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productname = product.find_element(By.XPATH, "div/h4/a").text
    if productname == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

driver.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()

success_message = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in success_message
