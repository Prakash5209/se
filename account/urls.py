from django.urls import path

from account import views

app_name = 'account'
urlpatterns = [
    path('',views.userLogin,name='userLogin'),
    path('signup/',views.userSignup,name='userSignup'),
    path('signout/',views.userLogout,name='userLogout'),
    # path('profile/',views.userProfile,name='userProfile'),
    path('profile/<int:pk>/',views.userProfile,name='userProfile'),
]