from django.shortcuts import get_object_or_404, render

from .models import Exhibit

def index(request):
    exhibit_list = Exhibit.objects.all()
    context = {'exhibit_list': exhibit_list}
    return render(request, 'api/index.html', context)

def detail(request, exhibit_id):    
    exhibit = get_object_or_404(Exhibit, pk=exhibit_id)
    return render(request, 'api/detail.html', {'exhibit': exhibit})