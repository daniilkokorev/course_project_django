from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import (MessageListView, MessageCreateView, MessageDeleteView, MessageDetailView,
                           MessageUpdateView,
                           MailingSettingsListView, MailingSettingsCreateView, MailingSettingsDeleteView,
                           MailingSettingsDetailView, MailingSettingsUpdateView, MessageTemplateView,
                           )

app_name = MailingConfig.name

urlpatterns = [
    path("", MessageTemplateView.as_view(), name="home"),
    path("list/", MessageListView.as_view(), name="list"),
    path("<int:pk>/", cache_page(60)(MessageDetailView.as_view()), name="view"),
    path("create/", MessageCreateView.as_view(), name="create"),
    path("<int:pk>/update/", MessageUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", MessageDeleteView.as_view(), name="delete"),
    path("settings", MailingSettingsListView.as_view(), name="settings_list"),
    path("settings/<int:pk>/", cache_page(60)(MailingSettingsDetailView.as_view()), name="settings_view"),
    path("settings/create/", MailingSettingsCreateView.as_view(), name="settings_create"),
    path("settings/<int:pk>/update/", MailingSettingsUpdateView.as_view(), name="settings_edit"),
    path("settings/<int:pk>/delete/", MailingSettingsDeleteView.as_view(), name="settings_delete"),
    ]
