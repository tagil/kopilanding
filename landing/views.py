from django.shortcuts import render
from django.views.generic import View, TemplateView
from landing.models import Page

class LandingView(TemplateView):

    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)
        context['page_obj'] = Page.objects.all().order_by("?").first()
        return context
