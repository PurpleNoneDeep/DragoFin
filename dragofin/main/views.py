from django.shortcuts import render
from .models import User, Transaction
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/index.html')

def dashboard(request):
    print(request.user)
    transactions = Transaction.objects.all()
    users = User.objects.all()
    user = users.first()
    return render(request, 'main/dashboard.html', {'transactions': transactions, 'users': users, 'user': user})

def income(request):
    return render(request, 'main/income.html')

def expences(request):
    return render(request, 'main/expences.html')

def auth(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('dashboard')
    return render(request, 'main/authorization.html')

def statistics(request):
    return render(request, 'main/statistics.html')

def addTransaction(request):
    return render(request, 'main/addTransaction.html')

def addCategory(request):
    return render(request, 'main/addCategory.html')

def Calendar(request):
    return render(request, 'main/Calendar.html')