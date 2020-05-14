from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    context = {
        "dojos": Dojo.objects.all(),
    }   
    return render(request, 'index.html', context)

def dojo_form(request):
    return render(request, 'dojo_form.html')

def create_dojo(request):
    stack_type = request.POST["stack_type"]
    location = request.POST["location"]
    Dojo.objects.create(
        stack_type=stack_type,
        location=location
    )
    return redirect('/')

def ninja_form(request):
    context = {
        "dojos": Dojo.objects.all(),
    }
    return render(request, 'ninja_form.html', context)

def create_ninja(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    dojo = request.POST["dojo_id"]
    Ninja.objects.create(
        first_name=first_name,
        last_name=last_name,
        dojo=Dojo.objects.get(id=dojo)
    )
    return redirect('/')
