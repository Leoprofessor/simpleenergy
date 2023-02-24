from django.urls import path
from . import views


urlpatterns = [

    path('leitor', views.leitor, name="leitor"),
    path('encontrar_codigo', views.encontrar_codigo, name="encontrar_codigo"),
    path('gerar_ia/<int:id>/', views.gerar_ia, name="gerar_ia"),
    path('hash/', views.hash, name="hash"),


]