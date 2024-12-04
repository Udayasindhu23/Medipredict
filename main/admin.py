# admin.py in your 'main' app
from django.contrib import admin
from .models import UserProfile, Role, Medicine  # Adjust based on your actual model names

admin.site.register(UserProfile)
admin.site.register(Role)
admin.site.register(Medicine)  # Assuming you have a Medicine model
