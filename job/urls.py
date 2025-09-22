from django.urls import path,include
from .import  views
app_name= 'job'
urlpatterns = [
    path('add_job',views.add_job,name='add_job'),
    path('',views.job_list,name='job_list'),
    path('<str:slug>',views.job_detail,name='job_detail')
       

]
