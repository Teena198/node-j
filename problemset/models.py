from django.db import models
# Create your models here.


class Problem(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    statement = models.CharField(max_length=500)
    input = models.CharField(max_length=100)
    output = models.CharField(max_length=100)
    tl = models.FloatField(default=2.00)
    ml = models.IntegerField()
    todo = models.BooleanField(default=False)


class Test(models.Model):
    inp = models.FileField(upload_to='test/', null=True)
    out = models.FileField(upload_to='test/', null=True)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)