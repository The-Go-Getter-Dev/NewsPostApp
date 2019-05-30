from django.views.generic import TemplateView

class Myhello(TemplateView):
    template_name='hello.html'