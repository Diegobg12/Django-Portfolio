from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=20)
    pub_date =  models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:50]

    def pub_date_short(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title


        
# Create A blog Models

# Create a migration

# Migrate

# Add the admin
