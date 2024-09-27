from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

def index(request):
    if request.method == 'POST':
        task_title = request.POST.get('task')
        new_task = Task(title=task_title)
        new_task.save()
        return redirect('tasks:index')
    
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks:index')

