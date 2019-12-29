from django.db import models

class Blog(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    pub_date = models.DateField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]