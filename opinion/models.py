from django.db import models

# Create your models here.

class opinion(models.Model):
	
	wards=[
   ('Tudun Wada South', 'Tudun Wada South'),
   
	('Tudun Wada North', 'Tudun Wada North'),
	
	('Minna South', 'Minna South'),
	
	('Makera', 'Makera'),
	
	('Minna Central', 'Minna Central'),
	
	('Limawa A', 'Limawa A'),
	
	('Limawa B', 'Limawa B'),
	
	('Sabon Gari', 'Sabon Gari'),
	('Nasarawa A', 'Nasarawa A'),
	
	('Nasarawa B', 'Nasarawa B'),
	
	('Nasarawa C', 'Nasarawa C')
	
	]
	language=[
   ('HTML', 'HTML'),
   
	('CSS', 'CSS'),
	
	('JAVASCRIPT', 'JAVASCRIPT'),
	
	('PYTHON', 'PYTHON')
	]
	
	sex=[
   ('male', 'male'),
   
	('female', 'female')
	]
	
	state=[
   ('Niger', 'Niger')
	]
	LGA=[
   ('Chanchaga', 'Chanchaga')
	]
	
	sex=models.CharField(
	max_length=255,
	choices=sex,
	default=('male', 'male')
	)
	state=models.CharField(
	max_length=255,
	choices=state,
	default=('Niger', 'Niger')
	)
	LGA=models.CharField(
	max_length=255,
	choices=LGA,
	default=('Chanchaga', 'Chanchaga')
	)
	ward=models.CharField(
	max_length=255,
	choices=wards,
	default=('Limawa A', 'Limawa A')
	)
	phone_number=models.CharField(max_length=255)
	programming_language=models.CharField(
	max_length=255,
	choices=language,
	default=('JAVASCRIPT', 'JAVASCRIPT')
	)
	
	def __str__(self):
		return f"{self.sex}  {self.state}  {self.LGA}  {self.ward}  {self.phone_number}  {self.programming_language}"
	
