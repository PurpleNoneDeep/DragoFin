from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    CATEGORY_TYPE_CHOICES = (
        ('income', 'Доход'),
        ('expense', 'Расход'),
    )

    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=7, choices=CATEGORY_TYPE_CHOICES)
    is_default = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Transaction {self.transaction_id} by {self.user.name}'

class Setting(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    value = models.TextField()

    def __str__(self):
        return f'Setting {self.key} for {self.user.name}'

class Analytics(models.Model):
    analytics_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    period = models.DateField()
    income_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    expense_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'Analytics for {self.user.name} - {self.period.strftime("%m/%Y")}'

class DragonState(models.Model):
    MOOD_CHOICES = (
        ('happy', 'Счастливый'),
        ('neutral', 'Нейтральный'),
        ('sad', 'Грустный'),
        ('sleeping', 'Спящий'),
    )

    dragon_state_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=8, choices=MOOD_CHOICES)
    last_updated = models.DateTimeField(auto_now=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'DragonState for {self.user.name} - Mood: {self.mood}'