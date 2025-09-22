from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.
JOB_TYPE=(
    ('Intenship','Intenship'),
    ('Freelance','Freelance'),
    ('Full Time','Full time'),
    ('Part Time','Part Time')
)

cities=(
    ('A','Cairo'),
    ('Alexandria','Alexandria'),
    ('Giza',' Giza'),
    ('Luxor','Luxor'),
    ('Aswan','Aswan'),
    ('Port Said','Port Said'),
    ('Suez','Suez')
    
)
def image_upload(instance,filename):
    image_name, extension=filename.split(".")
    return "jobs/%s.%s"%(instance.title,extension)
class job(models.Model):
    owner=models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE)
    title =models.CharField(max_length=100)
    past_at=models.DateTimeField(auto_now=True)
    salary=models.IntegerField(default=0)
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    decription=models.TextField(max_length=1000,default="")
    about_campany=models.TextField(max_length=1000,default="")
    experience=models.IntegerField(default=1)
    category=models.ForeignKey('category',on_delete=models.CASCADE)
    job_image=models.ImageField(upload_to=image_upload)
    location=models.CharField(choices=cities)
    slug =models.SlugField(blank=True,null=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):  # new
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
class category(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name
        
class applyer(models.Model):
    job=models.ForeignKey(job,related_name='apply_job',on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    Email=models.EmailField()
    cv=models.FileField(upload_to='apply/') 
    cover_letter=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
        