import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "JuegosMesa.settings")
django.setup()

from juegos.models import Categoria, Disenador, Juego, Resena
from decimal import Decimal
# Datos de ejemplo para las categorías      
categoria = [
    Categoria(nombre='Estrategia', descripcion='Juegos que requieren planificación y táctica.'),
    Categoria(nombre='Aventura', descripcion='Juegos que involucran exploración y descubrimiento.'),
    Categoria(nombre='Familiar', descripcion='Juegos adecuados para toda la familia.'),
    Categoria(nombre='Cartas', descripcion='Juegos que utilizan cartas como principal componente.'),
]
# Datos de ejemplo para los diseñadores
disenador = [
    Disenador(nombre='Reiner Knizia', fecha_nacimiento="1953-07-01", nacionalidad='Alemán'),
    Disenador(nombre='Klaus Teuber', fecha_nacimiento="1959-06-01", nacionalidad='Alemán'),
    Disenador(nombre='Elizabeth Hargrave', fecha_nacimiento="1985-02-01", nacionalidad='Americana'),
    Disenador(nombre='Uwe Rosenberg', fecha_nacimiento="1975-04-01", nacionalidad='Alemán'),
]
# Datos de ejemplo para los juegos  
juego = [
    Juego(nombre='Catán', descripcion='Un juego de estrategia donde los jugadores colonizan una isla.', fecha_lanzamiento="1995-07-01", precio=Decimal('49.99'), disenador=disenador[0], categoria=categoria[0], imagen='imagenes/catan.jpg'),
    Juego(nombre='Carcassonne', descripcion='Un juego de colocación de losetas donde los jugadores construyen un paisaje medieval.', fecha_lanzamiento="2014-07-01", precio=Decimal('39.99'), disenador=disenador[1], categoria=categoria[0], imagen='imagenes/carcassonne.jpg'),
    Juego(nombre='Wingspan', descripcion='Un juego de cartas sobre aves donde los jugadores crean su propio hábitat.', fecha_lanzamiento="1999-07-01", precio=Decimal('59.99'), disenador=disenador[2], categoria=categoria[2], imagen='imagenes/wingspan.jpg'),
    Juego(nombre='Agrícola', descripcion='Un juego de estrategia donde los jugadores gestionan una granja.', fecha_lanzamiento="2004-07-01", precio=Decimal('54.99'), disenador=disenador[3], categoria=categoria[0], imagen='imagenes/agricola.jpg'),
]
# Datos de ejemplo para las reseñas
resena = [
    Resena(juego=juego[0], calificacion=5, comentario='Un juego increíble, muy divertido y estratégico.'),
    Resena(juego=juego[1], calificacion=4, comentario='Un juego entretenido, pero puede volverse repetitivo.'),
    Resena(juego=juego[2], calificacion=5, comentario='Un juego hermoso y educativo sobre aves.'),
    Resena(juego=juego[3], calificacion=4, comentario='Un gran juego de gestión de recursos.'),
]

for categoria in categoria:
    categoria.save()
    print(f"Categoría {categoria.nombre} insertada correctamente.")
for disenador in disenador:
    disenador.save()
    print(f"Diseñador {disenador.nombre} insertado correctamente.")
for juego in juego:
    juego.save()
    print(f"Juego {juego.nombre} insertado correctamente.")
for resena in resena:   
    resena.save()
    print(f"Reseña para el juego {resena.juego.nombre} insertada correctamente.")
