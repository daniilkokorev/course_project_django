from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from blog.forms import BlogForm
from blog.models import Blog

# Create your views here.


class BlogListView(LoginRequiredMixin, ListView):
    """
    Контролер отображает список блогов
    """
    model = Blog


class BlogDetailView(LoginRequiredMixin, DetailView):
    """
    Контролер отображает блог
    """
    model = Blog

    def get_object(self, queryset=None):
        """
        Метод увеличивает количество просмотров блога
        """
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogCreateView(LoginRequiredMixin, CreateView):
    """
    Контролер создает новый блог
    """
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        post = form.save()
        post.owner = self.request.user
        post.save()
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контролер обновляет информацию о блоге
    """
    model = Blog
    form_class = BlogForm

    def get_success_url(self):
        return reverse_lazy('blog:view', kwargs={'pk': self.object.pk})


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контролер удаляет блог
    """
    model = Blog
    success_url = reverse_lazy('blog:list')
