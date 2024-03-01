from django.shortcuts import render, redirect

from .forms import TaskForm
from . models import Task
# Create your views here.
# def home(request):
#     # return render(request,'home.html');
#     if request.method=="POST":
#         name=request.POST.get('name')
#         priority=request.POST.get('priority')
#         description=request.POST.get('description')
#         obj=Task(name=name,priority=priority,description=description)
#         obj.save()
#     return render(request,"index.html")

def task_add(request):
    form = TaskForm()
    # print(form)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_view')
    return render(request,'task_add.html',{'form':form})

def task_view(request):
    taskdetails = Task.objects.all()
    return render(request, "task_view.html", {'taskdetails': taskdetails})
def task_delete(request,dl):
    taskdelete=Task.objects.get(id=dl)
    taskdelete.delete()
    return redirect("task_view")

def task_update(request,up):
    taskupdate=Task.objects.get(id=up)
    updateForm=TaskForm(instance=taskupdate)
    if request.method == 'POST':
        updateForm=TaskForm(request.POST,instance=taskupdate)
        if updateForm.is_valid():
            updateForm.save()
            return redirect("task_view")
    return render(request, "task_update.html",{'updateform':updateForm})
