from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
   pass

   class Meta:
      pass
   
   def __str__(self):
        return self.username
