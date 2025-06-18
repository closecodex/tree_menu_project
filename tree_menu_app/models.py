from django.db import models
from django.urls import reverse, NoReverseMatch

class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True, help_text="URL или name для reverse")
    named_url = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.url)
            except NoReverseMatch:
                return '#'
        return self.url
