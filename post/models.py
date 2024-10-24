from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):

    title = models.CharField( max_length=50)
    content = models.TextField()
    createed_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post-img/')

    

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})
