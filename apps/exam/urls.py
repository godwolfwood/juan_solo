from django.conf.urls import url, include
from . import views

urlpatterns = [
    #GETS
    url(r'^$', views.index,name="login_index"),
    url(r'^dashboard$', views.success,name="login_success"),
    url(r'^wish_items/create$', views.add,name="login_add"),
    url(r'^wish_items/(?P<number>\d+)$', views.show,name="login_show"),
    url(r'^wish_items/(?P<number>\d+)/remove$', views.remove,name="login_remove"),
    url(r'^wish_items/(?P<number>\d+)/delete$', views.delete,name="login_delete"),
    url(r'^wish_items/(?P<number>\d+)/add$', views.wish_add,name="login_wish_add"),
    
    #POSTS
    url(r'^register$', views.register,name="login_register"),
    url(r'^login$', views.login,name="login_login"),
    url(r'^wish_items/add$', views.create,name="login_create"),
]