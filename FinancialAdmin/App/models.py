from django.db import models

class Register(models.Model):
          Uname = models.CharField(max_length=30)
          No = models.IntegerField()
          Email =models.EmailField(max_length=40)
          password = models.CharField(max_length=30)
          
          def __str__(self):
                    return self.Uname
class customer(models.Model):
          cid=models.AutoField(primary_key=True)
          cname=models.CharField(max_length=30)
          cemail=models.EmailField(max_length=30)
          cmobile=models.IntegerField()
          place=models.CharField(max_length=30)
          date=models.DateField()
          time=models.TimeField()
          
          def __str__(self):
                    return self.cname
class Products(models.Model):
          pname=models.CharField(max_length=30)
          coname=models.CharField(max_length=30)
          price=models.IntegerField()
          quantity=models.IntegerField()
          exp=models.DateField()
          
          def __str__(self):
                    return self.pname
          
class Cart(models.Model):
          product=models.ForeignKey(Products,on_delete=models.CASCADE,related_name="Productname")
class CartDetails(models.Model):
          id=models.AutoField(primary_key=True)
          productname=models.CharField(max_length=30)
          cusname=models.CharField(max_length=30)
          pquantity=models.IntegerField()
          pprice=models.IntegerField()
          pdate=models.DateField()
          ptime=models.TimeField()
          
          def __str__(self):
                    return self.cusname

