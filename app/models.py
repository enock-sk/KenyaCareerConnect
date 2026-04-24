from django.db import models

# Create your models here.

# start of home page models
class Category(models.Model):
    name=models.CharField(max_length=100)
    icon = models.CharField(max_length=50, default='fa-briefcase')
    # job_count=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Location(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class About(models.Model):
    title = models.TextField()
    description = models.TextField()

    point_1 = models.CharField(max_length=255)
    point_2 = models.CharField(max_length=255)
    point_3 = models.CharField(max_length=255)

    button_text = models.CharField(max_length=50, default="Read More")
    button_link = models.CharField(max_length=255, blank=True)

    # images controlled by admin
    image_1 = models.ImageField(upload_to='about/')
    image_2 = models.ImageField(upload_to='about/')
    image_3 = models.ImageField(upload_to='about/')
    image_4 = models.ImageField(upload_to='about/')
# Job Type choices (clean version)
class JobType(models.TextChoices):
    FULL_TIME = "Full Time"
    PART_TIME = "Part Time"


# Job model (MISSING BEFORE — now fixed)
class Job(models.Model):
    title = models.CharField(max_length=200)
    company_logo = models.ImageField(upload_to='logos/')

    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    job_type = models.CharField(
        max_length=20,
        choices=JobType.choices
    )

    is_featured = models.BooleanField(default=False)

    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    deadline = models.DateField()
    description = models.TextField(blank=True)
    responsibilities = models.TextField(blank=True)
    qualifications = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True )

    def __str__(self):
        return self.title

class Client(models.Model):
    icon = models.CharField(max_length=50, default='fa-quote-left')
    image = models.ImageField(upload_to='profiles/')
    description = models.TextField()
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

    # end of home page models
