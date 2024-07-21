from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import re

#? instantiate options
options = webdriver.ChromeOptions()

#? run browser in headless mode
options.headless = True

#? instantiate driver
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=options
)

#? load website
url = "https://mrbilit.com/buses/isfahan_kaveh-yazd?departureDate=1403-04-31"

#? get the entire website content
driver.get(url)

#? select elements by class name
elements = driver.find_elements(By.CLASS_NAME, "route-section")

txt = ""
for element in elements:
    x = re.findall(r"[^\n*]", element.text)
    txt = ""
    for i in x:
        txt += i
    print(txt)
