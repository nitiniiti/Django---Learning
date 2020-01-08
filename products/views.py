from django.shortcuts import render
from django.http import Http404
from .models import Product

from .forms import ProductForm

# Create your views here.


def product_create_view(request):
    initial_data = {
        'title': "My Title"
    }
    form = ProductForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, "product_detail.html", context)


def product_detail_view_with_id(request, id):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, "product_detail.html", context)


def all_product_detail_view(request):
    obj = Product.objects.all()
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'data_list': obj
    }
    return render(request, "all_products.html", context)
