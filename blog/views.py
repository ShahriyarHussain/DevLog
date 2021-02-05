from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from .models import Post, Votes, Comments
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView
                                  )
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .forms import CommentForm


@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


# @login_required
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 7


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(FormMixin, DetailView):
    model = Post
    form_class = CommentForm

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(
            initial={'post': self.object, 'author': self.request.user})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.cleaned_data['author_id'] = self.request.user
            form.cleaned_data['post_id'] = self.object
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetailView, self).form_valid(form)


# def comment(self, request, pk):
#     template_name = 'post-detail'
#     author = self.request.user
#     post = get_object_or_404(Post, pk=pk)
#     new_comment = None

#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)

#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.post = post
#             new_comment.author = author
#             new_comment.save()
#             messages.success(
#                 request, f'Comment Posted!')
#             return redirect('post-detail', pk=post.pk)

#         else:
#             comment_form = CommentForm()
#             messages.warning(
#                 request, f' Invalid comment!')

#         return render(request, template_name, {'post': post,
#                                                'author': author,
#                                                'new_comment': new_comment,
#                                                'comment_form': comment_form})


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


# @login_required
def postdetail(self, request, pk):
    template_name = 'post-detail'
    author = self.request.user
    post = get_object_or_404(Post, pk=pk)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = author
            new_comment.save()
            messages.success(
                request, f'Comment Posted!')
            return redirect('post-detail', pk=post.pk)

        else:
            comment_form = CommentForm()
            messages.warning(
                request, f' Invalid comment!')

        return render(request, template_name, {'post': post,
                                               'author': author,
                                               'new_comment': new_comment,
                                               'comment_form': comment_form})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
