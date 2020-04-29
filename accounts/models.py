from django.db import models

# Create your models here.

class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	umur = models.CharField(max_length=200, null=True)
	alamat = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	priceweek = models.FloatField(null=True)
	pricemonth = models.FloatField(null=True)
	stok = models.FloatField(null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = (
			('Booking', 'Booking'), 
			('Pinjam', 'Pinjam'), 
			('Selesai', 'Selesai')
			)
	PINJAM = (
		('1 Hari', '1 Hari'), 
		('1 Minggu', '1 Minggu'), 
		('1 Bulan', '1 Bulan')
	)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	pinjam = models.CharField(max_length=200, null=True, choices=PINJAM)
	total = models.FloatField(max_length=200, null=True)

	def __str__(self):
		return self.product.name

