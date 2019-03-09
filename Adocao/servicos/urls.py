from django.urls import path
from .views import *

urlpatterns = [
    path('servicos/',PaginaServicoView.as_view(),name="servicos")
]
