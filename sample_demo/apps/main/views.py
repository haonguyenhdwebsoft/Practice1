from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, ProductForm
from .models import Category, Product, ProductImage

# Create your views here.
@login_required
def dashboard(request):
    user = request.user
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, "dashboard/dashboard.html", {"user": user, "categories": categories, "products": products})

@login_required
def create_category(request):
    user = request.user
    if request.method == "POST":
        category_form = CategoryForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return redirect("dashboard")
    else:
        category_form = CategoryForm()
    return render(request, "category/create_category.html", {"user": user, "form": category_form})

@login_required
def category_list(request):
    user = request.user
    categories = Category.objects.all()
    return render(request, "category/category_list.html", {"user": user, "categories": categories})

@login_required
def update_category(request, category_id):
    user = request.user
    if request.method == "POST":
        category = Category.objects.get(pk=category_id)
        category_form = CategoryForm(request.POST, request.FILES, instance=category)
        if category_form.is_valid():
            category_form.save()
            return redirect("category_list")
    else:
        category = Category.objects.get(pk=category_id)
        category_form = CategoryForm(instance=category)
    return render(request, "category/update_category.html", {"user": user, "form": category_form})

@login_required
def delete_category(request, category_id):
    if request.method == "POST":
        category = Category.objects.get(pk=category_id)
        category.delete()
    return redirect("category_list")

@login_required
def create_product(request):
    user = request.user
    if request.method == "POST":
        product = Product()
        product_form = ProductForm(request.POST, instance=product)
        files = request.FILES.getlist("files")
        if product_form.is_valid():
            product_form.save()
            for file in files:
                product_image = ProductImage(image_name=file.name, image=file, product=product_form.instance)
                product_image.save()
            return redirect("dashboard")
    else:
        product_form = ProductForm()
    return render(request, "product/create_product.html", {"user": user, "form": product_form})

@login_required
def product_list(request):
    user = request.user
    products = Product.objects.all()
    return render(request, "product/product_list.html", {"user": user, "products": products})

@login_required
def update_product(request, product_id):
    user = request.user
    if request.method == "POST":
        product = Product.objects.get(pk=product_id)
        product_form = ProductForm(request.POST, instance=product)
        files = request.FILES.getlist("files")
        if product_form.is_valid():
            product_form.save()
            if len(files) > 0:
                ProductImage.objects.filter(product=product_form.instance).delete()
                for file in files:
                    product_image = ProductImage(image_name=file.name, image=file, product=product_form.instance)
                    product_image.save()
            return redirect("product_list")
    else:
        product = Product.objects.get(pk=product_id)
        product_form = ProductForm(instance=product)
    return render(request, "product/update_product.html", {"user": user, "form": product_form})

@login_required
def delete_product(request, product_id):
    if request.method == "POST":
        product = Product.objects.get(pk=product_id)
        product.delete()
    return redirect("product_list")

@login_required
def product_detail(request, product_id):
    user = request.user
    product = Product.objects.get(pk=product_id)
    product_images = ProductImage.objects.filter(product=product)
    return render(request, "product/product_detail.html", {"user": user, "product": product, "product_images": product_images})