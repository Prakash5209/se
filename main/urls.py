from django.urls import path

from main import views


app_name = 'main'
urlpatterns = [
    path('',views.home,name='home'),
    path('deletepost/<int:pk>/',views.deletepost,name='deletepost'),
]