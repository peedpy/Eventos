from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager, models.Manager):
    def __create_user(self, username, email, password, is_staff, is_superuser, **extrafields):
        email = self.normalize_email(email)
        if not email:
            raise ValueError('El email debe ser obligatorio')
        user = self.model(  username=username,
                            email=email,
                            is_active=True,
                            is_staff=is_staff,
                            is_superuser=is_superuser,
                            **extrafields
        )
        #Setear el password
        user.set_password(password)
        user.save(using = self._db)
        return user

    #Para crear usuario
    def create_user(self, username, email,password=None, **extrafields):
        return self.__create_user(username, email, password, False, False, **extrafields)

    #Para crear super usuario
    def create_superuser(self, username, email,password=None, **extrafields):
        return self.__create_user(username, email, password, True, True, **extrafields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="users") #Falta hacer algo
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    #Si quiero crear un superuser
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    def get_short_name(self):
        return self.username
