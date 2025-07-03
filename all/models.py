from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_it = models.DateField()
    category_name = models.ForeignKey("Category", on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = ("Article")
        verbose_name_plural = ("Articles")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)
        
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    
    def __str__(self):
        return self.name