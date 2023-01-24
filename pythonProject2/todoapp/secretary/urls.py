from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', TodoList.as_view(), name='home'),
    path('executor/<int:executor_id>/', TodoExecutor.as_view(), name='executor'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('secretary/add_todo/', CreateTodo.as_view(), name='add_todo')
]
