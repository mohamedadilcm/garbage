from django.db import models
from django.contrib.auth.models import AbstractBaseUser,Group
from django.db import models
from .manager import UserManager
# Create your models here.



class User(AbstractBaseUser):
    full_name = models.CharField(max_length=60,blank=False,null=False)
    phone=models.CharField(max_length=13,blank=False,null=False,unique=True)
    email=models.EmailField(max_length=200,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    address = models.TextField()
    ROLE_CHOICES = (
          
        ('admin', 'Admin'),
        ('customer','customer'),
        ('driver','driver')
        
    )
    user_type = models.CharField(max_length=20,default='customer', choices=ROLE_CHOICES)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff
    


class GarbageBin(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveBigIntegerField()
    

    def __str__ (self):
        return self.name
    

class UserGarbageBin(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="garbage")
    bin = models.ManyToManyField(GarbageBin)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')


class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="complaints")
    issue = models.TextField()
    accepted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    



class Area(models.Model):
    root = models.CharField(max_length=100)

    def __str__(self):
        return self.root



class UserArea(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="userarea")
    area = models.ForeignKey(Area,on_delete=models.DO_NOTHING)
    street = models.CharField(max_length=100)
    buildingno=models.CharField(max_length=100)





class CollectionRequest(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    bin = models.ForeignKey(GarbageBin, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)





 





    


