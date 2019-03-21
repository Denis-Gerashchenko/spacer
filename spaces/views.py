from django.views import generic
from .models import Space

# Create your views here.
class Index_view(generic.DetailView):
    template_name = 'index.html'
    context_object_name = 'all_spaces'

    def get_queryset(self):
        return Space.objects.all()

def space_view(request):
    return render(request, 'single-post-1.html', {})

