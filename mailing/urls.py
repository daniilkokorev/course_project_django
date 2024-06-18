from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import (MessageListView, MessageCreateView, MessageDeleteView, MessageDetailView,
                           MessageUpdateView,
                           MailingSettingsListView, MailingSettingsCreateView, MailingSettingsDeleteView,
                           MailingSettingsDetailView, MailingSettingsUpdateView,
                           )

app_name = MailingConfig.name

urlpatterns = [
    path("", MessageListView.as_view(), name="list"),
    path("<int:pk>/", MessageDetailView.as_view(), name="view"),
    path("create/", MessageCreateView.as_view(), name="create"),
    path("<int:pk>/update/", MessageUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", MessageDeleteView.as_view(), name="delete"),
    path("settings", MailingSettingsListView.as_view(), name="settings_list"),
    path("settings/<int:pk>/", MailingSettingsDetailView.as_view(), name="settings_view"),
    path("settings/create/", MailingSettingsCreateView.as_view(), name="settings_create"),
    path("settings/<int:pk>/update/", MailingSettingsUpdateView.as_view(), name="settings_edit"),
    path("settings/<int:pk>/delete/", MailingSettingsDeleteView.as_view(), name="settings_delete"),
    ]
