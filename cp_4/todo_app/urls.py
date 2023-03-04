from django.urls import path
from .views import get_todo_lists, create_todo_list, get_todo_list, \
    update_todo_list, delete_todo_list, get_todo_list_todos, \
    create_todo_list_todo, get_todo_list, create_todo, get_todo_detail, \
    update_todo_detail, delete_todo_detail, todo_list_view, todo_list_detail

urlpatterns = [
    path('api/todo-lists/', get_todo_lists),
    path('api/todo-lists/create', create_todo_list),
    path('api/todo-lists/<int:id>/', get_todo_list),
    path('api/todo-lists/put/<int:pk>/', update_todo_list),
    path('api/todo-lists/delete/<int:pk>/', delete_todo_list),
    path('api/todo-lists/<int:pk>/todos/', get_todo_list_todos),
    path('api/todo-lists/<int:pk>/create/todos/', create_todo_list_todo),
    path('api/todos/', get_todo_list),
    path('api/create/todos/', create_todo),
    path('api/todos/<int:pk>/', get_todo_detail),
    path('api/todos/put/<int:pk>/', update_todo_detail),
    path('api/todos/delete/<int:pk>/', delete_todo_detail),
    path('todo-lists/', todo_list_view),
    path('todo-lists/<int:id>/', todo_list_detail),
]