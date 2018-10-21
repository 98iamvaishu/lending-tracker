from transact.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', home1, name='home1'),
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signin1/', signin1, name='signin1'),
    path('logout/', logout1, name='logout'),
    path('test/', test, name='test'),
    path('create/', create, name='create'),
    path('borrow/', borrower, name='borrow'),
    path('list1/', list1, name='list1'),
    path('paid/', paidfun, name='paid'),
]
