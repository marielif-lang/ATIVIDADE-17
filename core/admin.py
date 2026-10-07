from django.contrib import admin
from .models import Categoria, Aluno, PerfilAcademico, Projeto

admin.site.register(Categoria)
admin.site.register(Aluno)
admin.site.register(PerfilAcademico)
admin.site.register(Projeto)