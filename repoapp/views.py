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

def aboutprofile(request):
    return render(request, 'about1.html')

def heytanish(request):
    return render(request, 'hey.html')

def adminpage(request):
    return render(request, 'about.html')