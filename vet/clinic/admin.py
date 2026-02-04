from django.contrib import admin
from .models import Gender, PetType, PetPatient, Owner


admin.site.register(Gender)
admin.site.register(PetType)
admin.site.register(PetPatient)
admin.site.register(Owner)