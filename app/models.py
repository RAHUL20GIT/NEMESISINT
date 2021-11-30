from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin
# Create your models here.



class UserManager(BaseUserManager):
    def create_user(self,email,username,password,address, **other_fields):
        if not email:
            raise ValueError("provide an Email")
        email=self.normalize_email(email)
        user=self.model(email=email,username=username,address=address,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username,password,address,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)


        if other_fields.get('is_staff') is not True:
            raise ValueError('Super user must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Super user must be assigned to is_superuser=True')

        return self.create_user(email,username,password,address,**other_fields)

class NewUser(AbstractUser,PermissionsMixin):
    email=models.EmailField()
    username=models.CharField(max_length=200,unique=True)
    address=models.CharField(max_length=200)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects=UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['address','email']

    def __str__(self):
        return self.username