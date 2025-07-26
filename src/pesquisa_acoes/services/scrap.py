from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from csv import writer
from datetime import datetime





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
        print('Abrindo navegador')
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
    
    def search_ticker(self, ticker):
        
        try:
            informations = []
            search_box = self.driver.find_element(By.ID, "ybar-sbq")
            search_box.click()
            search_box.send_keys(ticker)
            search_box.send_keys(Keys.ENTER)
            print('código da ação digitado')
            get_info_ticker = self.driver.find_element(By.XPATH,"//h1[@class='yf-4vbjci']")
            get_price_ticker = self.driver.find_element(By.XPATH,'//*[@id="nimbus-app"]/section/section/section/article/section[2]/div/ul/li[3]/span[2]')
            stock_name = get_info_ticker.text
            price = get_price_ticker.text.split()[0]
            informations = [stock_name,price]
            print(get_info_ticker.text)
            print(get_price_ticker.text.split()[0])
            print('Informações obtidas')
            return informations

        finally:
            print('Fechando navegador')
            self.driver.quit()

            
    def search_ticker_output_csv(self, ticker):
        dados = self.search_ticker(ticker)
        stock_name = dados[0]
        price = dados[1]
        
        
        date = datetime.now().strftime('%d-%m-%Y')
        time = datetime.now().strftime('%H:%M:%S')
        informations = [stock_name,price,date,time]
        try:
            with open('tickers.csv','a',encoding='utf8',newline='') as f:
                csv_writer = writer(f)
                csv_writer.writerow(informations)
        except:
            pass


    






