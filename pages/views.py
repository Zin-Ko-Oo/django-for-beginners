from django.views.generic import TemplateView

class homePageView(TemplateView):
    template_name = "pages/home.html"

class aboutPageView(TemplateView):
    template_name = "pages/about.html"