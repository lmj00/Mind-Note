from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Page
from .forms import PageForm

# Create your views here.
def page_list(request):
    object_list = Page.objects.all()
    paginator = Paginator(object_list, 8)
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    page_object = paginator.page(page_number)
    return render(request, 'diary/page_list.html', {'page':page_object})


def page_detail(request, page_id):
    object = get_object_or_404(Page, id=page_id)
    return render(request, 'diary/page_detail.html', {'object':object})


def info(request):
    return render(request, 'diary/info.html')    


def page_create(request):
    if request.method == 'POST':
        page_form = PageForm(request.POST)
        if page_form.is_valid():
            new_page = page_form.save()
            return redirect('page-detail', page_id=new_page.id) 
    else:
        page_form = PageForm()
    return render(request, 'diary/page_form.html', {'form':page_form}) 


def page_update(request, page_id):
    object = get_object_or_404(Page, id=page_id)
    if request.method == 'POST':
        page_form = PageForm(request.POST, instance=object)
        if page_form.is_valid():
            page_form.save()
            return redirect('page-detail', page_id=page_id)
    else:
        page_form = PageForm(instance=object)
    return render(request, 'diary/page_form.html', {'form':page_form})


def page_delete(request, page_id):
    object = get_object_or_404(Page, id=page_id)
    if request.method == 'POST':
        object.delete()
        return redirect('page-list')
    else:
        return render(request, 'diary/page_confirm_delete.html', {'object':object})


def index(request):
    return render(request, 'diary/index.html')