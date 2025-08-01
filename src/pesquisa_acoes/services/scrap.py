from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from loguru import logger






class TickerScraper:
    def __init__(self):
        self.url = 'https://finance.yahoo.com/'
        self.options = self.options_chromedriver()
        self.driver = self.webdrive()
        self.implicity_wait()
        self.get_url()

        


    def options_chromedriver(self):
        options = Options()
        options.add_argument("--incognito")
        return options

    def webdrive(self):
        driver = webdriver.Chrome(options=self.options)
        return driver
        
    def implicity_wait(self,time=10):
        self.driver.implicitly_wait(time)

    

    def get_url(self):
        logger.info('Abrindo navegador')
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
    
    def search_ticker(self, ticker):
        
        try:
            search_box = self.driver.find_element(By.ID, "ybar-sbq")
            search_box.click()
            search_box.send_keys(ticker)
            search_box.send_keys(Keys.ENTER)
            logger.info('código da ação digitado')
            
            logger.info('Obtendo informação')
            try:
                get_info_ticker = self.driver.find_element(By.XPATH,"//h1[@class='yf-4vbjci']")
                get_price_ticker = self.driver.find_element(By.XPATH,"//li[span[@title='Bid']]/span[@class='value yf-1b7pzha']")
                stock_name = get_info_ticker.text.split('(')[0]
                cod_stock_name = get_info_ticker.text.split('(')[1][:-1].split('.')[0]
                price = get_price_ticker.text.split()[0]
                date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                data = {}
                data = {'cod_stock_name':cod_stock_name,'stock_name':stock_name,'price':price,'date':date}
                logger.info('Informações obtidas com sucesso')
                

            except NoSuchElementException:
                logger.error('Informações não encontradas')
            
            
        except UnboundLocalError:
            logger.error('Não foi realizar a pesquisa')

        finally:
            logger.info('Fechando navegador')
            self.driver.quit()
            logger.info('Até breve')
        return data
           

            

            


    






