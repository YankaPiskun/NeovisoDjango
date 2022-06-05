from django.db import models
from django.contrib.auth.models import AbstractUser

'''
Customer (
Name, Email, Phone, Address, Birthdate, slug
)
Car (
owner, manufacturer, model, yearOfManufacture, slug
)
Order (
car, user (employee), date, amount, status,slug
)
Employee (
name, lastname, profession,
)
'''
class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_reception = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class Reception(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ресепшен'
        verbose_name_plural = 'Ресепшен'


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    profession = models.CharField(max_length=255, verbose_name='Профессия')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Customer(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='Имя')
    email = models.EmailField(default='noone@email.com', verbose_name='Почта')
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name='Телефон')
    address = models.CharField(max_length=255, default='', verbose_name='Адрес')
    birthdate = models.DateField(default='1975-12-12', verbose_name='Дата рождения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'


class Car(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, default='', verbose_name='владелец')
    manufacturer = models.CharField(max_length=255, default='', verbose_name='производитель')
    model = models.CharField(max_length=255, default='', verbose_name='модель')
    yearOfManufacture = models.DateField(default='2000', verbose_name='дата выпуска')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class Order(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Машина')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Сотрудник')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    amount = models.CharField(max_length=255, verbose_name='сумма')
    status = models.CharField(max_length=255, verbose_name='статус')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'





# Create your models here.
