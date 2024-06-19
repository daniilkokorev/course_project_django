from django import forms

from blog.models import Blog
from common.views import StyleFormMixin


class BlogForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для блога
    """
    class Meta:
        model = Blog
        fields = ('name', 'content', 'preview', 'is_published', )
