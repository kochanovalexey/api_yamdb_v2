from django.contrib import admin
from .models import User, Genre, Category, Title


admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Title)
