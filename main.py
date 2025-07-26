from src.pesquisa_acoes.services.scrap import TickerScraper

scraper = TickerScraper()

#scraper.search_ticker('BBAS3.SA')
scraper.search_ticker_output_csv('BBAS3.SA')