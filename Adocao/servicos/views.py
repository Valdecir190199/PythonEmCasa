from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.

class PaginaServicoView(TemplateView):
    template_name="servicos.html"
