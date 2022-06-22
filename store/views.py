from django.shortcuts import render

# Create your views here.

def home(request):
    diction ={}
    return render(request,'index-2.html',context=diction)
