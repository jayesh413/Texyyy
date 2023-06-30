from djongo import models


class Text (models.Model):
    inp_text=models.CharField(max_length=100)
    output_text=models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

# Create your models here.
    def __str__(self):
       return self.inp_text

