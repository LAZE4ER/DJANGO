# from django.db import models

# from django.db.models import ForeignKey, TextField
# from django.contrib.auth import get_user_model
# # Create your models here.
# UserModel = get_user_model()


# class Post(models.Model):
#     author = models.ForeignKey(
#         UserModel, on_delete=models.CASCADE, related_name="posts"
#     )
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.title} by {self.author}"
    
# class Comment(models.Model):
#     post = ForeignKey(Post, on_delete = models.CASCADE)
#     author = ForeignKey(UserModel, on_delete = models.CASCADE)
#     text = TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f' {self.author.username} comment on {self.post.title}'
    
    
    
# class Tag(models.Model):
#     name = models.CharField(max_length=30, unique=True)

#     def __str__(self):
#         return self.name







