from django.urls import path
from . import views_html

urlpatterns = [
    path('adicionar_palavra/', views_html.add_translate, name='add_translate'),
    path('lista_de_palavras/', views_html.list_translation, name= 'list_translation'),
]  