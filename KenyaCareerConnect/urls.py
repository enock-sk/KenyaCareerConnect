from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from KenyaCareerConnect import settings
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
     path('jobs/', views.job_list, name='job_list'),                    # Cleaner URL
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),    # ← This is the most important fix,
    path('contact/',views.contact,name="contact"),
    path('error/',views.error,name="error")
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
