"""translate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers
from dictionary.views import KokamaViewSet, PhrasesViewSet, WordListViewSet, add_translate
from .views import login

router = routers.DefaultRouter()
router.register(r'dicionario', KokamaViewSet, basename="dictionary")
router.register(r'frases', PhrasesViewSet, basename="phrases")
router.register(r'lista_de_palavras', WordListViewSet, basename="wordlist")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    url(r'^traducao/adicionar_traducao/(?P<id>[0-9]*)$', add_translate, name="add_translate"),
    path('traducao/', include(router.urls)),
    path('', include(router.urls)),
]
