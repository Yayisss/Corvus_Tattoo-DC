from django.urls import path
from .views import home, products, exit, login, citas

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('products/', products, name='products'),
    path('citas/', citas, name='citas'),
    path('logout/', exit, name='exit'),
    
]