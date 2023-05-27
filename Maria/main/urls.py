from django.contrib import admin
from django.urls import path
from locadora.views import index_view, locacoes_view, filmes_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index_view, name='index'),
    path('lista_locacao/', locacoes_view, name='locacao'),
    path('lista_filmes/', filmes_view, name='filmes')
]
