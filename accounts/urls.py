from django.urls import path
import accounts.views as views


urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.awal, name="awal"),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('create_customer/', views.createCustomer, name="create_customer"),
    path('create_product/', views.createProduct, name="create_product"),
    path('update_cus/<str:pk>/', views.updateProduct, name="update_prod"),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('update_ubah/<str:pk>/', views.updateOrder, name="update_order"),
    path('update_customer/<str:pk>/', views.updateCustomer, name="update_customer"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('nota/<str:pk>/', views.nota, name="nota"),
    path('delete_prod/<str:pk>/', views.deleteProd, name="delete_prod"),
    path('datavisualumur/', views.CustomerViewumur, name="datavisualumur"),
    path('datavisualalamat/', views.CustomerViewalamat, name="datavisualalamat"),
    path('datavisualpendapatan/', views.CustomerViewpendapatan, name="datavisualpendapatan"),
    path('datavisualjenis/', views.CustomerViewjenis, name="datavisualjenis"),
]   