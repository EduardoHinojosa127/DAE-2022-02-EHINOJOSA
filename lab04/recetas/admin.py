from django.contrib import admin
from .models import Receta, Comentario, Autor
# Register your models here.
admin.site.register(Receta)
admin.site.register(Comentario)
admin.site.register(Autor)
