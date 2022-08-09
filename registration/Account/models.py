from django.db import models
from django.contrib.auth import models as auth_models

UserType=[
    ('Staff','Staff'),
    ('Student','Student')
]

class Manager(auth_models.BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None, **extra_fields):
            if not email:
                raise ValueError("User must have an email")
            if not password:
                raise ValueError("User must have a password")

            email=self.normalize_email(email)
            
            user=self.model(
                email=email,first_name=first_name,
                last_name=last_name,
                username=username,
                **extra_fields
            )
            user= UserType[1][0]
            user.set_password(password)
            user.save(using= self.db)
            return user
    def create_super(self, email,Password,first_name,last_name,username, **extra_fields):
        if not email:
            raise ValueError("Superuser must have an email")
        if not Password:
            raise ValueError("Superuser must have a password")
        
        email=self.normalize_email(email)
            
        user=self.model(
                email=email,first_name=first_name,
                last_name=last_name,
                username=username,
                **extra_fields
            )
        user.is_staff=True
        user.is_superuser=True
        user.is_active=True
        user.save(using= self.db)
        


class User(auth_models.AbstractUser):
    first_name=models.CharField(max_length=50, null=True)
    last_name=models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=254, unique=True)
    password=models.CharField(max_length=50)
    usertype=models.CharField(choices=UserType , max_length=50, default="Student")
    username=models.CharField(max_length=50)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS= ['password', 'usertype']

    is_active = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    

    def __str__(self):
         return self.email
