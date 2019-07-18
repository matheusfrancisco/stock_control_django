from django.urls import path
from project.stock import views as v

app_name = 'stock'

urlpatterns=[
    path('',v.estoque_entrada_list, name="estoque_entrada_list"),
]
