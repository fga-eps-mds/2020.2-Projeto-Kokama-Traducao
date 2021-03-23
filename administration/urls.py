from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^admin_register/$', views.admin_register, name='admin_register'),
    url(r'^login/$', views.login, name='login'),

]