from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from mailing.forms import MailingSettingsForm, MassageForm, MailingModeratorForm
from mailing.models import MailingSettings, Message, MailingStatus
from mailing.services import get_blog_from_cache
from recipient.models import Recipient


class MessageTemplateView(LoginRequiredMixin, TemplateView):
    """
    Контролер отображает главную страницу
    """
    template_name ='mailing/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blogs'] = get_blog_from_cache()
        mailing_settings = MailingSettings.objects.all()
        context_data['mailing_settings'] = len(mailing_settings)
        active_mailings = MailingSettings.objects.filter(status='Started')
        context_data['active_mailings'] = len(active_mailings)
        recipient = Recipient.objects.all()
        context_data['recipient'] = len(recipient)
        return context_data


class MessageCreateView(LoginRequiredMixin, CreateView):
    """
    Контролер создает сообщение
    """
    model = Message
    form_class = MassageForm
    success_url = reverse_lazy('mailing:list')

    def form_valid(self, form):
        massage = form.save()
        massage.owner = self.request.user
        massage.save()
        return super().form_valid(form)


class MessageListView(LoginRequiredMixin, ListView):
    """
    Контролер отображает список сообщений
    """
    model = Message


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контролер редактирует сообщение
    """
    model = Message
    form_class = MassageForm
    success_url = reverse_lazy('mailing:list')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контролер удаляет сообщение
    """
    model = Message
    success_url = reverse_lazy('mailing:list')


class MessageDetailView(LoginRequiredMixin, DetailView):
    """
    Контролер отображает сообщение
    """
    model = Message


class MailingSettingsCreateView(LoginRequiredMixin, CreateView):
    """
    Контролер создает рассылку
    """
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:settings_list')

    def form_valid(self, form):
        mailingsettings = form.save()
        mailingsettings.owner = self.request.user
        mailingsettings.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class MailingSettingsUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контролер редактирует рассылку
    """
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:settings_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            return MailingSettingsForm
        if user.has_perm('mailing.change_mailingsettings_setting_status'):
            return MailingModeratorForm
        return PermissionDenied

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class MailingSettingsDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контролер удаляет рассылку
    """
    model = MailingSettings
    success_url = reverse_lazy('mailing:settings_list')


class MailingSettingsDetailView(LoginRequiredMixin, DetailView):
    """
    Контролер отображает рассылку
    """
    model = MailingSettings


class MailingSettingsListView(LoginRequiredMixin, ListView):
    """
    Контролер отображает список рассылок
    """
    model = MailingSettings


class MailingStatusListView(LoginRequiredMixin, ListView):
    """
    Контролер отображает список статусов рассылок
    """
    model = MailingStatus


class MailingStatusDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контролер удаляет статус рассылки
    """
    model = MailingStatus
    success_url = reverse_lazy('mailing:status_list')
