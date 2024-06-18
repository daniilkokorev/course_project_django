from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.forms import MailingSettingsForm, MassageForm
from mailing.models import MailingSettings, Message, MailingStatus


class MessageCreateView(CreateView):
    """
    Контролер создает сообщение
    """
    model = Message
    form_class = MassageForm
    success_url = reverse_lazy('mailing:list')


class MessageListView(ListView):
    """
    Контролер отображает список сообщений
    """
    model = Message


class MessageUpdateView(UpdateView):
    """
    Контролер редактирует сообщение
    """
    model = Message
    form_class = MassageForm
    success_url = reverse_lazy('mailing:list')


class MessageDeleteView(DeleteView):
    """
    Контролер удаляет сообщение
    """
    model = Message
    success_url = reverse_lazy('mailing:list')


class MessageDetailView(DetailView):
    """
    Контролер отображает сообщение
    """
    model = Message


class MailingSettingsCreateView(CreateView):
    """
    Контролер создает рассылку
    """
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:settings_list')


class MailingSettingsUpdateView(UpdateView):
    """
    Контролер редактирует рассылку
    """
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:settings_list')


class MailingSettingsDeleteView(DeleteView):
    """
    Контролер удаляет рассылку
    """
    model = MailingSettings
    success_url = reverse_lazy('mailing:settings_list')


class MailingSettingsDetailView(DetailView):
    """
    Контролер отображает рассылку
    """
    model = MailingSettings


class MailingSettingsListView(ListView):
    """
    Контролер отображает список рассылок
    """
    model = MailingSettings


class MailingStatusListView(ListView):
    """
    Контролер отображает список статусов рассылок
    """
    model = MailingStatus


class MailingStatusDeleteView(DeleteView):
    """
    Контролер удаляет статус рассылки
    """
    model = MailingStatus
    success_url = reverse_lazy('mailing:status_list')
