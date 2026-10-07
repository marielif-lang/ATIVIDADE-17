from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.lista_projetos, name='lista_projetos'),
    path('projeto/<int:id>/', views.detalhe_projeto, name='detalhe_projeto'),
]