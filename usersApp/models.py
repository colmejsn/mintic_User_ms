from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, identi=None, doctor=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.set_doctor(doctor)
        user.set_identi(identi)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, identi , doctor):
        user = self.create_user(username=username, password=password, identi=identi, doctor=doctor)
        user.is_admin = True
        user.save(using=self._db)
        return user
        
class bankUser(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Name', max_length = 15, unique=True)
    password = models.CharField('Password', max_length = 256)
    identi = models.CharField('identi', max_length = 255,null=True )
    doctor = models.BooleanField('doctor',null=True)
    objects = UserManager()
    
    USERNAME_FIELD = 'username'