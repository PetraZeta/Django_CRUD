"""
La plantilla index.html debe mostrar una o varias imágenes relacionadas con
el tema que nos ocupa.
juegos_list.html debe mostrar la lista de juegos en una tabla. Cada juego
incluirá las opciones Ver detalles y Eliminar que llevarán a las plantillas
detalles_juego.html y eliminar_juego.html respectivamente.
nuevo_juego.html se utilizará para dar de alta un nuevo juego en la base de
datos.
detalles_juego.html. Mostrará toda la información relacionada con el juego,
su categoría y datos de su creador. Además de todas las reseñas del mismo.
"""
from juegos import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexViews.as_view(), name='index'), # 127.0.0.1:8000/
    path('list/', views.JuegoListView.as_view(), name='juegos_list'), # 127.0.0.1:8000/list/
    path('nuevo/juego', views.JuegoCreateView.as_view(), name='nuevo_juego'), # 127.0.0.8000/nuevo/juego
    path('detalle/<int:pk>', views.JuegoDetailView.as_view(), name='detalles_juego'), # 127.0.0.8000/detalle/juego
    path('eliminar/<int:pk>', views.JuegoDeleteView.as_view(), name='eliminar_juego'), # 127.0.0.8000/eliminar/juego
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)