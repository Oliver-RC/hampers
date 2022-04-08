from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_products, name="products"),
    path("<int:product_id>/", views.product_detail, name="product_detail"),
    path("add/", views.add_product, name="add_product"),
    path("edit/<int:product_id>/", views.edit_product, name="edit_product"),
    path("delete/<int:product_id>/", views.delete_product, name="delete_product"),
    path("review/<int:product_id>/", views.review_submission, name="review_submission"),
    path("saved_item_list/", views.saved_item_list, name="saved_item_list"),
    path(
        "add_saved_items/<int:product_id>/",
        views.add_saved_items,
        name="add_saved_items",
    ),
    path(
        "remove_saved_items/<int:product_id>/",
        views.remove_saved_items,
        name="remove_saved_items",
    ),
]
