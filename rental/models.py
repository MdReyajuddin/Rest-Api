from django.db import models

# Create your models here.
class Friend(models.Model):
    name=models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Belonging(models.Model):
    name=models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Borrowed(models.Model):
    what=models.ForeignKey(Belonging, on_delete=models.CASCADE)
    who=models.ForeignKey(Friend, on_delete=models.CASCADE)
    when=models.DateTimeField(auto_now_add=True)
    returned=models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.who.name
