from models.usuario import Usuario
from models.post import Post
from models.comentario import Comentario

from datetime import datetime

#Instanciando usuários
usuario1 = Usuario('Gustavo', 'gustavo@gmail.com')
usuario2 = Usuario('Luciano', 'luciano@gmail.com')

#Instanciando posts
post1 = Post('Primeiro post do Gustavo', datetime.now(), usuario1)
post2 = Post('Segundo post do Gustavo', datetime.now(), usuario1)
post3 = Post('Primeiro post do Luciano', datetime.now(), usuario2)

#Instanciando comentários
com1 = Comentario(post1, 'Comentário 1 do post1')
com2 = Comentario(post1, 'Comentario 2 do post1')
com3 = Comentario(post2, 'Comentario 1 do post2')
com4 = Comentario(post2, 'Comentario 2 do post2')
com5 = Comentario(post3, 'Comentario 1 do post3')
com6 = Comentario(post3, 'Comentario 2 do post3')

#Testando usuários
print('Usuários:')
print(usuario1)
print(usuario2)
print('')

#Testando posts
print('Posts:')

for post in usuario1.posts:
    print(post)
    print('\nComentários:')
    for comentario in post.comentarios:
        print(comentario)

print('')

for post in usuario2.posts:
    print(post)
    print('\nComentários:')
    for comentario in post.comentarios:
        print(comentario)