from django.db import models
from django.utils import timezone
# Create your models here.
class UserInfo(models.Model):
  name_text = models.CharField(max_length=50)
  birth_date = models.DateTimeField('Date of birth')
  def __str__(self):
        return self.name_text
  def age(self):
     return self.birth_date - timezone.now()

class OtherInfo(models.Model):
  userinfo = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
  age = models.IntegerField(default=0)
  skills = models.CharField(max_length=200)
  def __str__(self):
        return self.skills