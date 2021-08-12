from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.urls import reverse
from .models import Page
from .forms import PageForm

# Create your views here.
class PageListView(ListView):
    model = Page
    tempalte_name = 'diary/page_list.html'
    ordering = ['-dt_created']
    paginate_by = 8
    page_kwarg = 'page'
    

class PageDetailView(DetailView):
    model = Page
    template_name = 'diary/page_detail.html'
    pk_url_kwarg = 'page_id'


def info(request):
    return render(request, 'diary/info.html')    


class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    template_name = 'diary/page_form.html'

    def get_success_url(self):
        return reverse('page-detail', kwargs={'page_id':self.object.id})


class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'diary/page_form.html'
    pk_url_kwarg = 'page_id'

    def get_success_url(self):
        return reverse('page-detail', kwargs={'page_id':self.object.id})


def page_delete(request, page_id):
    object = get_object_or_404(Page, id=page_id)
    if request.method == 'POST':
        object.delete()
        return redirect('page-list')
    else:
        return render(request, 'diary/page_confirm_delete.html', {'object':object})


def index(request):
    return render(request, 'diary/index.html')