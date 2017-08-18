from django.conf.urls import url, include
from . import views

urlpatterns = [
    #GETS
    url(r'^$', views.index,name="login_index"),
    url(r'^success$', views.success,name="login_success"),
    
    #POSTS
    url(r'^register$', views.register,name="login_register"),
    url(r'^login$', views.login,name="login_login")
]