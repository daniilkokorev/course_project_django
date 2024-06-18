from django import forms

from common.views import StyleFormMixin
from mailing.models import MailingSettings, Message


class MailingSettingsForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для создания настроек рассылки
    """
    class Meta:
        model = MailingSettings
        fields = ('frequency', 'message', 'recipient', 'last_datetime',)


class MassageForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для создания сообщения
    """
    class Meta:
        model = Message
        fields = ('title', 'content',)
