from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Owner, PetPatient

class OwnerRegistrationForm(UserCreationForm):
    class Meta:
        model = Owner
        fields = [
            'phone_number',
            'surname',
            'name',
            'patronymic',
            'password1',
            'password2',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].label = "Номер телефона"
        self.fields['surname'].label = "Фамилия"
        self.fields['name'].label = "Имя"
        self.fields['patronymic'].label = "Отчество (не обязательно)"
        self.fields['password1'].label = "Пароль"
        self.fields['password2'].label = "Подтверждение пароля"
        self.fields['phone_number'].widget.attrs.update({'placeholder': '+7 (XXX) XXX-XX-XX'})
        self.fields['surname'].widget.attrs.update({'placeholder': 'Иванов'})
        self.fields['name'].widget.attrs.update({'placeholder': 'Иван'})
        self.fields['patronymic'].widget.attrs.update({'placeholder': 'Иванович'})

class PetPatientCreateForm(forms.ModelForm):
    class Meta:
        model = PetPatient
        fields = ['name', 'type', 'breed', 'gender', 'birth_date', 'color', 'is_sterilized', 'microchip_number',
                  'tattoo_number', 'vet_passport', 'alive']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Кличка"
        self.fields['breed'].label = "Порода"
        self.fields['color'].label = "Окрас"
        self.fields['type'].label = "Вид животного"
        self.fields['gender'].label = "Пол животного"
        self.fields['birth_date'].label = "Дата рождения животного"
        self.fields['is_sterilized'].label = "Животное стерелизовано?"
        self.fields['vet_passport'].label = "Есть ветеринарный паспорт?"
        self.fields['microchip_number'].label = "Номер микрочипа(если есть)"
        self.fields['tattoo_number'].label = "Номер клейма(если есть)"
        self.fields['alive'].label = "Животное живое?"


