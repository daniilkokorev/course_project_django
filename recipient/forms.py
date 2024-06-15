from django import forms

from common.views import StyleFormMixin
from recipient.models import Recipient


class RecipientForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для получателя
    """
    class Meta:
        model = Recipient
        fields = ('email', 'name', 'description',)
