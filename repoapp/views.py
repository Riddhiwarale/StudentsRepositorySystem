from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def profile(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def forget(request):
    return render(request, 'forgetpass.html')
