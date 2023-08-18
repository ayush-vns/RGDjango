from django.db import models

class regis(models.Model):
   Username = models.CharField(max_length = 300)
   Name = models.CharField(max_length = 50)
   Password = models.CharField(max_length = 50)

   def __str__(self):
        return "Username={0},Name={1},Password{2}".format(self.Username, self.Name,self.Password)

  