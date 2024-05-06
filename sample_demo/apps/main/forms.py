from django.forms import ModelForm, TextInput, FileInput, SelectMultiple, ClearableFileInput
from .models import Category, Product, ProductImage

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name", "image"]
        labels = {
            "name": "Name",
            "image": "Image"
        }
        widgets = {
            "name": TextInput(attrs={"class": "form-control", "placeholder": "Input name..."}),
            "image": FileInput(attrs={"class": "form-control-file"})
        }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "categories"]
        labels = {
            "name": "Name",
            "categories": "Categories"
        }
        widgets = {
            "name": TextInput(attrs={"class": "form-control", "placeholder": "Input name..."}),
            "categories": SelectMultiple(attrs={"class": "form-control"})
        }