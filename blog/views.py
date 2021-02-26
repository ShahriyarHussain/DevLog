from django.shortcuts import render, get_object_or_404, reverse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView
                                  )
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
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


class SearchListView(ListView):
    model = Post
    template_name = 'blog/search_list.html'
    ordering = ['-date_posted']
    # paginate_by = 7 #Paginate not working, gives 500 server error

    def get_queryset(self):
        query = self.request.GET.get('q')
        post_list = Post.objects.filter(Q(title__icontains=query) | Q(
            content__icontains=query) | Q(author__username__icontains=query) | Q(
            post_type__icontains=query) | Q(comments__content__icontains=query)).distinct()

        return post_list


class PostDetailView(FormMixin, DetailView):
    model = Post
    form_class = CommentForm

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(
            initial={})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            # form.cleaned_data['author_id'] = self.request.user
            # form.cleaned_data['post_id'] = self.object
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # def form_valid(self, form):
    #     form.save()
    #     return super(PostDetailView, self).form_valid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.post = self.object
        comment.save()
        return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'post_type']

    def form_valid(self, form):
        # form.instance.image = self.image.url
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image', 'post_type']

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
    return render(request, 'blog/about.html', {'title': 'About Oblog'})

# check tomorrow
# def form_valid(self, form):
#     comment = form.save(commit=False)
#     comment.author = self.request.user
#     comment.post = self.object
#     comment.save()
#     return super().form_valid(form)
