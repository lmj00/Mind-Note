from django.shortcuts import render
from .models import Page

# Create your views here.
def page_list(request):
    lists = Page.objects.all()
    return render(request, 'diary/page_list.html', {'lists':lists})

def page_detail(request, page_id):
    data = Page.objects.get(id=page_id)
    return render(request, 'diary/page_detail.html', {'data':data})

    
