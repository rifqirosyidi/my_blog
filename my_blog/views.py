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
        context['recent_posts'] = Post.objects.all().order_by('-created_at')[:15]
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
        context['recent_posts'] = Post.objects.all().order_by('-created_at')[:15]
        return context


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['recent_posts'] = Post.objects.all().order_by('-created_at')[:15]
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['recent_posts'] = Post.objects.all().order_by('-created_at')[:15]
        return context


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

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['recent_posts'] = Post.objects.all().order_by('-created_at')[:15]
        return context


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
