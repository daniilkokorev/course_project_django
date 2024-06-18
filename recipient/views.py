from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from recipient.forms import RecipientForm
from recipient.models import Recipient


class RecipientListView(ListView):
    """
    Контролер отображает список получателей
    """
    model = Recipient


class RecipientDetailView(DetailView):
    """
    Контролер отображает информацию о получателе
    """
    model = Recipient


class RecipientCreateView(CreateView):
    """
    Контролер создает нового получателя
    """
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy('recipient:list')


class RecipientUpdateView(UpdateView):
    """
    Контролер обновляет информацию о получателе
    """
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy('recipient:list')


class RecipientDeleteView(DeleteView):
    """
    Контролер удаляет получателя
    """
    model = Recipient
    success_url = reverse_lazy('recipient:list')
