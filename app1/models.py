from django.db import models

# Create your models here.
class MovieWorldModel(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField()
    language=models.CharField(max_length=20)
    year=models.IntegerField(default=0)
    image=models.ImageField(upload_to="image")
def __str__(self):

    return self.title
