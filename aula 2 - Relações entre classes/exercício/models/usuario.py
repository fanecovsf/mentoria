class Usuario:
    nome:str
    email:str
    posts:list

    def __init__(self, nome:str, email:str):
        self.nome = nome
        self.email = email
        self.posts = []

    def __str__(self):
        return f'Nome: {self.nome}, Email: {self.email}'


    def add_post(self, post):
        self.posts.append(post)