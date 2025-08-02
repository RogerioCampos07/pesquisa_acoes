from src.pesquisa_acoes.utils.escreve_csv import search_ticker_output_csv, search_tickers_output_csv
from src.pesquisa_acoes.services.scrap import TickerScraper
from src.pesquisa_acoes.services.clients import SearchTicker

#scraper = TickerScraper()
client = SearchTicker()

# Exemplo de scrap e registro 1 ticket em arquivo .csv
# ticker = scraper.search_ticker("ITSA4.SA")
# search_ticker_output_csv(ticker)

# Exemplo de scrap e registro de uma lista de tickers em arquivo .csv
# acoes_brasileiras = ["VALE3.SA", "ITUB4.SA", "BBDC4.SA", "BBAS3.SA"]
# search_tickers_output_csv(acoes_brasileiras)

#evemplo de consulta de 1 ticker
ticker = client.get_info_ticker("VALE3")
search_ticker_output_csv(ticker)
