from . import views
from django.urls import path
app_name='shop'
urlpatterns = [

    path('',views.home,name='home'),
    path('register',views.Reg,name='register'),
    path('login',views.login,name="login"),
    path('logout',views.logout,name='logout'),
    path("forms", views.index, name="forms"),
    path("load/",views.load,name='load')
]
