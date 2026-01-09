from tokenize import Comment
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.shortcuts import get_object_or_404
from .models import Comment, Post, Tag
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.mixins import LoginRequiredMixin

class CommentsListView(ListView):
    model = Comment
    template_name = "comments/comments_list.html"
    context_object_name = "comments"
    
    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_id'])
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, id=self.kwargs['post_id'])
        return context



class CommentDetailView(DetailView):
    model = Comment
    template_name = "comments/comment_detail.html"
    context_object_name = "comment"



class CommentCreateView(CreateView, LoginRequiredMixin):
    model = Comment
    template_name = "comments/comment_form.html"
    fields = [ 'text']
    success_url = '/comments/'
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['post_id']
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class CommentUpdateView(UpdateView, LoginRequiredMixin):
    model = Comment
    template_name = "comments/comment_form.html"
    fields = ['text']
    success_url = '/comments/'

class CommentDeleteView(DeleteView, LoginRequiredMixin):
    model = Comment
    template_name = "comments/comment_confirm_delete.html"
    success_url = '/comments/'




@login_required(login_url='auth_user')
@require_POST
def create_tag(request):
    name = request.POST.get('name')

    if name:
        Tag.objects.create(name=name)
        return redirect('/tags/')
    
    return render(request, 'tags/tag_form.html', {
        'error': 'Name cannot be empty'
    })
@login_required(login_url='auth_user')
@require_GET
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags/tag_list.html', {
        'tags': tags
    })