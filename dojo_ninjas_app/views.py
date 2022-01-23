from django.shortcuts import render,redirect
from .models import Dojo,Ninja

def home(request):
    context={
        "all_the_dojos":Dojo.objects.all(),
        "all_the_ninjas":Ninja.objects.all()
    }
    return render(request, 'index.html',context)
# Create your views here.
def new_dojo(request):
    if request.method=="POST":
        Dojo.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state'],
        )
    return redirect('/')

def new_ninja(request):
    if request.method=="POST":
        Ninja.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        #=request.POST['dojo'] need to figure out how to create the dojo attribute for Ninja
        dojo=Dojo.objects.get(name=request.POST['dojo'])
        )
    return redirect('/')