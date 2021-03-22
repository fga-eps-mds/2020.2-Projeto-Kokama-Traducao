from django.urls import path
from . import views_html


urlpatterns = [
    path('adicionar_palavra/', views_html.add_translate ),
]   