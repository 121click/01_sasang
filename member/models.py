from django.db import models
class Member(models.Model):

    user_id = models.CharField(max_length=50, unique=True)
    user_pw = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    user_birth = models.DateField()
    user_gender = models.SmallIntegerField(null=True)
    date_joined = models.DateTimeField()
    result_type = models.CharField(max_length=200, null=True)
    
    # class Meta:
    #     db_table = 'member'
    #     ordering = ['-id']