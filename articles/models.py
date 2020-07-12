from django.db import models

# Create your models here.
class all_info(models.Model):
    email = models.CharField(max_length=45,default="")
    author = models.CharField(max_length=20,default="Anonymous",null=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100000000000,default="Nothing Here...")
    date = models.DateField()
    image = models.ImageField(upload_to="articles/images", default="")

    def __str__(self):
        return self.title
