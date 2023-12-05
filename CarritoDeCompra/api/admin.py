from django.contrib import admin
from .models import Gorras,Camiseta
# Register your models here.



admin.site.register([Camiseta,
                     Gorras,
                     ])