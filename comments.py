import requests

# Definindo a classe users
class Comments:

    def __init__(self, user_id):
        self.user_id = user_id
        self.base_url = f'http://localhost:8000/users/{user_id}/posts/comments'

    def list(self):
        url = self.base_url
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError("ID inválido "+str(response.status_code))

    def read(self, user_id):
        url = self.base_url+str(user_id)
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError("ID inválido")

    def delete(self, user_id):
        url = self.base_url+str(user_id)
        response = requests.delete(url)

        if response.status_code == 204:
            return True
        else:
            raise ValueError("ID inválido")

    def create(self, user_data):
        url = self.base_url

        response = requests.post(url, json=user_data)
        if response.status_code == 201:
            return response.json()
        else:
            raise ValueError("Problema na execução")

    def update(self, user_id, user_data):
        url = self.base_url+str(user_id)+"/"
        user_data = dict(user_data)
        user_data["id"]=user_id
        print(user_data)
        response = requests.patch(url, json=user_data)

        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code)
            raise ValueError("Problema na execução")
        
    
