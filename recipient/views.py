from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from recipient.forms import RecipientForm
from recipient.models import Recipient


class RecipientListView(LoginRequiredMixin, ListView):
    """
    Контролер отображает список получателей
    """
    model = Recipient


class RecipientDetailView(LoginRequiredMixin, DetailView):
    """
    Контролер отображает информацию о получателе
    """
    model = Recipient


class RecipientCreateView(LoginRequiredMixin, CreateView):
    """
    Контролер создает нового получателя
    """
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy('recipient:list')

    def form_valid(self, form):
        recipient = form.save()
        recipient.owner = self.request.user
        recipient.save()
        return super().form_valid(form)


class RecipientUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контролер обновляет информацию о получателе
    """
    model = Recipient
    form_class = RecipientForm

    def get_success_url(self):
        return reverse_lazy('recipient:view', kwargs={'pk': self.object.pk})


class RecipientDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контролер удаляет получателя
    """
    model = Recipient
    success_url = reverse_lazy('recipient:list')
