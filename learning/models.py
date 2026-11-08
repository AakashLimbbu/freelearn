from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class Resource(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
    ]

    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)

    description = models.TextField()

    file_link = models.CharField(max_length=500)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    uploaded_by = models.CharField(max_length=100)

    def __str__(self):
        return self.title