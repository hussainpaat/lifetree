from django.db import models
import datetime
from tinymce.models import HTMLField

class category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    date = models.DateField(("Date"), default=datetime.date.today)
    content = HTMLField()

    def __str__(self):
        return self.name

class service(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    cat = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class gallery(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    cat = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class blog(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    date = models.DateField(("Date"), default=datetime.date.today)
    content = HTMLField()
    cat = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class doctor(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    specialist = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pics')
    training = HTMLField()
    facebook = models.CharField(max_length=200, default="https://facebook.com")
    twitter = models.CharField(max_length=200, default="https://twitter.com/")
    instagram = models.CharField(max_length=200, default="https://instagram.com")
    linkedin = models.CharField(max_length=200, default="https://linkedin.com")
    date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return self.name

class testimonial(models.Model):
    name = models.CharField(max_length=100)
    testimonial = models.CharField(max_length=400)

    def __str__(self):
        return self.name
