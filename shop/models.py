from django.db import models
class product(models.Model):
    prod_id=models.AutoField(primary_key=True)
    prod_name=models.CharField( max_length=50)
    catagory=models.CharField( max_length=50 , default="")
    sub_catagory=models.CharField( max_length=50 , default="")
    price=models.IntegerField(default=0)
    desc=models.CharField( max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='static/IMG' ,default="")
    
    
    def __str__(self):
        return self.prod_name





class Signup(models.Model):
    prod_id=models.AutoField(primary_key=True)
    Username=models.CharField( max_length=50)
    Email=models.CharField( max_length=50)
    Fname=models.CharField( max_length=50)
    Lname=models.CharField( max_length=50)
   
    phone=models.CharField( max_length=10)
    password=models.CharField( max_length=30)
    
    
    
    
    def __str__(self):
        return self.Username 