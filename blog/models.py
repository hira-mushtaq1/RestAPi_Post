from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    firstname=models.CharField(max_length=50, default='Hira')
    # content = models.TextField()
    lastname=models.CharField(max_length=50, default='Mushtaq')
    email=models.EmailField((""), max_length=254, default='hira.mushtaq@alrafayconsulting.com')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title