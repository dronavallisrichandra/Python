from django.db import models

# Create your models here.

class HrUser(models.Model):
    
    username = models.CharField(max_length=50, primary_key=True)

    password = models.CharField(max_length=50) 

    def __str__(self):

        return self.username


class TechUser(models.Model):
    
    username = models.CharField(max_length=50, primary_key=True)

    password = models.CharField(max_length=50) 

    email = models.EmailField(max_length=50) 

    phone = models.CharField(max_length=50) 

    dob=models.DateField()

    gender=models.CharField(max_length=10)
    

    def __str__(self):

        return self.username

class JobUser(models.Model):
    
    username = models.CharField(max_length=50, primary_key=True)

    password = models.CharField(max_length=50) 

    email = models.EmailField(max_length=50) 

    phone = models.CharField(max_length=50) 

    dob=models.DateField()

    gender=models.CharField(max_length=10)

    addr=models.TextField(default='')
    
    def __str__(self):

        return self.username

class JobPost(models.Model):

    JobTitle = models.CharField(max_length=50)

    Description = models.CharField(max_length=300) 

    location = models.CharField(max_length=50) 

    salary_package = models.CharField(max_length=50) 

    PostDate=models.DateField()

class Profile(models.Model):
   
    experience = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    job_role = models.CharField(max_length=50)
    username=models.ForeignKey(JobUser,on_delete=models.CASCADE)

class JobApply(models.Model):

    job_id = models.CharField(max_length=10)

    username = models.CharField(max_length=30)



