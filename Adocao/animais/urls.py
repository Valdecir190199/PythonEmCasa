from django.urls import path
from .views import *

urlpatterns = [
	path('inicio/',PaginaInicialView.as_view(), name="index"),
	path('sobre/',PaginaSobreView.as_view(), name="sobre"),
	path('portfolio/',PaginaPortfolioView.as_view(), name="portfolio"),

]
