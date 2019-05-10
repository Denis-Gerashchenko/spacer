from django.views.generic import View, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Space

# Create your views here.
class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        spaces = Space.objects.all()
        context = {
            'spaces': spaces
        }
        return render(request, self.template_name, context)

class SpaceDetailView(DetailView):
    model = Space
    template_name = 'single-post-1.html'
    context_object_name = 'space'

    def get_object(self):
        obj = super().get_object()
        return obj


