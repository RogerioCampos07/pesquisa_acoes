from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from time import sleep


chrome_options = Options()
chrome_options.add_argument("--incognito")


url ='https://finance.yahoo.com/'

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)




try:

    print('Abrindo navegador')
    driver.get(url) 
    # clicar na caixa de pesquisa
    
    caixa_input = driver.find_element(By.ID,"ybar-sbq")
    caixa_input.click()

    # DIGITA  CÓDIGO DA AÇÃO

    caixa_input.send_keys('SBSP3.SA')
    print('código da ação digitado')
    # ENTER
    caixa_input.send_keys(Keys.ENTER)
    print('Obtendo a informação')
    info = driver.find_element(By.XPATH,"//h1[@class='yf-4vbjci']")
    preco = driver.find_element(By.XPATH,'//*[@id="nimbus-app"]/section/section/section/article/section[2]/div/ul/li[3]/span[2]')
    print(info.text)
    print(preco.text.split()[0])


    

    


finally:
    print('Fechando navegador')
    #driver.quit()


