import csv

def search_ticker_output_csv(dados_dicionario):
    dados = dados_dicionario.keys() 
    try:
        with open('assests/tickers.csv','a',encoding='utf8',newline='') as f:
            writer = csv.DictWriter(f,fieldnames=dados)
            writer.writerow(dados_dicionario)
    except:
        pass
        
    return dados

            
        



