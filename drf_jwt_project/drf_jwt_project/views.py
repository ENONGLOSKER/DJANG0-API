from django.shortcuts import render


# Create your views here.
def register_page(request):
    return render(request, 'register.html')

def login_page(request):
    return render(request, 'login.html')

def user_list_page(request):
    return render(request, 'index.html')
