from django.db import models
from django.contrib.auth.models import AbstractUser


class Gender(models.Model):
    gender = models.CharField(max_length=50, verbose_name="Пол")

    class Meta:
        verbose_name = "Пол"
        verbose_name_plural = "Полы"

    def __str__(self):
        return self.gender


class PetType(models.Model):
    type = models.CharField(max_length=300, verbose_name="Вид животного")

    class Meta:
        verbose_name = "Вид животного"
        verbose_name_plural = "Виды животных"

    def __str__(self):
        return self.type


class Owner(AbstractUser):
    surname = models.CharField(max_length=150, verbose_name="Фамилия")
    name = models.CharField(max_length=150, verbose_name="Имя")
    patronymic = models.CharField(max_length=150, blank=True, null=True, verbose_name="Отчество")
    phone_number = models.CharField(max_length=30, unique=True, verbose_name="Номер телефона")
    passport_data = models.CharField(max_length=100, blank=True, null=True, verbose_name="Паспортные данные")
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Пол владельца")

    def save(self, *args, **kwargs):
        if self.phone_number and (not self.username or self.username != self.phone_number):
            self.username = self.phone_number
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.surname} {self.name}" + (f"{self.patronymic or ''}".strip())

    class Meta:
        verbose_name = "Владелец"
        verbose_name_plural = "Владельцы"


class PetPatient(models.Model):
    name = models.CharField(max_length=150, verbose_name="Кличка")
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="pets", verbose_name="Владелец")
    type = models.ForeignKey(PetType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Вид")
    breed = models.CharField(max_length=100, blank=True, verbose_name="Порода")
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Пол")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    color = models.CharField(max_length=100, blank=True, verbose_name="Окрас")
    is_sterilized = models.BooleanField(default=False, verbose_name="Стерилизован/кастрирован")
    microchip_number = models.CharField(max_length=50, blank=True, verbose_name="Номер микрочипа")
    tattoo_number = models.CharField(max_length=50, blank=True, verbose_name="Номер татуировки")
    vet_passport = models.BooleanField(default=False, verbose_name="Ветпаспорт")
    alive = models.BooleanField(default=True, verbose_name="Жив")

    def __str__(self):
        return f"{self.name} — {self.owner}"
