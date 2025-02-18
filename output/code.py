
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
			
from selenium.webdriver.common.action_chains import ActionChains
driver.execute_script('window.open()')
driver.switch_to.window(driver.window_handles[-1])
driver.get('https://pomofocus.io/')

element_to_click = driver.find_element(By.XPATH, 'html/body/main/div/div/div/div[3]/div/div[3]/div[3]')
element_to_click.click()


element_to_click = driver.find_element(By.XPATH, 'html/body/main/div/div/div/div[3]/div/div[3]/div[3]/div[2]/div/button[2]')
element_to_click.click()


element_to_click = driver.find_element(By.XPATH, 'html/body/main/div/div/div/div[3]/div/div[3]/div[3]/div[2]/div/button[2]')
element_to_click.click()


element_to_click = driver.find_element(By.XPATH, 'html/body/main/div/div/div/div[3]/div/div[3]/div/div/div/button/img')
element_to_click.click()


element_to_click = driver.find_element(By.XPATH, 'html/body/main/div/div/div/div[3]/div/div[3]/div/div/div/div/div[7]')
element_to_click.click()


element_to_click = driver.find_element(By.XPATH, 'html/body/main/div/div/div/div[3]/div/div[3]/div/div/div/button/img')
element_to_click.click()


element_to_click = driver.find_element(By.XPATH, 'html/body/main/div/div/div/div[3]/div/div[3]/div/div/div/div/div[7]')
element_to_click.click()


element_to_click = driver.find_element(By.XPATH, 'html/body/main/div/div/div/div[3]/div/div[3]/div/div/div/button/img')
element_to_click.click()


element_to_click = driver.find_element(By.XPATH, 'html/body/main/div/div/div/div[3]/div/div[3]/div/div/div/div/div[7]')
element_to_click.click()

