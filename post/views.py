from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from . forms import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        task = Task(title=title, description=description)
        task.save()


    tasks = Task.objects.order_by('-created')
    form = TaskForm()
    

    context = {
        'tasks':tasks,
    }
    return render(request, 'post/tasks.html', context)