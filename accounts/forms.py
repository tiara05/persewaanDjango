from django.forms import ModelForm
from accounts.models import Customer, Order, Product


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class OrderUbahForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class CusForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'

class ProdForm(ModelForm):
	class Meta:
		model = Product
		fields = '__all__'

class NotaForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'