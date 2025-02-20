from django.db import models
from django.utils.text import slugify

class ContactSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Client(models.Model):
    CLIENT_TYPE_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]

    name = models.CharField(max_length=100)
    client_type = models.CharField(
        max_length=10,
        choices=CLIENT_TYPE_CHOICES,
        default='public',
    )
    image = models.ImageField(upload_to='clients/')
    description = models.TextField()

    def __str__(self):
        return self.name
    
class TimelineItem(models.Model):
    POSITION_CHOICES = [
        ('left', 'Left'),
        ('right', 'Right'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField()
    additional_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='timeline_images/', blank=True, null=True)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)
    left_placeholder = models.CharField(max_length=200, blank=True, null=True)
    right_placeholder = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name