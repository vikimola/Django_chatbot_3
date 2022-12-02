from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("register", views.register, name="register"),
    path("log_in", views.log_in, name="log_in"),
    path("log_out", views.log_out, name="log_out"),
    path("home", views.home, name="home"),
    # path("home_auth", views.home_auth, name="home_auth"),
    path("room_checker", views.room_checker, name="room_checker"),
    path("<str:room_name>/", views.room, name="room"),
    path("send", views.send, name="send"),
    path("getMessages/<str:room_name>/", views.getMessages, name="getMessages"),
    path("something", views.something, name="something"),

]