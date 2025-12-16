from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options=Options()
chrome_options.add_argument("--headless")
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://sunbeaminfo.in/")
print("Page Title:",driver.title)

driver.implicitly_wait(5)

intern=driver.find_element(By.ID,"INTERNSHIP").click()
available_internship_programs=driver.find_elements(By.XPATH,"https://sunbeaminfo.in/#collapseSix")
available_internship_programs=driver.find_elements(By.XPATH,"//*[@id=collapseSix]/div/div/div[2]")