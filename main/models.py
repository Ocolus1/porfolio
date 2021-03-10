from django.db import models

class Feedback(models.Model):
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

