from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from .models import job
from .form import applyform ,jobform
from django.contrib.auth.models import User
# Create your views here.
def job_list(request):
    job_list=job.objects.all()
    paginator = Paginator(job_list,2)
    page_number = request.GET.get("page") 
    page_obj = paginator.get_page(page_number)
    context={'jobs':page_obj}

    return render(request,'job/job_list.html',context)

def job_detail(request,slug):
    job_detail=job.objects.get(slug=slug)
    if request.method == "POST":
        
        form = applyform(request.POST, request.FILES)
        if form.is_valid():
          
           my_form= form.save(commit=False)
           my_form.job=job_detail
           my_form.save()
          
    else:
        form = applyform()
       
    context={'job':job_detail,'form':form}
    return render(request,'job/job_detail.html',context)

def add_job(request):
    if request.method == "POST":
        form = jobform(request.POST, request.FILES)
        if form.is_valid():
           my_form= form.save(commit=False)
           my_form.owner=request.user
           my_form.save()
           return redirect (reverse('jobs:job_list'))
    else:
        form = jobform()
    context={'form':form}
    return render(request,'job/add_job.html',context)