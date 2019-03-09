from django.shortcuts import render
#importando a classe genérica para exibir
#uma pagina simples

from django.views.generic import TemplateView

# Create your views here.

class PaginaInicialView(TemplateView):
    template_name="index.html"

class PaginaSobreView(TemplateView):
    template_name="sobre.html"

class PaginaPortfolioView(TemplateView):
    template_name="portfolio.html"
