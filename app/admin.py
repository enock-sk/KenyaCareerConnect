from django.contrib import admin

from app.models import About, Category, Client, Job, Location
# start of home page registers


# Register your models here.
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(About)
admin.site.register(Job)
admin.site.register(Client)



# end of home page registers