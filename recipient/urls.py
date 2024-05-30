from django.urls import path

from recipient.apps import RecipientConfig
from recipient.views import (RecipientListView, RecipientCreateView, RecipientDeleteView, RecipientDetailView,
                             RecipientUpdateView)

app_name = RecipientConfig.name

urlpatterns = [
    path("", RecipientListView.as_view(), name='list'),
    path("products/<int:pk>", RecipientDetailView.as_view(), name='product_info'),
    path("create/", RecipientCreateView.as_view(), name='create_product'),
    path("edit/<int:pk>",RecipientUpdateView.as_view(), name='update_product'),
    path("delete/<int:pk>", RecipientDeleteView.as_view(), name='delete_product'),
]
