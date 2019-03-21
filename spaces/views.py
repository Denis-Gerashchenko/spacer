from django.views import View
from django.shortcuts import render
from .models import Space

# Create your views here.
class Index_view(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        spaces = Space.objects.all()
        context = {
            'spaces': spaces
        }
        return render(request, self.template_name, context)

def space_view(request):
    return render(request, 'single-post-1.html', {})

