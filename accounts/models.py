from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class BaseUser(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('email is required')
    
        user = self.model(
            email=self.normalize_email(email) 
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username ,email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password
        )

        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user

class User(AbstractUser):
    username = models.CharField(max_length=20, blank=False, unique=True)    
    first_name = models.TextField(max_length=20, blank=False)
    last_name = models.TextField(max_length=50, blank=False)
    full_name = models.TextField(max_length=70, blank=False)
    email = models.EmailField(max_length=60, unique=True, blank=False)
    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    date_of_birth = models.DateField(blank=False)
    CPF = models.CharField(max_length=30)
    wallet = models.IntegerField(blank=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'full_name', 'date_of_birth', 'CPF', 'wallet']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

     # deverá haver uma chave única que identifica a transação, podendo ser o e-mail ou username