from bs4 import BeautifulSoup
import requests

url = "https://irancell.ir/o/1001/mobile-internet-packages"
response = requests.get(url)
print(response.status_code)
