from django.contrib import admin
from django.contrib.auth.admin import User

class BookrAdmin(admin.AdminSite):
    site_header = "Bookr Administration"

admin_site = BookrAdmin(name="bookr_admin")


# Register your models here.
admin_site.register(User)