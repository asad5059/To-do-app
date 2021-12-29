from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path
from app.views import home,login, signup,add_todo,signout,delete_todo,change_todo,about

urlpatterns = [
    path('',home,name="home"),
    path('login/',login,name='login'),
    path('signup/',signup),
    path('add-todo/',add_todo),
    path('logout/',signout),
    path('about/',about),
    path('delete-todo/<int:id>',delete_todo),
    path('change-status/<int:id>/<str:status>',change_todo),

]
