from django.db import models

# Create your models here.
class Users(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.TextField(max_length=255)
    age=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

def create_user(data):

    Users.objects.create(first_name=data['fname'],last_name=data['lname'],email=data['email'],age=data['age'])

def get_all_users():
    return Users.objects.all()

def del_user(id):

    temp_user=Users.objects.get(id=id)

    temp_user.delete()