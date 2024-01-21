from django.db import models
from django.utils import timezone

# print(my_ctg) === print(my_ctg.__str___())
# aruzhan
# 123456789

class Category(models.Model):
    title=models.CharField(max_length=300)
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self): # как отображается в админ панеле
        return self.title

class Course(models.Model):
    title=models.CharField(max_length=255)
    price=models.FloatField()
    students_qty=models.IntegerField()
    reviews_qty=models.IntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title