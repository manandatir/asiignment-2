from django.shortcuts import render,HttpResponse
from .models import Student
from datetime import datetime
# Create your views here.
def index(request):
    # return HttpResponse("Hello this a home page ",  datetime.now())
# def STUDENT(request):
    obj=Student.objects.all()
    context={
        "obj":obj,
    }
    return render(request, "index.html",context)