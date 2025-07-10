from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    author = models.ForeignKey(
        "auth.User", on_delete=models.SET_NULL, blank=True, null=True
    )
    categories = models.ManyToManyField("Category", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=100)
    sumary = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    document = models.FileField(upload_to="projects/documents/", blank=True, null=True)
    author = models.ForeignKey(
        "auth.User", on_delete=models.SET_NULL, blank=True, null=True
    )
    categories = models.ManyToManyField("Category", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(
        Article, on_delete=models.SET_NULL, blank=True, null=True
    )
    project = models.ForeignKey(
        "Project", on_delete=models.SET_NULL, blank=True, null=True
    )
    author = models.ForeignKey(
        "auth.User", on_delete=models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} in {self.created_at}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
