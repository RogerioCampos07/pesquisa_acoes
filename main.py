from src.pesquisa_acoes.services.scrap import TickerScraper

scraper = TickerScraper()

#scraper.search_ticker('CXSE3.SA')

scraper.search_ticker_output_csv('MGLU3.SA')