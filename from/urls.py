from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginpage1,name="login"),
    
    path('logout/',views.logoutUser,name="Logout"),
    
    path('',views.home,name="home"),
    
    ##path('home_phone/<str:pk>',views.home_phone, name="home_phone"),
    
    path('contact/',views.player,name="contact"),
    
    path('add_player/',views.add_player,name="add_player"),
    
    path('update_player/<str:pk>',views.update_player, name="update_player"),
    

    
    path('delete_player/<player_id>',views.delete_player, name="delete_player"),
    
    path('user/',views.userPage, name="user-page"),
    
    
    
    
    path('passport/',views.passport,name="passport"),
    path('music/',views.music,name="music"),
    path('travel/',views.travel,name="travel"),
    path('national_anthem/',views.national_anthem,name="national_anthem"),
    path('add_pass/',views.add_pass,name="add_pass"),
    path('add_anthem/',views.add_anthem,name="add_anthem"),
    path('add_music/',views.add_music,name="add_music"),
    path('add_travel/',views.add_travel,name="add_travel"),
]
