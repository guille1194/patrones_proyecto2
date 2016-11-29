from django.contrib import admin
from .models import Usuario, Pregunta, Opcion_Pregunta, Respuesta, Respuesta_Opcion, Categoria
# Register your models here.

admin.site.register(Pregunta)
admin.site.register(Opcion_Pregunta)
admin.site.register(Usuario)
admin.site.register(Respuesta)
admin.site.register(Categoria)
admin.site.register(Respuesta_Opcion)
