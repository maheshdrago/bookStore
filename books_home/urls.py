from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout,name='logout'),
    path('book/<int:listing_id>',views.show_book,name='show_book'),
    path('<str:category>',views.byCategory,name='category'),
]