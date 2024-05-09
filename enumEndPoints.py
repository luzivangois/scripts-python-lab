import requests

url = 'http://localhost:8080/'

with open("wordlist/endpoints.txt", "r") as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas:
    
        endpoint  = linha.strip()
        
        r = requests.get(url+endpoint)
        retorno = r.status_code
        codigo_retorno = str(retorno)
        if (retorno != 404):
            with open("endpoints_validos.txt", "a") as resultado:
                resultado.write("\nURL : "+url+endpoint+"\nStatus Code: "+codigo_retorno)