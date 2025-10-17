from django.shortcuts import render, get_object_or_404
from .models import User, Transaction, Category
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/index.html')

def dashboard(request):
    print(request.user)
    query = request.GET.get('category')
    transactions = Transaction.objects.all()
    categories = Category.objects.all()
    users = User.objects.all()
    user = users.first()
    if query:
        transactions = transactions.filter(category__name__icontains=query)
    return render(request, 'main/dashboard.html', {'transactions': transactions, 'users': users, 'user': user, 'query': query})

def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, transaction_id=transaction_id)
    transaction.delete()
    return redirect('dashboard')

def add_transaction(request):
    categories = Category.objects.all().values('name', 'type')  # Получаем все категории

    if request.method == 'POST':
        date = request.POST.get('date')
        transaction_type = request.POST.get('type')
        category_name = request.POST.get('custom_category') if request.POST.get('category') == 'custom' else request.POST.get('category')
        amount = request.POST.get('amount')
        description = request.POST.get('description')

        # Проверка, если выбрана новая категория
        if request.POST.get('category') == 'custom' and category_name:
            # Создаем новую категорию с указанным именем и типом
            category, created = Category.objects.get_or_create(name=category_name, type=transaction_type)
        else:
            # Убедитесь, что категория выбрана из выпадающего списка
            category_id = request.POST.get('category')
            if category_id:
                category, created = Category.objects.get_or_create(name=category_id, type=transaction_type)
            else:
                # Обработка ошибки: категория не выбрана
                return render(request, 'add_transaction.html', {
                    'categories': categories,
                    'error': 'Пожалуйста, выберите категорию.'
                })
        first_user = User.objects.first()
        # Сохраняем транзакцию
        transaction = Transaction(
            user=first_user,
            date=date,
            category=category,  # Используем категорию, которую мы получили или создали
            amount=amount,
            comment=description,
             # Автоматически добавляем текущего пользователя
        )
        transaction.save()

        return redirect('dashboard')

    return render(request, 'add_transaction.html', {'categories': categories})

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