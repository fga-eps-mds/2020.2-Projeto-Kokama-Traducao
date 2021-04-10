from django.urls import path
from . import views_html

urlpatterns = [
    path('adicionar_palavra/', views_html.add_word, name='add_translate'),
    path('lista_de_palavras/', views_html.list_words, name= 'list_translation'),
    path('lista_de_palavras/<int:id>/', views_html.view_word, name="view-word"),
    path('lista_de_palavras/<int:id>/editar/<field>', views_html.edit_word, name="edit-word"),
    path('lista_de_palavras/<int:id>/delete/', views_html.del_word, name="del-word"),
    path('lista_de_palavras/<int:id>/editar/', views_html.update_word, name="update-word"),
]  