from django.shortcuts import render
from django.views.generic import TemplateView
from apps.products.models import Product, Category


class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_products'] = Product.objects.filter(is_featured=True)[:8]
        context['categories'] = Category.objects.all()[:6]
        return context


class AboutView(TemplateView):
    template_name = 'core/about.html'


class ContactView(TemplateView):
    template_name = 'core/contact.html'