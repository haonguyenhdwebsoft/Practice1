from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create-category/", views.create_category, name="create_category"),
    path("category-list/", views.category_list, name="category_list"),
    path("update-category/<int:category_id>", views.update_category, name="update_category"),
    path("delete-category/<int:category_id>", views.delete_category, name="delete_category"),
    path("create-product/", views.create_product, name="create_product"),
    path("product-list/", views.product_list, name="product_list"),
    path("update-product/<int:product_id>", views.update_product, name="update_product"),
    path("delete-product/<int:product_id>", views.delete_product, name="delete_product"),
    path("product-detail/<int:product_id>", views.product_detail, name="product_detail")
]