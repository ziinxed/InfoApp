from django.db import models

class Links(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    url = models.TextField()
    source = models.CharField(default='yonsei.ac.kr', max_length=100)
    class Meta:
        ordering = ['created']

# Create your models here.
