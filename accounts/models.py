
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not email:
            raise ValueError('User must have a email address.')
        if not username:
            raise ValueError('User must have a unque username.')
        
        user=self.model(
            email=self.normalize_email(email),
            username=username,
        )
        
        user.set_password(password)

        user.save(using=self._db)

        return user
    
    def create_superuser(self,username,email,password=None):
        user=self.create_user(username,email,password)
        user.is_admin=True
        user.is_staff=True
        user.is_superadmin=True
        user.is_active=True

        user.save(using=self._db)

        return user
   


class User(AbstractBaseUser):
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=50,unique=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    
    USERNAME_FIELD='email'

    REQUIRED_FIELDS=['username']
    
    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

    objects=UserManager()

