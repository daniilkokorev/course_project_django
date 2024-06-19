from django import forms

from common.views import StyleFormMixin
from mailing.models import MailingSettings, Message
from recipient.models import Recipient


class MailingSettingsForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для создания настроек рассылки
    """
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        user = self.request.user
        super().__init__(*args, **kwargs)
        self.fields['recipient'].queryset = Recipient.objects.filter(owner=user)
        self.fields['message'].queryset = Message.objects.filter(owner=user)

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


class MailingModeratorForm(StyleFormMixin, forms.ModelForm):
    """
    Форма модератора рассылки
    """
    class Meta:
        model = MailingSettings
        fields = ('status',)
