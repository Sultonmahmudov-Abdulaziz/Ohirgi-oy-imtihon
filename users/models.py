from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    publikatsiya = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
            return self.publikatsiya


class Comment(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
      post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
      coment = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      
      def __str__(self):
        return f"Comment by {self.user.username} on {self.post} - {self.coment}"
    

class Likes(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="like")
     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)


     def __str__(self):
          return f"{self.user.username} liked {self.post.publikatsiya}"
     



