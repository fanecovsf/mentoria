from models.usuario import Usuario

from datetime import datetime

class Post:
    titulo:str
    data:datetime
    responsavel:Usuario
    comentarios:list

    def __init__(self, titulo:str, data:datetime, responsavel:Usuario):
        self.titulo = titulo
        self.data = data

        self.responsavel = responsavel
        self.responsavel.add_post(self)

        self.comentarios = []

    def __str__(self):
        return f'Título: {self.titulo}, Data/Hora do post: {self.data}'


    def add_comentario(self, comentario):
        self.comentarios.append(comentario)
    