from django.db import models

# Create your models here.

class User_Address(models.Model):
    address_id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=100)
    current = models.BooleanField()
    user_id = models.ForeignKey("User_Accounts", on_delete=models.CASCADE)

class User_Accounts(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)
    password = models.CharField(max_length=200, default="password")

class Appointments(models.Model):
    appointment_id = models.IntegerField(primary_key=True)
    service_id = models.ForeignKey("Services", on_delete=models.CASCADE)
    user_id = models.ForeignKey(User_Accounts, on_delete=models.CASCADE)
    b_user_id = models.ForeignKey("Business_User_Accounts", on_delete=models.CASCADE)
    date_time = models.DateTimeField()

class Business_User_Address(models.Model):
    address_id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=100)
    current = models.BooleanField()
    user_id = models.ForeignKey("Business_User_Accounts", on_delete=models.CASCADE)

class Business_User_Accounts(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    business_name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=10)
    password = models.CharField(max_length=200, default="password")

class Services(models.Model):
    service_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField()
    b_user_id = models.ForeignKey(Business_User_Accounts, on_delete=models.CASCADE)
    price = models.IntegerField()

class Appointment_History(models.Model):
    appointment_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User_Accounts, on_delete=models.PROTECT)
    b_user_id = models.ForeignKey(Business_User_Accounts, on_delete=models.PROTECT)
    date_time = models.DateTimeField()

class Feedback(models.Model):
    feedback_id = models.IntegerField(primary_key=True)
    rating = models.IntegerField()
    review = models.CharField(max_length=150)
    user_id = models.ForeignKey(User_Accounts, on_delete=models.PROTECT)
    b_user_id = models.ForeignKey(Business_User_Accounts, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)

class Membership(models.Model):
    membership_id = models.IntegerField(primary_key=True)
    membership_type = models.CharField(max_length=50)
    user_id = models.ForeignKey(User_Accounts, on_delete=models.CASCADE)

