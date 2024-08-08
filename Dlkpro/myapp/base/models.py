from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils.translation import gettext_lazy as _

class UserRegistration(models.Model):
    username= models.CharField(max_length=50)
    useremail = models.EmailField(max_length=100)
    password = models.CharField(max_length=60)
    confirm_password = models.CharField(max_length=60)
    
    
    def _str_(self):
        return self.username
    

# class UserLogin(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=60)



#     def _str_(self):
#         return self.username
  

  
    
