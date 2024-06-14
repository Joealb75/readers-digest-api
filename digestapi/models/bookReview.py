from django.db import models
from django.contrib.auth.models import User

class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books_reviewed")
    bookName = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    reviewContent = models.TextField(max_length=1000)
    datePosted = models.DateTimeField(auto_now_add=True)
