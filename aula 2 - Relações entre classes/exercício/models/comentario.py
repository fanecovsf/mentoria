from models.post import Post

class Comentario:
    post:Post
    comentario:str

    def __init__(self, post:Post, comentario:str):
        self.post = post
        self.post.add_comentario(self)

        self.comentario = comentario

    def __str__(self):
        return str(self.comentario)