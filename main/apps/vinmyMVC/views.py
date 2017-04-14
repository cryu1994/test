from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "vinmymvc/index.html")

def show(request):
    
    return render(request, "vinmymvc/show_users.html")
