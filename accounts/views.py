from django.shortcuts import render, redirect 
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import OrderForm
from .forms import CusForm
from accounts.forms import NotaForm, OrderUbahForm, ProdForm
from matplotlib import pyplot as plt
import numpy as np
from django.views.generic import TemplateView
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.models import ColumnDataSource
from bokeh.palettes import Paired12
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

def awal(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Selesai').count()
	booking = orders.filter(status='Booking').count()
	pending = orders.filter(status='Pinjam').count()

	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,'booking':booking,
	'pending':pending }

	return render(request, 'accounts/awal.html', context)

def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Selesai').count()
	pending = orders.filter(status='Pinjam').count()
	booking = orders.filter(status='Booking').count()

	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,'booking':booking,
	'pending':pending }

	return render(request, 'accounts/dashboard.html', context)

def products(request):
	products = Product.objects.all()
	

	return render(request, 'accounts/products.html', {'products':products})

def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	context = {'customer':customer, 'orders':orders, 'order_count':order_count}
	return render(request, 'accounts/customer.html',context)

def coba(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	context = {'customer':customer, 'orders':orders, 'order_count':order_count}
	return render(request, 'accounts/datavisual.html',context)


def createCustomer(request):
	form = CusForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = CusForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	
	return render(request, 'accounts/create_cus.html', context)
	
def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

def createProduct(request):
	form = ProdForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = ProdForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			

	context = {'form':form}
	return render(request, 'accounts/create_product.html', context)

def updateProduct(request, pk):

	prod = Product.objects.get(id=pk)
	form = ProdForm(instance=prod)

	if request.method == 'POST':
		form = ProdForm(request.POST, instance=prod)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/update_prod.html', context)

def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderUbahForm(instance=order)

	if request.method == 'POST':
		form = OrderUbahForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/orderubah.html', context)

def updateCustomer(request, pk):

	cus = Customer.objects.get(id=pk)
	form = CusForm(instance=cus)

	if request.method == 'POST':
		form = CusForm(request.POST, instance=cus)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/updatecus.html', context)

def deleteProd(request, pk):
	order = Product.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'accounts/delete_prod.html', context)

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'accounts/delete.html', context)


def CustomerViewumur(request):
	def get_context_data(**kwargs):
		context = super().get_context_data(**kwargs)
		context['qs'] = Customer.objects.all()
		return context
	return render(request, 'accounts/datavisualumur.html')
def CustomerViewjenis(request):
	def get_context_data(**kwargs):
		context = super().get_context_data(**kwargs)
		context['qs'] = Customer.objects.all()
		return context
	return render(request, 'accounts/datavisualjenis.html')
def CustomerViewpendapatan(request):
	def get_context_data(**kwargs):
		context = super().get_context_data(**kwargs)
		context['qs'] = Customer.objects.all()
		return context
	return render(request, 'accounts/datavisualpendapatan.html')
def CustomerViewalamat(request):
	def get_context_data(**kwargs):
		context = super().get_context_data(**kwargs)
		context['qs'] = Customer.objects.all()
		return context
	return render(request, 'accounts/datavisualalamat.html')

def nota(request, pk):
	cus = Order.objects.get(id=pk)
	form = NotaForm(instance=cus)

	if request.method == 'POST':
		form = NotaForm(request.POST, instance=cus)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	
	return render(request, 'accounts/nota.html', context)

