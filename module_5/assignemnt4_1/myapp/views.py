from django.shortcuts import render
from django.shortcuts import render

from django.db.models import Q

from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductMst, ProductSubCat
from .forms import ProductSubCatForm


def product_list(request):
    products = ProductMst.objects.all()
    return render(request,'product_list.html',{'products': products})

def product_subcat_list(request, product_id):
    product = get_object_or_404(ProductMst, pk=product_id)
    subcategories = ProductSubCat.objects.filter(product=product)
    return render(request, 'product_subcat_list.html', {'product': product, 'subcategories': subcategories})

def add_product_subcat(request, product_id):
    product = get_object_or_404(ProductMst, pk=product_id)
    
    if request.method == 'POST':
        form = ProductSubCatForm(request.POST, request.FILES)
        if form.is_valid():
            subcat = form.save(commit=False)
            subcat.product = product
            subcat.save()
            return redirect('product_subcat_list', product_id=product_id)
    else:
        form = ProductSubCatForm()

    return render(request, 'add_product_subcat.html', {'product': product, 'form': form})

def edit_product_subcat(request, product_id, subcat_id):
    product = get_object_or_404(ProductMst, pk=product_id)
    subcat = get_object_or_404(ProductSubCat, pk=subcat_id)

    if request.method == 'POST':
        form = ProductSubCatForm(request.POST, request.FILES, instance=subcat)
        if form.is_valid():
            form.save()
            return redirect('product_subcat_list', product_id=product_id)
    else:
        form = ProductSubCatForm(instance=subcat)

    return render(request, 'edit_product_subcat.html', {'product': product, 'form': form, 'subcat': subcat})

def delete_product_subcat(request, product_id, subcat_id):
    subcat = get_object_or_404(ProductSubCat, pk=subcat_id)
    subcat.delete()
    return redirect('product_subcat_list', product_id=product_id)


def search_products(request):
    query = request.GET.get('q')
    if query:
        products = ProductMst.objects.filter(Q(product_name__icontains=query))
        return render(request, 'search_results.html', {'products': products, 'query': query})
    else:
        return render(request, 'search_results.html')

def product_detail(request, product_id):
    product = get_object_or_404(ProductMst, pk=product_id)
    subcategories = ProductSubCat.objects.filter(product=product)

    return render(request,'product_detail.html', {'product': product,'subcategories': subcategories})