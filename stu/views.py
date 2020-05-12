from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from stu.models import *
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def index(request):
    if request.POST:
        p=Person(name=request.POST['name'],age=request.POST['age'],birthday=request.POST['birthday'])
        p.save()
    #return getdata(request)
    return render(request, 'index.html', {'list':getdata(request)})

def getdata(request):
    list=Person.objects.all()
    print(list)
    return list
    #return render(request, 'index.html',{'list':list})
