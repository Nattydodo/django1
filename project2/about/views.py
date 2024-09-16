from django.http import HttpResponse
from django.template import loader
from .models import About

def about(request):
  mymembers = About.objects.all().values()
  template = loader.get_template('aboutTem.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))