from src.pesquisa_acoes.services.scrap import TickerScraper
from src.pesquisa_acoes.utils.escreve_csv import search_ticker_output_csv


scraper = TickerScraper()

ticker =scraper.search_ticker('ITSA4.SA')
search_ticker_output_csv(ticker)



