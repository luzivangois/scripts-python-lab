import requests

# API Java
# url = 'http://localhost:8080/'

# API .Net
url = 'http://localhost:5127/'

with open("wordlist/endpoints.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
    
        endpoint  = line.strip()
        
        r = requests.get(url+endpoint)
        response = r.status_code
        response_code = str(response)
        if (response != 404):
            with open("endpoints_validos.txt", "a") as result:
                result.write("\nURL : "+url+endpoint+"\nStatus Code: "+response_code)