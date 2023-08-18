from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView,DetailView
from .models import Task
from django.urls import reverse_lazy
# Create your views here.
class TodoView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name='todo_list/task.html'
    

class CreateTodoView(CreateView):
    model = Task
    context_object_name = 'task'
    fields = ["user", "title", "description"]
    template_name='todo_list/create_task.html'
    
class DetailTodoView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name='todo_list/task_detail.html'
 
 
class UpdateTodoView(UpdateView):
    model = Task
    fields= ['title', 'description']
    context_object_name = 'task_update'
    template_name='todo_list/task_update.html'   
    
class DeleteTodoView(DeleteView):
    model = Task
    context_object_name = "post-delete"
    success_url = reverse_lazy("task")
    template_name='todo_list/task_delete.html'
    