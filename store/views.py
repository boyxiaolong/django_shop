from django.shortcuts import render, HttpResponseRedirect
from .models import Product,Category
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from .forms import SearchForm
# Create your views here.

def index(request):
    clo_list = Product.objects.all()
    clo_list = get_page(request, clo_list)
    categories = Category.objects.filter(parent=None)
    search_form = SearchForm()
    return render(request, "index.html", locals())

def get_page(request, clo_list):
    paginator = Paginator(clo_list, 4)
    try:
        page = int(request.GET.get('page', 1))
        clo_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        clo_list = paginator.page(1)
    return clo_list

def product_detail(request, id):
    try:
        clo = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return render(request, 'error.html', {'error':"商品不存在"})

    return render(request, 'single_product.html', locals())

def category(request, id):
    try:
        cat = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return render(request, 'error.html', {'error':'category not exit'})

    print(cat)
    clo_list = Product.active_objects.filter(categories=cat)
    clo_list = get_page(request, clo_list)
    categories = Category.objects.filter(parent=None)
    return render(request, 'index.html', locals())

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            clo_list = Product.objects.filter(name__contains=content)
            clo_list = get_page(request, clo_list)
            categories = Category.objects.filter(parent=None)
            search_form = SearchForm()
            return render(request, "index.html", locals())
    return HttpResponseRedirect('/')