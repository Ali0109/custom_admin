from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    category = models.ForeignKey("Category", on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
