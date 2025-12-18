"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()

driver.get("https://duckduckgo.com/")
print("page title is:",driver.title)

driver.implicitly_wait(5)

search_box=driver.find_element(By.NAME,"q")

search_box.send_keys("dkte college ichalkaranji")
search_box.send_keys(Keys.RETURN)

print("Later page title:",driver.title)
time.sleep(10)
driver.quit()"""

# import required packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = Options()


options.add_argument("--user-data-dir=C:/temp/selenium-profile")
options.add_argument("--no-first-run")
options.add_argument("--no-default-browser-check")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://duckduckgo.com/")
print("Initial Page Title:", driver.title)
# define wait strategy -- set one time in the application
driver.implicitly_wait(5)

# access the controls on the page
# time.sleep(5)
search_box = driver.find_element(By.NAME, "q")

# interact with the control
# for ch in "dkte college ichalkaranji":
#     search_box.send_keys(ch)
#     time.sleep(0.2)
search_box.send_keys("dkte college ichalkaranji")
search_box.send_keys(Keys.RETURN)

# wait for the result
print("Later Page Title:", driver.title)

# stop the session
time.sleep(10)
driver.quit()



