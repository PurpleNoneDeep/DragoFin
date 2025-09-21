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

def auth(request):
    return render(request, 'main/authorization.html')

def statistics(request):
    return render(request, 'main/statistics.html')

def addTransaction(request):
    return render(request, 'main/addTransaction.html')

def addCategory(request):
    return render(request, 'main/addCategory.html')