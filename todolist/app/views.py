from django.shortcuts import render
from .models import Task
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from django.template import loader

# Create your views here.
def index(request):
    # template = loader.get_template("app/index.html")
    db_data = Task.objects.all()
    context = {
        "db_data": db_data[::-1],
        "update": None
    }
    # return HttpResponse(template.render(context, request))
    return render(request, "app/index.html", context)


def insert(request):
    try:
        task_subject = request.POST["subject"]
        task_description = request.POST["description"]
        if task_subject == "" or task_description == "":
            raise ValueError("No ha ingresado informacion.")
        db_data = Task(subject=task_subject, description=task_description)
        db_data.save()
        return HttpResponseRedirect(reverse("index")) 
    except ValueError as err:
        print(err)
        return HttpResponseRedirect(reverse("index")) 


def update(request):
    task_id = request.POST["id"]
    task_subject = request.POST["subject"]
    task_description = request.POST["description"]
    db_data = Task.objects.get(pk=task_id)
    db_data.subject = task_subject
    db_data.description = task_description
    db_data.save()
    return HttpResponseRedirect(reverse("index")) 


def update_form(request, task_id):
    db_data = Task.objects.all()
    db_data_only = Task.objects.get(pk=task_id)
    print(db_data_only)
    context = {
        "db_data": db_data[::-1],
        "update": db_data_only
    }
    return render(request, "app/index.html", context)


def delete(request, task_id):
    db_data = Task.objects.filter(id=task_id)
    db_data.delete()
    return HttpResponseRedirect(reverse("index")) 
