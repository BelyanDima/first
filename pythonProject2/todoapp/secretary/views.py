from datetime import date

from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import ToDo, Executor
from .forms import ToDoForm, UserRegisterForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')

    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'secretary/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'secretary/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')


class TodoList(ListView):
    model = ToDo
    template_name = 'secretary/home_todo_list.html'
    context_object_name = 'todo'
    # extra_context = {'title': 'Главная'}
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs, is_complete=False)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return ToDo.objects.filter(is_complete=False).select_related('executor')




class TodoList_is_compete(ListView):
    model = ToDo
    template_name = 'secretary/is_complete_todo.html'
    context_object_name = 'todo'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs, is_complete=True)
        context['title'] = 'Завершённые задачи'
        return context

    def get_queryset(self):
        return ToDo.objects.filter(is_complete=True).select_related('executor')


class TodoExecutor(ListView):
    model = ToDo
    template_name = 'secretary/home_todo_list/html'
    context_object_name = 'todo'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Executor.objects.get(pk=self.kwargs['executor_id'])
        return context

    def get_queryset(self):
        return ToDo.objects.filter(executor_id=self.kwargs['executor_id'], is_complete=False).select_related('executor')


class CreateTodo(CreateView):
    form_class = ToDoForm
    template_name = 'secretary/add_todo.html'
    success_url = reverse_lazy('home')


def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('home')


def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('home')


