from django.db import models

# Create your models here.


class Contact(models.Model):

    CATEGORY_CHOICES = (
        ('Друзья', 'Друзья'),
        ('Семья', 'Семья'),
        ('Работа', 'Работа'),
    )
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    address = models.CharField(max_length=100, verbose_name='Адрес проживания')
    email = models.CharField(max_length=100, verbose_name='Электронная почта')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    category = models.CharField(max_length=10, verbose_name='Категория контакта', choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Search(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.contact}"


