from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login_view,name='login_view'),
    path('register',views.register,name='register'),
    path('home/', views.customer, name='customer'),
    path('home/purchase',views.nextpage,name='purchase'),
    path('create-requisition/', views.create_requisition, name='create_requisition'),
    path('generate-requisition-id/', views.generate_requisition_id, name='generate_requisition_id'),
     path('add-lines/', views.add_lines, name='add_lines'),
     path('nextpage/',views.nextpage,name='nextpage'),
     path('manager/',views.manager_view,name='managerview'),
     path('update_status/', views.update_status, name='update_status'),
      path('check-status/', views.check_status, name='check_status'),
]

