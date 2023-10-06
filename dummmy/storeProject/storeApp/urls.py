from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.index,name="index"),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('form',views.form,name="form"),
    path('order',views.order,name='order')
]
