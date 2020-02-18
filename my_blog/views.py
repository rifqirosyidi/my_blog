from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.models import User


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['recent_posts'] = Post.objects.all().order_by('-created_at')[:10]
        return context


class UserPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'my_blog/post_user.html'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, id=self.kwargs.get('user_id'))
        return Post.objects.filter(author=user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        kwargs['author'] = get_object_or_404(User, id=self.kwargs.get('user_id'))
        context = super(UserPostListView, self).get_context_data(**kwargs)
        return context


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'my_blog/about.html', context)