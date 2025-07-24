from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")


url ='https://www.infomoney.com.br/cotacoes/b3/'

driver = webdriver.Chrome(options=chrome_options)

try:
    print('Abrindo navegador')
    driver.get(url) 
finally:
    print('Fechando navegador')
    driver.quit()
