from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Post, Comment


def add_comment(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        text = request.POST.get('text')
        
        if not text:
            return JsonResponse({'error': 'Текст не може бути порожнім'}, status=400)
            
        post = get_object_or_404(Post, id=post_id)
        comment = Comment.objects.create(post=post, text=text)
        
        return JsonResponse({
            'id': comment.id,
            'text': comment.text,
            'new_count': post.comment_set.count() 
        })


def delete_comment(request, comment_id):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=comment_id)
        post = comment.post
        comment.delete()
        
        return JsonResponse({
            'status': 'success',
            'new_count': post.comment_set.count()
        })


def like_post(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        post.likes += 1
        post.save()
        
        return JsonResponse({
            'likes': post.likes,
            'dislikes': post.dislikes
        })


def dislike_post(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        post.dislikes += 1
        post.save()
        
        return JsonResponse({
            'likes': post.likes,
            'dislikes': post.dislikes
        })
