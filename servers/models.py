from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Server(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    ip = models.CharField(max_length=15, null=False, blank=False, unique=True)
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        app_label = 'servers'
        db_table = 'servers'
        verbose_name = 'server'
        verbose_name_plural = 'servers'


class UserProfileManager(BaseUserManager):
    def create_user(self, email, username, first_name, middle_name,
                    last_name, work_position, password=None, **extra_fields):
        # Data validation
        if not email:
            raise ValueError('Users must have the email address')
        if not username:
            raise ValueError('Users must have the username')
        if not first_name:
            raise ValueError('Users must have the first_name')
        if not middle_name:
            raise ValueError('Users must have the middle_name')
        if not last_name:
            raise ValueError('Users must have the second_name')
        if not work_position:
            raise ValueError('Users must have the work position')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            work_position=work_position,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, middle_name,
                         last_name, work_position, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            work_position=work_position
        )

        # Define superuser features
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    work_position = models.CharField(max_length=20)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=40, unique=True)

    objects = UserProfileManager()

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # Login field
    REQUIRED_FIELDS = ('username', 'first_name', 'middle_name', 'last_name', 'work_position')

    class Meta:
        app_label = 'servers'
        db_table = 'user_profiles'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ('date_joined',)

    # Utility stuff
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
