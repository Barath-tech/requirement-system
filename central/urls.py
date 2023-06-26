from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login_view,name='login_view'),
    path('register',views.register,name='register'),
    path('home/', views.customer, name='customer'),
    path('home/purchaseorder',views.nextpage,name='purchaseorder'),
    path('manager/', views.manager, name='manager'),
    path('create-requisition/', views.create_requisition, name='create_requisition'),
    path('save-requisition/', views.save_requisition, name='save_requisition'),
     path('add-lines/', views.add_lines, name='add_lines'),
     path('nextpage/',views.nextpage,name='nextpage')

]

