from django.contrib import admin
from.models import Articulo,Comentario

class ComentarioEnLinea(admin.TabularInline):
    model=Comentario
    extra = 0

#se hace como un join entre artculos y artucs admin
class ArticuloAdmin(admin.ModelAdmin):
    inlines=[
        ComentarioEnLinea,

    ]
# Register your models here.

admin.site.register(Articulo,ArticuloAdmin)
admin.site.register(Comentario)
