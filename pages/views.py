from django.shortcuts import render

from django.http import HttpResponse

def homepageview(request):
    return HttpResponse("<h3>nice try</h3>")

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class aboutpageview(TemplateView):
    template_name = 'about.html'

class projectapageview(TemplateView):
    template_name = 'projecta.html'

class projectbpageview(TemplateView):
    template_name = 'projectb.html'

class projectcpageview(TemplateView):
    template_name = 'projectc.html'