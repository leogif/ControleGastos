from django.contrib import admin
from .models import Categoria, Transacaoes

# Registrando nossa aplicação no site do Admin
admin.site.register(Categoria)
admin.site.register(Transacaoes)
