from django.shortcuts import get_object_or_404, render

from app.models import About, Category, Client, Job, Location


def home(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    about = About.objects.first()
    clients = Client.objects.all()

    # Limit the number of jobs shown on homepage
    featured_jobs = Job.objects.filter(is_featured=True)[:6]
    full_time_jobs = Job.objects.filter(job_type='Full Time')[:6]
    part_time_jobs = Job.objects.filter(job_type='Part Time')[:6]
    for category in categories:
        category.job_count = Job.objects.filter(category=category).count()

    return render(request, 'index.html', {
        "categories": categories,
        "locations": locations,
        "about": about,
        "featured_jobs": featured_jobs,
        "full_time_jobs": full_time_jobs,
        "part_time_jobs": part_time_jobs,
        "clients": clients,
    })


def about(request):
    about = About.objects.first()
    return render(request, 'about.html', {"about": about})


def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')

    # Get filter values from search form
    cat_id = request.GET.get('category')
    loc_id = request.GET.get('location')
    keyword = request.GET.get('keyword')

    # Apply filters
    if cat_id:
        jobs = jobs.filter(category_id=cat_id)
    if loc_id:
        jobs = jobs.filter(location_id=loc_id)
    if keyword:
        jobs = jobs.filter(title__icontains=keyword)

    # Tab data (limited)
    featured_jobs = Job.objects.filter(is_featured=True)[:6]
    full_time_jobs = Job.objects.filter(job_type='Full Time')[:6]
    part_time_jobs = Job.objects.filter(job_type='Part Time')[:6]

    return render(request, 'job-list.html', {
        "jobs": jobs,
        "categories": Category.objects.all(),
        "locations": Location.objects.all(),
        "featured_jobs": featured_jobs,
        "full_time_jobs": full_time_jobs,
        "part_time_jobs": part_time_jobs,
    })


# ==================== JOB DETAIL PAGE ====================
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    # Optional: Related jobs in same category
    related_jobs = Job.objects.filter(
        category=job.category
    ).exclude(id=job.id)[:4]

    return render(request, 'job-detail.html', {
        'job': job,
        'related_jobs': related_jobs,
    })

def contact(request):
    return render(request, 'contact.html')


def error(request):
    return render(request, '404.html')