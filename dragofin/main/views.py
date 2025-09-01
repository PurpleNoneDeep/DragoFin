from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/index.html')

def dashboard(request):
    return render(request, 'main/dashboard.html')

def income(request):
    return render(request, 'main/income.html')

def expences(request):
    return render(request, 'main/expences.html')