import csv

from loguru import logger


def search_ticker_output_csv(dados_dicionario):
    if not dados_dicionario:
        logger.warning("Dados não encontrados")
        return logger.info("insira o código da ação")
    dados = dados_dicionario.keys()
    try:
        with open("assests/tickers.csv", "a", encoding="utf8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=dados)
            writer.writerow(dados_dicionario)
    except Exception as e:
        logger.error(e)

    return dados
