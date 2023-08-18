from django.urls import path
from . views import TodoView, CreateTodoView, DetailTodoView, DeleteTodoView, UpdateTodoView

urlpatterns =[
    path('', TodoView.as_view(), name='task'),
    path('task-create/', CreateTodoView.as_view(), name='task-create'),
    path('task/<int:pk>', DetailTodoView.as_view(), name='task_detail'),
    path('task/<int:pk>/update', UpdateTodoView.as_view(), name='task-update'),
    path('task/<int:pk>/delete', DeleteTodoView.as_view(), name='task-delete'),
]
    